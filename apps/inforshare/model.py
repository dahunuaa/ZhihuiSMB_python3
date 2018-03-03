# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
import ZhihuiSMB.apps.user.model as user_model
from ZhihuiSMB.libs.datatypelib import *

class InforshareModel(model.StandCURDModel):
    _coll_name = "inforshare"
    _columns = [
        ("infor_title",StrDT()),
        ("infor_type",StrDT()),
        ("infor_text",StrDT()),
        ("images_list",ListDT()),
        ("filename", StrDT()),
        ("filepath", StrDT()),
    ]

    def before_create(self,object):
        user=user_model.UserModel.get_username_by_id(object['add_user_id'])
        object["add_user_name"] =user['name']
        object["add_user_jobno"]=user['job_no']
        images = self.save_images(object['add_user_jobno'],object['images_list'])
        del object['images_list']
        object['images']=images
        self.coll.save(object)
        return object

    def after_create(self,object):
        msgunread_coll = model.BaseModel.get_model("msgunread.MsgunreadModel").get_coll()
        _msgunread = msgunread_coll.find()
        for i in _msgunread:
            i["inforshare_unread"].append(utils.objectid_str(object['_id']))
            msgunread_coll.save(i)
        return object

    def save_images(self,add_user_jobno,images_list):
        images=[]
        for i in images_list:
            if i =="":
                pass
            else:
                try:
                    uri = utils.str_to_img("inforshare/%s_%s.png"%(add_user_jobno,utils.get_uuid()),i)
                    url = self.get_host()+uri
                except:
                    url = i
                images.append(url)
        return images

    def before_update(self,object):
        _object = self._get_from_id(update=True)
        images_list = self.get_argument("images_list")
        images = self.save_images(_object['add_user_jobno'], images_list)
        del object['images_list']
        object['images'] = images
        _object.update(object)
        return _object

    def after_delete(self,object):
        msg_id = utils.objectid_str(object["_id"])
        msgunread_coll = model.BaseModel.get_model("msgunread.MsgunreadModel").get_coll()
        _msgunread = msgunread_coll.find()
        for i in _msgunread:
            if msg_id in i["inforshare_unread"]:
                i["inforshare_unread"].remove(msg_id)
                msgunread_coll.save(i)
        return object

    def unread_msg(self):
        user_mobile = user_model.UserModel.get_user_mobile_by_token(self._arguments["access_token"])
        msgunread_coll = model.BaseModel.get_model("msgunread.MsgunreadModel").get_coll()
        msgunread = msgunread_coll.find_one({"user_id":user_mobile["job_no"]})
        return msgunread

    def classify(self):
        result = utils.dump(self.coll.aggregate([{"$group":{"_id":"$infor_type",
                                                    "num":{"$sum":1}}},
                                                  {"$sort":{"num":-1}}
                                                  ]))
        return result