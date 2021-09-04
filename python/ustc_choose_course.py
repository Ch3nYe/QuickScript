# -*- encoding:"utf-8"-*-
#!/usr/bin/python3

import os
import json
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s| %(levelname)s| %(message)s')

REQUEST_INTERVAL = 5 # 请求间隔
ADD_OR_DROP = True # True:ADD False:Drop
CURL_KEEP_QUITE = " -s"
# make sure that time of courses is unconflict !!!
# web-browser f12 network select-request-item rightclick copy-curl || then you can get following string
add_req_cmd = '''curl "https://jw.ustc.edu.cn/ws/for-std/course-select/add-request" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://jw.ustc.edu.cn" -H "Connection: keep-alive" -H "Referer: https://jw.ustc.edu.cn/for-std/course-select/123456/turn/481/select" -H "Cookie: sduuid=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; SESSION=aaaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaa; SVRNAME=student2" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" --data-raw "studentAssoc=123456&lessonAssoc=136153&courseSelectTurnAssoc=481&scheduleGroupAssoc=&virtualCost=0"''' + CURL_KEEP_QUITE
add_confirm_cmd = '''curl "https://jw.ustc.edu.cn/ws/for-std/course-select/add-drop-response" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://jw.ustc.edu.cn" -H "Connection: keep-alive" -H "Referer: https://jw.ustc.edu.cn/for-std/course-select/123456/turn/481/select" -H "Cookie: sduuid=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; SESSION=aaaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaa; SVRNAME=student2" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" --data-raw "studentId=123456&requestId={}"''' + CURL_KEEP_QUITE


drop_req_cmd = '''curl "https://jw.ustc.edu.cn/ws/for-std/course-select/drop-request" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://jw.ustc.edu.cn" -H "Connection: keep-alive" -H "Referer: https://jw.ustc.edu.cn/for-std/course-select/123456/turn/481/select" -H "Cookie: sduuid=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; SESSION=aaaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaa; SVRNAME=student2" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" --data-raw "studentAssoc=123456&lessonAssoc=136771&courseSelectTurnAssoc=481"''' + CURL_KEEP_QUITE
drop_confirm_cmd = '''curl "https://jw.ustc.edu.cn/ws/for-std/course-select/add-drop-response" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://jw.ustc.edu.cn" -H "Connection: keep-alive" -H "Referer: https://jw.ustc.edu.cn/for-std/course-select/123456/turn/481/select" -H "Cookie: sduuid=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; SESSION=aaaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaa; SVRNAME=student2" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" --data-raw "studentId=123456&requestId={}"''' + CURL_KEEP_QUITE


if ADD_OR_DROP:
    logging.debug("[+]adding course routine!")
    while True:
        logging.debug("[-]try request token...")
        out = os.popen(add_req_cmd)
        token = out.read()
        logging.debug("[-]try send token {}...".format(token))
        add_confirm_cmd_complete = add_confirm_cmd.format(token)
        out = os.popen(add_confirm_cmd_complete)
        result = out.read()
        result = json.loads(result)
        if not result:
            logging.debug("[-]operation result: send token request return null!")
            break
        if result['success']:
            logging.debug("[+]operation result: {}".format(result['success']))
            break
        logging.debug("[-]operation response: {}".format(result))
        time.sleep(REQUEST_INTERVAL)

else:
    logging.debug("[+]dropping course routine!")
    logging.debug("[-]try request token...")
    out = os.popen(drop_req_cmd)
    token = out.read()
    logging.debug("[-]try send token {}...".format(token))
    add_confirm_cmd_complete = drop_confirm_cmd.format(token)
    out = os.popen(add_confirm_cmd_complete)
    result = out.read()
    result = json.loads(result)
    if result['success']:
        logging.debug("[+]operation result: {}".format(result['success']))
    else:
        logging.debug("[-]operation result: {}".format(result['success']))
        logging.debug("[-]operation response: {}".format(result))
