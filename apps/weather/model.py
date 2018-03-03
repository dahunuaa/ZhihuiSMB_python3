# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.libs.utils as utils

class WeatherModel(model.StandCURDModel):
    _coll_name ="weather"
    _columns=[]

    def city2mongo(self,citycode):
        for i in citycode:
            self.coll.insert({
                "code":i[0],
                "name":i[1]
            })

    def getcodefromname(self,cityname):
        result = self.coll.find_one({"name":cityname})
        return utils.dump(result)