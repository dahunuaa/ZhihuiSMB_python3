# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.apps.user.model as user_model

class PtosModel(model.StandCURDModel):
    _coll_name = "ptos"
    _columns=[
        ("title",StrDT(required=True)),
        ("category",StrDT(required=True)),
        ("context",StrDT()),
        ("images_list",ListDT()),
        ("to_name",StrDT()),
        ("to_no",StrDT()),
        ("project_no", StrDT()),
        ("result",StrDT())
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
            i["ptos_unread"].append(utils.objectid_str(object['_id']))
            msgunread_coll.save(i)
        return object

    def save_images(self,add_user_jobno,images_list):
        images=[]
        for i in images_list:
            if i =="":
                pass
            else:
                try:
                    uri = utils.str_to_img("ptos/%s_%s.png"%(add_user_jobno,utils.get_uuid()),i)
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
            if msg_id in i["ptos_unread"]:
                i["ptos_unread"].remove(msg_id)
                msgunread_coll.save(i)
        return object

    def unread_msg(self):
        user_mobile = user_model.UserModel.get_user_mobile_by_token(self._arguments["access_token"])
        msgunread_coll = model.BaseModel.get_model("msgunread.MsgunreadModel").get_coll()
        msgunread = msgunread_coll.find_one({"user_id":user_mobile["job_no"]})
        return msgunread

    def add_result(self,result,ptos_id):
        ptos = self.coll.find_one({"_id": utils.create_objectid(ptos_id)})
        if not ptos:
            raise ValueError(u"无该记录")
        ptos["result"]=result
        self.coll.save(ptos)
        return utils.dump(ptos)

    # def update(self):
    #     res = utils.dump(self.coll.find())
    #     for i in res:
    #         i["add_time"] = utils.strtodatetime(i["add_time"], '%Y-%m-%d %H:%M:%S')
    #         i["last_updated_time"] = utils.strtodatetime(i["last_updated_time"], '%Y-%m-%d %H:%M:%S')
    #         self.coll.save(i)