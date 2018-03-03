# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.apps.user.model as user_model

class PtosaddModel(model.StandCURDModel):
    _coll_name="ptosadd"
    _columns = [
        ("ptos_id",StrDT(required=True)),
        ("context", StrDT()),
        ("images_list", ListDT()),
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