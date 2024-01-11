from mitmproxy import http
import re

def remove_httponly(input_string):
    pattern = re.compile(r'httponly;?', flags=re.IGNORECASE)
    return pattern.sub('', input_string)

def split_cookies(cookie_string):
    # 正則表達式匹配 cookie 名稱=值的模式，並允許後續的屬性（如 expires、path 等）
    cookie_pattern = re.compile(r'(?<=,)\s*(?=\w+=[^;]+(;|$))')
    return cookie_pattern.split(cookie_string)

def valid_cookie(cookie_str):
    return cookie_str.strip() != '' and '=' in cookie_str

def response(flow: http.HTTPFlow):
    assert flow.response
    header_list = []
    print(flow.response.headers)

    for key, value in flow.response.headers.items():
        if key.lower() == 'set-cookie':
            cookies = split_cookies(remove_httponly(value))
            for cookie in cookies:
                if valid_cookie(cookie):
                    header_list.append((b'Set-Cookie', bytes(cookie.strip(), 'utf-8')))
        else:
            header_list.append((bytes(key, 'utf-8'), bytes(value, 'utf-8')))

    flow.response.headers = http.Headers(header_list)
    print(flow.response.headers)
