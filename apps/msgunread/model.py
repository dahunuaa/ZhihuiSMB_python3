# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *

class MsgunreadModel(model.StandCURDModel):
    _coll_name = "msgunread"
    _columns = [
        ("user_id",StrDT(required=True)),
        ("ptos_unread",ListDT()),
        ("inforshare_unread", ListDT())
    ]

    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(MsgunreadModel,self).__init__()#此处必须加上self

    def init(self):
        user_coll = self.user_coll.find()
        for i in user_coll:
            _mobile = i["mobile"]
            _unread = self.coll.find_one({"user_id":_mobile})
            if not  _unread:
                msgunread = {
                    "user_id":_mobile,
                    "ptos_unread":[],
                    "inforshare_unread": []
                }
                self.coll.save(msgunread)

    def minus(self,user_id,type,msg_id):
        _msgunread=self.coll.find_one({"user_id":user_id})
        if type == "ptos":
            if msg_id in _msgunread["ptos_unread"]:
                _msgunread["ptos_unread"].remove(msg_id)
        elif type == "inforshare":
            if msg_id in _msgunread["inforshare_unread"]:
                _msgunread["inforshare_unread"].remove(msg_id)
        else:
            raise ValueError(u"类型错误")
        self.coll.save(_msgunread)
        return utils.dump(_msgunread)


