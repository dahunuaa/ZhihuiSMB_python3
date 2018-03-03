# -*- coding:utf-8 -*-

from ZhihuiSMB.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from ZhihuiSMB.libs.loglib import get_logger
from ZhihuiSMB.libs.oauthlib import get_provider

logger = get_logger("debug")

class ScopeHandler(SingleStandardHanler,TokenHandler):
    _model = "scope.ScopeModel"
    peivate =False
    enable_methods = ["get"]

    def get(self):
        return super(ScopeHandler,self).get(self.scope['_id'])

handlers = [
    (r"",ScopeHandler,get_provider('scope'))
]