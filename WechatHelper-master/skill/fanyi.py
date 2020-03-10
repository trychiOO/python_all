import json
from ask_sdk_core.response_helper import get_text_content
from ask_sdk_model.interfaces.display import (
    RenderTemplateDirective,
    BodyTemplate1)
from python_skill_adpater import pythonSkillAdpater
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
from imp import reload
from azero_log.azero_logger import logger
#import logging
#logger = logging.getLogger(__name__)
import time

reload(sys)

sb = SkillBuilder()

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '21b5ab24d57492c8'
APP_SECRET = '7eCRxI2DQd669claPuge1QCp653KX7cy'


# 返回方法
def build_rsp_with_speech(handler_input, speech):
    return handler_input.response_builder.speak(speech).response


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(original, trance_src, trance_des, handler_input):
    data = {}
    data['from'] = trance_src
    data['to'] = trance_des
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(original) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = original
    data['salt'] = salt
    data['sign'] = sign
    logger.info('有道请求数据：' + json.dumps(data), handler_input.request_envelope)
    response = do_request(data)
    logger.info('有道响应数据：' + str(response.content), handler_input.request_envelope)
    return json.loads(str(response.content, 'utf-8'))

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""


class CompletedDelegateHandler_Translation(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("Translation")(handler_input) and
                ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')

    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        original = ask_utils.get_slot(handler_input, "original")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
            handler_input.response_builder
                .speak(speakOutput)
                .set_should_end_session(True)
                .response
        )


"""
用户取消和退出或者错误退出时的Handle
"""


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.speak('已退出当前意图').set_should_end_session(True).response


class IntentRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # 获取翻译内容：
        original = ask_utils.get_slot_value(handler_input, 'original')
        logger.info('获取翻译内容：' + str(original), handler_input.request_envelope)
        if len(original) == 0:
            return build_rsp_with_speech(handler_input, '抱歉，请说出翻译内容')
        # 获取翻译源语言：
        trance_src = ask_utils.get_slot_value(handler_input, 'tranceSrc')
        logger.info('获取翻译源语言：' + str(trance_src), handler_input.request_envelope)
        # 获取翻译目标语言：
        trance_des = ask_utils.get_slot_value(handler_input, 'tranceDes')
        logger.info('获取翻译目标语言：' + str(trance_des), handler_input.request_envelope)
        # 调用翻译API：
        if trance_src == 'English':
            trance_src = 'en'
        elif trance_src == 'Chinese':
            trance_src = 'zh-CHS'
        else:
            trance_src = 'auto'

        if trance_des == 'English':
            trance_des = 'en'
        elif trance_des == 'Chinese':
            trance_des = 'zh-CHS'
        else:
            trance_des = 'auto'
        logger.info('准备请求API，翻译内容：【' + original + '】，源语言：【' + trance_src + '】，目标语言：【' + trance_des + '】', handler_input.request_envelope)
        result = connect(original.capitalize(), trance_src, trance_des, handler_input)

        speak_output = result.get('translation')[0]
        if len(speak_output) == 0:
            return build_rsp_with_speech(handler_input, '抱歉，暂未查询到结果')
        return (
            handler_input.response_builder.add_directive(
                RenderTemplateDirective(
                    BodyTemplate1(
                        title=speak_output,
                        text_content=get_text_content(primary_text=speak_output))))
                .speak(speak_output)
                .set_should_end_session(True)
                .response
        )


def invoke_skill(app):
    sb.add_request_handler(SessionEndedRequestHandler())
    sb.add_request_handler(IntentRequestHandler())
    skill_adapter = pythonSkillAdpater(skill=sb.create(), skill_id='5e4a82c1ac159c00083113d3', app=app)
    result = skill_adapter.dispatch_request()
    return result