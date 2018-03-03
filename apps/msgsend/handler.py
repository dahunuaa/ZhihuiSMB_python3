# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import MultiStandardHandler,SingleStandardHanler,TokenHandler
from ZhihuiSMB.libs.oauthlib import get_provider
import ZhihuiSMB.sendmsg.aliyun.demo as demo
import uuid

class MsgSendHandler(MultiStandardHandler,TokenHandler):
    _model="msgsend.MsgSendModel"
    enable_methods = ["get"]
    private =False
    def get(self):
        __business_id = uuid.uuid1()
        name = self.get_argument("name")
        job_no = self.get_argument("job_no")
        mobile = self.model.get_mobile_by_job_no(job_no)
        params = {"name":name}
        self.result["data"]=demo.send_sms(__business_id,mobile,"ZhihuiSMB系统","SMS_125018960",params)
        self.finish(self.result)


handlers=[
    (r"",MsgSendHandler,get_provider("msgsend"))
]