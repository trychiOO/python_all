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
import requests
from imp import reload
from azero_log.azero_logger import logger
#import logging
#logger = logging.getLogger(__name__)
reload(sys)

sb = SkillBuilder()

baseUrl = 'https://api.tratao.com/xcurrency/v1/convert'
AppKey = '03A73304fC7311e8A5631b43E8e6422c'
Authorization = 'MDNBNzMzMDRmQzczMTFlOEE1NjMxYjQzRThlNjQyMmMzYTYxOTRkZS1mYzczLTExZTgtYjk5Yy1mNzU3NzRmNDNiNjE='


# 返回方法
def build_rsp_with_speech(handler_input, speech):
    return handler_input.response_builder.speak(speech).response


def connect(original_currency, target_currency, handler_input):
    params = {'from': original_currency, 'to': target_currency}
    headers = {'AppKey': AppKey, 'Authorization': Authorization}
    response = requests.get(url=baseUrl, params=params, headers=headers)
    logger.info('极简汇率response：' + str(response.content), handler_input.request_envelope)
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
        # 源货币种类：
        original_currency = ask_utils.get_slot_value(handler_input, 'originalCurrency')
        if len(original_currency) == 0:
            return build_rsp_with_speech(handler_input, '请说出想要转换的货币种类')
        logger.info('源货币种类：' + original_currency, handler_input.request_envelope)
        # 目标货币种类：
        target_currency = ask_utils.get_slot_value(handler_input, 'targetCurrency')
        if target_currency is None:
            target_currency = 'CNY'
        logger.info('目标货币种类：' + target_currency, handler_input.request_envelope)
        # 源货币数量：
        original_currency_quantity = ask_utils.get_slot_value(handler_input, 'originalCurrencyQuantity')
        logger.info('源货币数量：' + str(original_currency_quantity), handler_input.request_envelope)
        # 调用极简汇率API：
        result = connect(original_currency, target_currency, handler_input)

        mid = result.get('to')[0].get('mid')
        if original_currency_quantity is not None:
            speak_output = str('%.3f' % (mid * float(original_currency_quantity)))
        else:
            speak_output = str('%.3f' % mid)
        if len(speak_output) == 0:
            return build_rsp_with_speech(handler_input, '抱歉，暂未查询到结果')
        return (
            handler_input.response_builder.add_directive(
                RenderTemplateDirective(
                    BodyTemplate1(
                        title=str(speak_output),
                        text_content=get_text_content(primary_text=speak_output))))
                .speak(speak_output)
                .set_should_end_session(True)
                .response
        )


def invoke_skill(app):
    sb.add_request_handler(SessionEndedRequestHandler())
    sb.add_request_handler(IntentRequestHandler())
    skill_adapter = pythonSkillAdpater(skill=sb.create(), skill_id='5e4d34656aa8810008b89274', app=app)
    result = skill_adapter.dispatch_request()
    return result