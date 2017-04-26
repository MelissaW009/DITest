
# coding:utf-8

import requests
import json

from RestAPITest.DolphinLib import *


'''
def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)
'''


def login_and_get_role(endpoint, username, password):
    uri = build_uri(endpoint)
    request_payload = {"username": "admin", "password": "admin", "rememberMe": False}
    response = requests.post(uri, json=request_payload)
    return ((response.json())["result"])["role"]


def create_user_model(endpoint, namebase, genCnt):
    uri = build_uri(endpoint)
    for i in range(genCnt):
        name = "%s_%s" % (namebase, i)
        request_payload = {"name":name}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        print(response.text)
        if ((response.json())["success"]) == False:
            print("create user model %s failed" % name)


def list_user_model(endpoint, pageIndex, pageSize):
    uri = build_uri(endpoint)
    request_payload = {"sortBy":"","keyword":"","pageIndex":pageIndex,"pageSize":pageSize}
    response = requests.post(uri, headers=HEADERS, json=request_payload)
    return ((response.json())["result"])["list"]


def delete_user_model(endpoint, id):
    uri = build_uri(endpoint)
    request_payload = {"id": id}
    response = requests.post(uri, headers=HEADERS, json=request_payload)
    return (response.json())["success"]

def delete_user_model_list(endpoint,modellist):
    uri = build_uri(endpoint)
    for item in modellist:
        id = item["id"]
        request_payload = {"id": id}
        requests.post(uri, headers=HEADERS, json=request_payload)

def create_model_file(endpoint, modelid, namebase, extendname, path, genCnt):
    uri = build_uri(endpoint)
    for i in range(genCnt):
        name = "%s_%s.%s" % (namebase, i, extendname)
        request_payload = {"id": modelid, "name": name, "path": path, "isFile": True}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        if ((response.json())["success"]) == False:
            print("create user file %s failed" % name)

def delete_model_file(endpoint, modelid, namebase,extendname ,path, genCnt):
    uri = build_uri(endpoint)
    for i in range(genCnt):
        if extendname == "":
            name = "%s_%s" % (namebase, i)
        else:
            name = "%s_%s.%s" % (namebase, i,extendname)
        print(name)
        filepath = path + "/" + name
        request_payload = {"id": modelid, "path": filepath, "isFile": True}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        if ((response.json())["success"]) == False:
            print("create user file %s failed" % name)

def update_model_file(endpoint, modelid, namebase, extendname, path, genCnt):
    uri = build_uri(endpoint)
    for i in range(genCnt):
        if extendname == "":
            name = "%s_%s" % (namebase, i)
        else:
            name = "%s_%s.%s" % (namebase, i,extendname)
        filepath = path + "/" + name
        print(filepath)
        content = "x1=%s\nprint(x1)" % i
        request_payload = {"id": modelid, "path": filepath, "content":content}
        response = requests.post(uri, headers=HEADERS, json=request_payload)
        if ((response.json())["success"]) == False:
            print("update user file %s failed" % name)


if __name__ == '__main__':
    #login_and_get_role("login", "admin", "admin")
    #create_user_model("model/createModel", "信息技术2", 180)
    #modellist = list_user_model("model/listModel", 1,30)
    #delete_user_model_list("model/deleteModel",modellist)
    create_model_file("model/createModelFileOrDir", 6, "rtest", "R","/src", 10)
    create_model_file("model/createModelFileOrDir", 6, "pytest", "py", "/src", 10)
    #update_model_file("fs/updateFile",30,"mytest", "R","/src",20)
    #delete_model_file("/fs/deleteFile", 35, "test_1","", "/src/aaa", 20)



