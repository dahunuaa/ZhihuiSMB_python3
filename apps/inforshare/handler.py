# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from ZhihuiSMB.libs.oauthlib import get_provider

class InforshareListHandler(MultiStandardHandler,TokenHandler):
    _model = "inforshare.InforshareModel"
    enable_methods = ["post","get"]
    private = False

class InforshareClassifyHandler(MultiStandardHandler,TokenHandler):
    _model = "inforshare.InforshareModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        self.result["data"] = self.model.classify()
        self.finish(self.result)

class InforshareHandler(SingleStandardHanler,TokenHandler):
    _model = "inforshare.InforshareModel"
    enable_methods = ["get","put","delete"]
    private = False


handlers=[
    (r"",InforshareListHandler,get_provider("inforshare")),
    (r"/classify",InforshareClassifyHandler,get_provider("inforshare")),
    (r"/(.*)",InforshareHandler,get_provider("inforshare"))
]
