# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *

class FeedbackModel(model.StandCURDModel):
    _coll_name = "feedback"
    _columns = [
        ("feedback_content",StrDT(required=True)),
        ("images_list", ListDT()),
    ]

    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(FeedbackModel,self).__init__()

    def before_create(self, object):
        user = self.user_coll.find_one({"_id": utils.create_objectid(object['add_user_id'])})
        object["add_user_name"] = user['name']
        object["add_user_jobno"] = user['job_no']
        images = self.save_images(object['add_user_jobno'], object['images_list'])
        del object['images_list']
        object['images'] = images
        self.coll.save(object)
        return object

    def save_images(self, add_user_jobno, images_list):
        images = []
        for i in images_list:
            if i == "":
                pass
            else:
                try:
                    uri = utils.str_to_img("feedback/%s_%s.png" % (add_user_jobno, utils.get_uuid()), i)
                    url = self.get_host() + uri
                except:
                    url = i
                images.append(url)
        return images

    def before_update(self, object):
        _object = self._get_from_id(update=True)
        images_list = self.get_argument("images_list")
        images = self.save_images(_object['add_user_jobno'], images_list)
        del object['images_list']
        object['images'] = images
        _object.update(object)
        return _object

