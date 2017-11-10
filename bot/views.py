import os
import json
import random
import requests

from django.shortcuts import render
from django.http import HttpResponse

config:set DISABLE_COLLECTSTATIC=1
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.getenv("xz/JtdLRqBocv4PpYboi0a0RnXv3vpurJW9ElUuaHPpT8DFAflJK1Fpwc4cy0Unl94BXTdCmVaWYB9g8v8G8hNeci/Kr45J3a9m7kHsbeXYGbmiDQltRp5dsLJj7aNr34uhp/iWf+B+fI4SUvFcd+AdB04t89/1O/w1cDnyilFU=")
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("It works!")

def callback(request_json):
    reply = ""
    request = json.loads(request_json.body.decode('utf-8'))
    for e in request["events"]:
        reply_token = e["replyToken"]
        if e["type"] == "message":
            if e["message"]["type"] == "text":
                reply += e["message"]["text"]
            else:
                reply += "only text message"
            reply_message(reply_token, reply)
    return HttpResponse(reply)

def make_text():
    from . import reply_words
    return random.choice(reply_words)


def reply_message(reply_token, reply):
    reply_body = {
        "replyToken":reply_token,
        "messages":[
            {
                "type":"text",
                "text": reply
            }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(reply_body))
