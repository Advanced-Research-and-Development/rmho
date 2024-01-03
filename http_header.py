from mitmproxy import http
from mitmproxy.http import Headers

def response(flow: http.HTTPFlow):
    assert flow.response
    cookies = flow.response.cookies
    if "Set-Cookie" in flow.response.headers:
        flow.response.headers["Set-Cookie"]= flow.response.headers["Set-Cookie"].replace("HttpOnly;","")
        #print("HTTP : " ,flow.response.headers["Set-Cookie"])
