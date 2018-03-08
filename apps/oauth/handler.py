# -*- coding:utf-8 -*-
from oauth2.web.tornado import OAuth2Handler
from ZhihuiSMB.apps.base.handler import TokenHandler,MultiStandardHandler
from ZhihuiSMB.apps.base.model import BaseModel
from ZhihuiSMB.libs.oauthlib import get_provider

class OauthHandler(MultiStandardHandler,TokenHandler):
    _model = "oauth.OauthAccessTokenModel"
    enable_methods = ["post","get"]

    # def _post(self):
    #     user_model = BaseModel.get_model("user.UserModel")
    #     user = user_model.get_user_infor(self.user_id)
    #     self.result["data"] = user

handlers = [
    (r'',OauthHandler,get_provider('oauth')),
    (r'/token',OAuth2Handler,get_provider())
]