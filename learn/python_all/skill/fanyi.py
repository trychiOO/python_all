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


# ���ط���
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
    logger.info('�е��������ݣ�' + json.dumps(data), handler_input.request_envelope)
    response = do_request(data)
    logger.info('�е���Ӧ���ݣ�' + str(response.content), handler_input.request_envelope)
    return json.loads(str(response.content, 'utf-8'))

"""
Dialogί�г���COMPLETED���֮��Skill��ɵ�ǰ��ͼ Handle
����ɵ�ǰ��ͼ��ϣ��ת������ͼset_should_end_session����Ϊfalse�����践��Dialog��Directive
"""


class CompletedDelegateHandler_Translation(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("Translation")(handler_input) and
                ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')

    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        original = ask_utils.get_slot(handler_input, "original")
        speakOutput = '��ӭʹ�ü���,���ɸ��ݵ�ǰ��ͼ�Ͳ�λ��������ظ��Ļ���';
        return (
            handler_input.response_builder
                .speak(speakOutput)
                .set_should_end_session(True)
                .response
        )


"""
�û�ȡ�����˳����ߴ����˳�ʱ��Handle
"""


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.speak('���˳���ǰ��ͼ').set_should_end_session(True).response


class IntentRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # ��ȡ�������ݣ�
        original = ask_utils.get_slot_value(handler_input, 'original')
        logger.info('��ȡ�������ݣ�' + str(original), handler_input.request_envelope)
        if len(original) == 0:
            return build_rsp_with_speech(handler_input, '��Ǹ����˵����������')
        # ��ȡ����Դ���ԣ�
        trance_src = ask_utils.get_slot_value(handler_input, 'tranceSrc')
        logger.info('��ȡ����Դ���ԣ�' + str(trance_src), handler_input.request_envelope)
        # ��ȡ����Ŀ�����ԣ�
        trance_des = ask_utils.get_slot_value(handler_input, 'tranceDes')
        logger.info('��ȡ����Ŀ�����ԣ�' + str(trance_des), handler_input.request_envelope)
        # ���÷���API��
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
        logger.info('׼������API���������ݣ���' + original + '����Դ���ԣ���' + trance_src + '����Ŀ�����ԣ���' + trance_des + '��', handler_input.request_envelope)
        result = connect(original.capitalize(), trance_src, trance_des, handler_input)

        speak_output = result.get('translation')[0]
        if len(speak_output) == 0:
            return build_rsp_with_speech(handler_input, '��Ǹ����δ��ѯ�����')
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