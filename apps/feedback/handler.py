# -*- coding:utf-8 -*-

from ZhihuiSMB.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from ZhihuiSMB.libs.loglib import get_logger
from ZhihuiSMB.libs.oauthlib import get_provider

logger = get_logger("debug")

class FeedbackListHandler(MultiStandardHandler,TokenHandler):
    _model = "feedback.FeedbackModel"
    enable_methods = ['post','get']
    private = False

class FeedbackHandler(SingleStandardHanler,TokenHandler):
    _model = "feedback.FeedbackModel"
    enable_methods = ['get','delete']

handlers = [
    (r"",FeedbackListHandler,get_provider("feedback")),
    (r"/(.*)",FeedbackHandler,get_provider("feedback_admin"))
]