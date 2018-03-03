# -*- coding:utf-8 -*-

import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import  ZhihuiSMB.libs.utils as utils
import ZhihuiSMB.apps.user.model as user_model

class NoticeModel(model.StandCURDModel):
    _coll_name = "notice"
    _columns=[
        ("notice_title",StrDT(required=True)),
        ("notice_text",StrDT(required=True)),
        ("images_list", ListDT()),
    ]


    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(NoticeModel, self).__init__()


    def before_create(self,object):
        user = user_model.UserModel.get_username_by_id(object['add_user_id'])
        object["add_user_name"] = user['name']
        object["add_user_jobno"] = user['job_no']
        images = self.save_images(object['add_user_jobno'], object['images_list'])
        del object['images_list']
        object['images'] = images
        self.coll.save(object)
        return object

    def after_create(self,object):
        noticeread_coll = model.BaseModel.get_model("noticeread.NoticereadModel").get_coll()
        _noticeread = noticeread_coll.find()
        for i in _noticeread:
            i["unread_msg"].append(utils.objectid_str(object['_id']))
            noticeread_coll.save(i)
        return object

    def after_delete(self,object):
        msg_id = utils.objectid_str(object["_id"])
        noticeread_coll = model.BaseModel.get_model("noticeread.NoticereadModel").get_coll()
        _noticeread = noticeread_coll.find()
        for i in _noticeread:
            if msg_id in i["unread_msg"]:
                i["unread_msg"].remove(msg_id)
                noticeread_coll.save(i)
        return object

    def unread_msg(self):
        user_mobile = user_model.UserModel.get_user_mobile_by_token(self._arguments["access_token"])
        noticeread_coll = model.BaseModel.get_model("noticeread.NoticereadModel").get_coll()
        noticeread = noticeread_coll.find_one({"user_id":user_mobile["mobile"]})
        return noticeread

    def save_images(self,add_user_jobno,images_list):
        images=[]
        for i in images_list:
            if i =="":
                pass
            else:
                try:
                    uri = utils.str_to_img("notice/%s_%s.png"%(add_user_jobno,utils.get_uuid()),i)
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





