# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import os
from ZhihuiSMB.libs.utils import *

class FileModel(model.StandCURDModel):
    _coll_name = "file"
    _columns = [
        ("file_name",StrDT()),
        ("file_path",StrDT()),
        ("file_size", StrDT())

    ]



