# -*- coding:utf-8 -*-

from ZhihuiSMB.apps.base.handler import APIHandler,TokenHandler,SingleStandardHanler,MultiStandardHandler
from ZhihuiSMB.libs.loglib import get_logger
from ZhihuiSMB.libs.oauthlib import get_provider

logger = get_logger("debug")

class UserRegisterHandler(MultiStandardHandler):
    _model = "user.UserModel"
    enable_methods = ['post']

    def _post(self):
        res = self.model.new()
        self.result["data"]=res

class UserLoginHandler(MultiStandardHandler):
    _model = "user.UserModel"
    enable_methods = ['post']

    def _post(self):
        job_no = self.get_argument('job_no',None)
        password = self.get_argument('password',None)
        if job_no is None or password is None:
            raise ValueError(u"用户名或密码为空")
        res = self.model.login(job_no,password)
        self.result['data']=res

# class CompleteHandler(MultiStandardHandler,TokenHandler):
#     _model = "user.UserModel"
#     def _post(self):


class UserPswChangeHandler(MultiStandardHandler,TokenHandler):
    _model = "user.UserModel"
    enable_methods = ['put']

    def _put(self):
        job_no = self.get_argument("job_no",None)
        oldpsw = self.get_argument("oldpsw",None)
        newpsw = self.get_argument("newpsw",None)
        if job_no is None or newpsw  is None:
            raise ValueError(u"手机号或密码为空")
        res = self.model.changepsw(job_no,oldpsw,newpsw)
        self.result['data'] = res

class UserPswResetHandler(MultiStandardHandler,TokenHandler):
    _model = "user.UserModel"
    enable_methods = ["put"]

    def _put(self):
        reset_psw = self.get_argument("reset_psw",None)
        mobile = self.get_argument("mobile",None)
        res = self.model.reset_psw(mobile,reset_psw)
        self.result['data'] = res


class UserListHandler(MultiStandardHandler,TokenHandler):
    _model = "user.UserModel"
    enable_methods = ['get','post','put','delete']
    private = False


class UserHandler(SingleStandardHanler,TokenHandler):
    _model = "user.UserModel"
    enable_methods = ['get','delete','put']
    private = False

class GetcontactHandler(MultiStandardHandler,TokenHandler):
    _model = "user.UserModel"
    enable_methods = ['get']

    def _get(self):
        position = self.get_argument("position")
        res = self.model.getcontact(position)
        self.result["data"]=res


handlers = [
    (r"/register",UserRegisterHandler),
    (r"/login",UserLoginHandler),
    (r"/getcontact",GetcontactHandler,get_provider("user")),
    (r'/psw/change',UserPswChangeHandler,get_provider("user")),
    (r'/psw/reset',UserPswResetHandler,get_provider("user_admin")),
    (r"",UserListHandler,get_provider("user")),
    (r"/(.*)",UserHandler,get_provider("user"))
]