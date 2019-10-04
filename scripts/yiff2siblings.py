#!/usr/bin/env python3
import json
import sys
import argparse
from urllib.request import urlopen,Request

DEFAULT_URL="https://yiff.party/json/creators.json?_=1570229034607"
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
parser = argparse.ArgumentParser(description='Convert yiff manifest to hydrus siblings',argument_default=None)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-o", "--outfile",help="Path of file to write results",default=None)
group.add_argument("-p", "--print", help="Printto standard out", action="store_true",default=False)
parser.add_argument("url",nargs="?",default=DEFAULT_URL,help="The url/path of the yiff.party manifest")
args=parser.parse_args()

url=args.url
file_out = args.outfile is not None
req = Request(url, headers=hdr)
with urlopen(req) as f:
        d = json.load(f)
        if file_out:
            out = open(args.outfile,'w')

        for u in d["creators"]:
            # yiff id:13538527
            # creator:000
            s="yiff id:%s\r\ncreator:%s" % (u["id"], u["name"])
            if file_out:
                out.write(s)
                out.write('\r\n')
            else:
                print(s)
        if file_out:
            out.close()
