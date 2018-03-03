# -*- coding:utf-8 -*-

import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *

class CommentHandler(model.StandCURDModel):
    _coll_name = "comment"
    _columns = [
        ("comment_type",StrDT(required=True)),
        ("text_id",StrDT(required=True)),
        ("user_id",StrDT(required=True)),#工号/手机号
        ("text",StrDT(required=True)),
    #     添加回复功能 user_id是评论的人 下面的to_user_id是回复的人
        ("to_user_id", StrDT()),
        ("to_user_name", StrDT()),
        ("father_comment_id", StrDT()),
        ("comment_status", StrDT()),
        ("childen_comment_ids", ListDT()),
        ("like_amounts", IntDT(default=0)),
        ("like_users", ListDT()),
    ]

    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(CommentHandler, self).__init__()


    def before_create(self, object):
        user = self.user_coll.find_one({"_id": utils.create_objectid(object['add_user_id'])})
        object['add_user_name'] = user['name']
        father_id = self.get_argument("father_comment_id")
        self.coll.save(object)
        if father_id is not None:
            father_comment = self.coll.find_one({"_id": utils.create_objectid(father_id)})
            if father_comment is not None:
                # father_comment['childen_comment_ids'].append(utils.objectid_str(object["_id"]))
                father_comment['childen_comment_ids'].append(utils.dump(object))
                self.coll.save(father_comment)
        return object

    def before_delete(self,object):
        user_id = self.get_argument("user_id")
        if user_id != object['user_id']:
            raise ValueError(u"你无权限删除该评论！")
        return object

    def alter_comment_like(self,comment_id,type,user_id):
        comment = self.coll.find_one({"_id": utils.create_objectid(comment_id)})
        if user_id in comment["like_users"]:
            raise ValueError(u"Allow only one agreement")
        else:
            if type == "1":
                comment["like_amounts"] = comment["like_amounts"]+1
                comment["like_users"].append(user_id)
            elif type=="0":
                comment["like_amounts"] = comment["like_amounts"]-1
                comment["like_users"].remove(user_id)
            else:
                raise ValueError(u"类型错误")
            self.coll.save(comment)
            res = utils.dump(self.coll.find_one({"_id": utils.create_objectid(comment_id)}))
        return res










