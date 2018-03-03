# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.apps.user.model as user_model
import ZhihuiSMB.apps.ptos.model as ptos_model

class PtosresultModel(model.StandCURDModel):
    _coll_name="ptosresult"
    _columns = [
        ("ptos_id",StrDT(required=True)),
        ("remark", StrDT()),
        ("images_list",ListDT()),
        ("result", StrDT()),
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
        ptos_coll = model.BaseModel.get_model("ptos.PtosModel").get_coll()
        _ptos_coll = ptos_coll.find_one({"_id":utils.create_objectid(object["ptos_id"])})
        if _ptos_coll is not None:
            _ptos_coll["result"]=object["result"]
        ptos_coll.save(_ptos_coll)
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