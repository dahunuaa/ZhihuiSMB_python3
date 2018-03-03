# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from ZhihuiSMB.libs.oauthlib import get_provider

class AdminScopeListHandler(MultiStandardHandler,TokenHandler):
    _model = "scope.ScopeModel"

class AdminScopeHandler(SingleStandardHanler,TokenHandler):
    _model = "scope.ScopeModel"

handlers =[
    (r"",AdminScopeListHandler,get_provider('scope')),
    (r"/(.*)",AdminScopeHandler,get_provider('scope'))
]