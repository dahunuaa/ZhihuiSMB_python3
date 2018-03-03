# -*- coding:utf-8 -*-
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.apps.base.model as model

class LikeModel(model.StandCURDModel):
    _coll_name = "like"
    _columns = [
        ("user_id",StrDT(required=True)),
        ("ptos_like", ListDT()),
        ("inforshare_like", ListDT()),
        ("ptos_like_detail", ListDT()),
        ("inforshare_like_detail", ListDT())
    ]

    def __init__(self):
        self.user_coll = model.BaseModel.get_model("user.UserModel").get_coll()
        super(LikeModel, self).__init__()

    def init(self):
        user_coll = self.user_coll.find()
        for i in user_coll:
            _job_no = i["job_no"]
            _like = self.coll.find_one({"user_id":_job_no})
            if not  _like:
                like = {
                    "user_id":_job_no,
                    "ptos_like":[],
                    "inforshare_like":[],
                }
                self.coll.save(like)

    def alter(self,user_id,type,like_id):
        _like = self.coll.find_one({"user_id":user_id})
        if type =="ptos":
            if like_id in _like["ptos_like"]:
                _like["ptos_like"].remove(like_id)
            else:
                _like["ptos_like"].append(like_id)
        if type =="inforshare":
            if like_id in _like["inforshare_like"]:
                _like["inforshare_like"].remove(like_id)
            else:
                _like["inforshare_like"].append(like_id)
        self.coll.save(_like)
        return utils.dump(_like)

    def like_list(self,user_id):
        ptos_coll = model.BaseModel.get_model("ptos.PtosModel").get_coll()
        inforshare_coll = model.BaseModel.get_model("inforshare.InforshareModel").get_coll()
        like_coll=self.coll.find_one({"user_id":user_id})
        ptos_like_detail=[]
        inforshare_like_detail=[]
        for i in like_coll["ptos_like"]:
            _ptos=ptos_coll.find_one({"_id":utils.create_objectid(i)})
            ptos_like_detail.append(_ptos)
        for j in like_coll["inforshare_like"]:
            _infoeshare = inforshare_coll.find_one({"_id":utils.create_objectid(j)})
            inforshare_like_detail.append(_infoeshare)

        like_coll=utils.dump(like_coll)
        ptos_like_detail=utils.dump(ptos_like_detail)
        inforshare_like_detail=utils.dump(inforshare_like_detail)
        return like_coll,ptos_like_detail,inforshare_like_detail

    def islike(self,user_id,type,like_id):
        _like = self.coll.find_one({"user_id":user_id})
        if type =="ptos":
            if like_id in _like["ptos_like"]:
                islike ="1"
            else:
                islike = "0"
        if type =="inforshare":
            if like_id in _like["inforshare_like"]:
                islike = "1"
            else:
                islike = "0"
        return islike