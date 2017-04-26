# coding:utf-8

import requests
import json

from RestAPITest.DolphinLib import *


def commit_file_histversions(endpoint, modelid, path, genCnt):
    uri = build_uri(endpoint)
    resContent = ""
    for i in range(genCnt):
        content = "print(\"this is test %s\")" % i
        resContent = resContent + "\n" + content
        version = "Commit V%s" % i

        request_payload = {"id": modelid, "path": path, "content": resContent, "commitMsg": version}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        if ((response.json())["success"]) == False:
            print("commit file history version %s failed" % version )


if __name__ == '__main__':
    #commit_file_histversions("fs/commitFile", 3, "/src/testV1.r",25)
    commit_file_histversions("fs/commitFile", 3, "/src/h.py", 1000)
