import json
import logging

from django.http import JsonResponse
from django.shortcuts import render
from wxcloudrun.models import Counters


logger = logging.getLogger('log')
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import datasmodel
import gzip
# 解密加密数据，获取用户的手机号码
from Crypto.Cipher import AES
import base64
import re
import uuid
@csrf_exempt
def put_data(request):
    try:
        data = json.loads(request.body)
        # print(data)
        dct = {}
        dct["id"] = data.get("openId")
        dct["nickName"] = data.get("nickName")
        dct["avatarUrl"] = data.get("avatarUrl")
        for item in data.get("datas"):
            # if item.get("questionID") not in ["一","二","三","四"]:
            if item.get("questionType") == 0:
                if item.get("questionID") != "1.7" and item.get("fldAnswer") == 10:
                    u=f'_{str(uuid.uuid3(uuid.NAMESPACE_DNS, item.get("fldName"))).replace("-","_")}'
                    dct[u] = QuestionOptionList[fldAnswer - 1].get(
                        "fldOptionText")
                else:
                    QuestionOptionList = item.get("QuestionOptionList")
                    fldAnswer = item.get("fldAnswer")
                    u=f'_{str(uuid.uuid3(uuid.NAMESPACE_DNS, item.get("fldName"))).replace("-","_")}'
                    dct[u] = QuestionOptionList[fldAnswer - 1].get(
                        "fldOptionText")

            elif item.get("questionType") == 5:
                u=f'_{str(uuid.uuid3(uuid.NAMESPACE_DNS, item.get("fldName"))).replace("-","_")}'
                v=[]
                for i in item.get("QuestionOptionList"):
                    print(item)
                    _=i.get("value") or 0
                    v.append(str(_))
                dct[u] = ";".join(v)

            elif item.get("questionType") == 4:
                u=f'_{str(uuid.uuid3(uuid.NAMESPACE_DNS, item.get("fldName"))).replace("-","_")}'
                dct[u] = item.get("latlng")
            elif item.get("questionType") == 2:
                u=f'_{str(uuid.uuid3(uuid.NAMESPACE_DNS, item.get("fldName"))).replace("-","_")}'
                dct[u] = item.get("fldAnswer")
                # dct["q"] = data.get("openId")
        datasmodel.objects.update_or_create(id=dct.get("id"),defaults=dct)
        print(len(dct), dct)
        return JsonResponse({'status': 1,"message":"成功提交"})
    except:
        return JsonResponse({'status': 0,"message":"提交失败"})

@csrf_exempt
def get_openId(request):
    data = json.loads(request.body)
    # 获取登录凭证和加密数据
    code = data.get('code')
    encrypted_data = data.get('encryptedData')
    iv = data.get('iv')
    # 向微信后台发送请求，获取session_key
    response = requests.get(
        f'https://api.weixin.qq.com/sns/jscode2session?appid=wx27cc81a974a6db02&secret=0265005290ef5da636c77303c30fe091&js_code={code}&grant_type=authorization_code')
    d=response.json()
    session_key = d.get('session_key')
    data['session_key']=session_key
    def decrypt(encrypted_data, session_key, iv):
        session_key = base64.b64decode(session_key)
        encrypted_data = base64.b64decode(encrypted_data)
        iv = base64.b64decode(iv)
        cipher = AES.new(session_key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)
        # 去除解码后的非法字符
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', decrypted_data.decode())
            return json.loads(result)
        except Exception:
             return {}

    decrypted_data=decrypt(encrypted_data, session_key, iv)
    print("decrypted_data",decrypted_data)
    openId = decrypted_data.get('openId')
    # 在这里进行后续的处理，比如保存用户的手机号码到数据库中

    return JsonResponse({'openId': openId})


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return render(request, 'index.html')


def counter(request, _):
    """
    获取当前计数

     `` request `` 请求对象
    """

    rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
    if request.method == 'GET' or request.method == 'get':
        rsp = get_count()
    elif request.method == 'POST' or request.method == 'post':
        rsp = update_count(request)
    else:
        rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
                            json_dumps_params={'ensure_ascii': False})
    logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
    return rsp


def get_count():
    """
    获取当前计数
    """

    try:
        data = Counters.objects.get(id=1)
    except Counters.DoesNotExist:
        return JsonResponse({'code': 0, 'data': 0},
                    json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'code': 0, 'data': data.count},
                        json_dumps_params={'ensure_ascii': False})


def update_count(request):
    """
    更新计数，自增或者清零

    `` request `` 请求对象
    """

    logger.info('update_count req: {}'.format(request.body))

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if 'action' not in body:
        return JsonResponse({'code': -1, 'errorMsg': '缺少action参数'},
                            json_dumps_params={'ensure_ascii': False})

    if body['action'] == 'inc':
        try:
            data = Counters.objects.get(id=1)
        except Counters.DoesNotExist:
            data = Counters()
        data.id = 1
        data.count += 1
        data.save()
        return JsonResponse({'code': 0, "data": data.count},
                    json_dumps_params={'ensure_ascii': False})
    elif body['action'] == 'clear':
        try:
            data = Counters.objects.get(id=1)
            data.delete()
        except Counters.DoesNotExist:
            logger.info('record not exist')
        return JsonResponse({'code': 0, 'data': 0},
                    json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'code': -1, 'errorMsg': 'action参数错误'},
                    json_dumps_params={'ensure_ascii': False})
