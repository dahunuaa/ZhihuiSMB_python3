# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
import ZhihuiSMB.apps.user.model as user_model
from ZhihuiSMB.libs.datatypelib import *

class MsgSendModel(model.StandCURDModel):
    _coll_name = "msgsend"
    _columns = [

    ]

    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(MsgSendModel, self).__init__()

    def get_mobile_by_job_no(self,job_no):
        user = self.user_coll.find_one({"job_no":job_no})
        mobile = user['mobile']
        return mobile