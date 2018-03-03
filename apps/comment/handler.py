# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from ZhihuiSMB.libs.oauthlib import get_provider

class CommentListHandler(MultiStandardHandler,TokenHandler):
    _model = "comment.CommentHandler"
    enable_methods = ["post","get"]
    private = False

class CommentHandler(SingleStandardHanler,TokenHandler):
    _model = "comment.CommentHandler"
    enable_methods = ["get","delete","put"]
    private = False

class CommentLikeHandler(SingleStandardHanler,TokenHandler):
    _model = "comment.CommentHandler"
    enable_methods = ["put"]
    private= False

    def put(self):
        comment_id = self.get_argument("comment_id")
        type = self.get_argument("type")
        user_id = self.get_argument("user_id")
        res = self.model.alter_comment_like(comment_id,type,user_id)
        self.finish(res)




handlers = [
    (r"",CommentListHandler,get_provider("comment")),
    (r"/like_amount",CommentLikeHandler,get_provider("comment")),
    (r"/(.*)",CommentHandler,get_provider("comment"))
]
