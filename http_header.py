from mitmproxy import http
from mitmproxy.http import Headers
from typing import List, Dict
import json
import re

def response(flow: http.HTTPFlow):
    assert flow.response
    headers_str = str(flow.response.headers)
    rex = re.finditer(r"Set-cookie", headers_str, re.I)
    if any(rex) :
        print(flow.response.headers)
        
        for m in rex :
            flow.response.headers[m.group()] = flow.response.headers[m.group()].replace("httponly;","")
            flow.response.headers[m.group()] = flow.response.headers[m.group()].replace("HttpOnly;","")
            flow.response.headers[m.group()] = flow.response.headers[m.group()].replace("httponly","")
            flow.response.headers[m.group()] = flow.response.headers[m.group()].replace("HttpOnly","")
            flow.response.headers[m.group()]= flow.response.headers[m.group()].replace(",","\r\nSet-Cookie:")
        print(flow.response.headers)
    
