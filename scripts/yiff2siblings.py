#!/usr/bin/env python3 
import json
import sys
with open(sys.argv[1]) as f:
    d= json.load(f)
    for u in d["creators"]:
        #yiff id:13538527
        #creator:000
        print("yiff id:%s\r\ncreator:%s"%(u["id"],u["name"]))