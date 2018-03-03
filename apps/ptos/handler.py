# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from ZhihuiSMB.libs.oauthlib import get_provider

class PtosListHandler(MultiStandardHandler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["post","get"]
    private = False

class PtosHandler(SingleStandardHanler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["get","put","delete"]
    private = False

class AddresultHandler(SingleStandardHanler,TokenHandler):
    _model = "ptos.PtosModel"
    enable_methods = ["put"]
    private = False
    def put(self):
        result = self.get_argument("result",None)
        ptos_id = self.get_argument("ptos_id", None)
        res = self.model.add_result(result,ptos_id)
        self.result["data"]=res
        self.finish(self.result)

handlers =[
    (r"",PtosListHandler,get_provider("ptos")),
    (r"/add_result",AddresultHandler,get_provider("ptos")),
    (r"/(.*)",PtosHandler,get_provider("ptos"))
]