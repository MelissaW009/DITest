# coding:utf-8

import requests
import json

#BASE_URL = "http://d114.mlamp.co:8800/bus"
BASE_URL = "http://localhost:8800/bus"
HEADERS = {
        "Server": "nginx/1.4.3",
        "Cookie": "dolphin_session=1d4d4c363c21ec963ba5613c906bdad4c8bd886d-user=admin&token=e9a5b919a159861bee8a18cfc4cd466c84a55f71",
        "Content-Type": "application/json;charset = UTF-8"
    }

#/model/createModelFileOrDir
def create_model_file(endpoint, namebase, path, genCnt):
    #{"id":34,"name":"a.r","path":"/src","isFile":true,"content":"","_timestamp":1491471657875}
    uri = build_uri(endpoint)
    for i in range(genCnt):
        name = "%s_%s" % (namebase, i)
        request_payload = {"id": 34, "name": name, "path": path, "isFile": True}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        if ((response.json())["success"]) == False:
            print("create user file %s failed" % name)


if __name__ == '__main__':
    create_user_file("model/createModelFileOrDir", "rfiletest","/src", 10)