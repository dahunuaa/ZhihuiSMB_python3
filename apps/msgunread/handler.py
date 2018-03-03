# -*- coding:utf-8 -*-

from ZhihuiSMB.apps.base.handler import MultiStandardHandler,SingleStandardHanler,TokenHandler
from ZhihuiSMB.libs.oauthlib import get_provider

class MsgunreadHandler(MultiStandardHandler,TokenHandler):
    _model = "msgunread.MsgunreadModel"
    enable_methods = ["put","get"]
    private = False

    def _put(self):
        user_id = self.get_argument("user_id")
        msg_type = self.get_argument("type")
        msg_id = self.get_argument("msg_id")
        res = self.model.minus(user_id,msg_type,msg_id)
        self.result['data'] =res


handlers = [
    (r"/minus",MsgunreadHandler,get_provider("msgunread")),
    (r"",MsgunreadHandler,get_provider("msgunread"))
]