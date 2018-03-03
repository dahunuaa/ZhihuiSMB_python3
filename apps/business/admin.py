# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from ZhihuiSMB.libs.loglib import get_logger
from ZhihuiSMB.libs.oauthlib import get_provider

logger = get_logger("debug")

class AdminBusinessListHandler(MultiStandardHandler,TokenHandler):
    _model = "business.BusinessModel"
    private = False

class AdminBussinessHandler(SingleStandardHanler,TokenHandler):
    _model = "business.BusinessModel"
    private = False

handlers = [
    (r"",AdminBusinessListHandler,get_provider("business_admin")),
    (r"/(.*)",AdminBussinessHandler,get_provider("business_admin"))
]
