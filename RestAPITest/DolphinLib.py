# coding:utf-8

import requests

#BASE_URL = "http://d44.mlamp.co:8800/bus"
BASE_URL = "http://localhost:8888/bus"
HEADERS = {
    "Server": "nginx/1.4.3",
    "Cookie": "dolphin_session=1d4d4c363c21ec963ba5613c906bdad4c8bd886d-user=admin&token=e9a5b919a159861bee8a18cfc4cd466c84a55f71",
    "Content-Type": "application/json;charset = UTF-8"
}



def build_uri(endpoint):
    return '/'.join([BASE_URL, endpoint])

