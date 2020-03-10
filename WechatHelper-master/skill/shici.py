import json
import logging

from ask_sdk_core.response_helper import get_text_content
from ask_sdk_model.interfaces.display import (
    RenderTemplateDirective,
    BodyTemplate1)
from flask import request
from ask_sdk_model.directive import *
from ask_sdk_model.dialog import *
from python_skill_adpater import pythonSkillAdpater
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_ReadThePoems(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("ReadThePoems")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        poemtitle = ask_utils.get_slot(handler_input, "poemtitle")   #古诗名
        poemauthor = ask_utils.get_slot(handler_input, "poemauthor")  #// 作者


        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_ReadTheSongPoems(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("ReadTheSongPoems")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        songpoemtitle = ask_utils.get_slot(handler_input, "songpoemtitle")
        tunename = ask_utils.get_slot(handler_input, "tunename")
        songpoemtitleauthor = ask_utils.get_slot(handler_input, "songpoemtitleauthor")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchThePoems_Previous(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchThePoems_Previous")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        verse = ask_utils.get_slot(handler_input, "verse")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchThePoems_Next(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchThePoems_Next")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        verse = ask_utils.get_slot(handler_input, "verse")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchPoemsName(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchPoemsName")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        verse = ask_utils.get_slot(handler_input, "verse")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchPoemsDynasty(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchPoemsDynasty")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        poemtitle = ask_utils.get_slot(handler_input, "poemtitle")
        songpoemtitle = ask_utils.get_slot(handler_input, "songpoemtitle")
        tunename = ask_utils.get_slot(handler_input, "tunename")
        verse = ask_utils.get_slot(handler_input, "verse")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchThePoems_Order(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchThePoems_Order")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        poemtitle = ask_utils.get_slot(handler_input, "poemtitle")
        number = ask_utils.get_slot(handler_input, "number")
        songpoemtitle = ask_utils.get_slot(handler_input, "songpoemtitle")
        tunename = ask_utils.get_slot(handler_input, "tunename")
        verse = ask_utils.get_slot(handler_input, "verse")
        speakOutput = '欢迎使用技能,您可根据当前意图和槽位返回您想回复的话术';
        return (
        	handler_input.response_builder
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_SearchPoemsAuthor(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("SearchPoemsAuthor")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        poemtitle = ask_utils.get_slot(handler_input, "poemtitle")
        songpoemtitle = ask_utils.get_slot(handler_input, "songpoemtitle")
        tunename = ask_utils.get_slot(handler_input, "tunename")
        verse = ask_utils.get_slot(handler_input, "verse")
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
        speak_output='欢迎使用技能'
        poemtitle = ask_utils.get_slot_value(handler_input, 'original')
        logger.info('获取内容：' + str(poemtitle), handler_input.request_envelope)
        if len(poemtitle) == 0:
            return build_rsp_with_speech(handler_input, '抱歉，哪首诗')
        # 获取翻译源语言：
        trance_src = ask_utils.get_slot_value(handler_input, 'tranceSrc')
        logger.info('获取翻译源语言：' + str(trance_src), handler_input.request_envelope)
        # 获取翻译目标语言：
        trance_des = ask_utils.get_slot_value(handler_input, 'tranceDes')
        logger.info('获取翻译目标语言：' + str(trance_des), handler_input.request_envelope)


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
    sb.add_request_handler(CompletedDelegateHandler_ReadThePoems())
    sb.add_request_handler(CompletedDelegateHandler_ReadTheSongPoems())
    sb.add_request_handler(CompletedDelegateHandler_SearchThePoems_Previous())
    sb.add_request_handler(CompletedDelegateHandler_SearchThePoems_Next())
    sb.add_request_handler(CompletedDelegateHandler_SearchPoemsName())
    sb.add_request_handler(CompletedDelegateHandler_SearchPoemsDynasty())
    sb.add_request_handler(CompletedDelegateHandler_SearchThePoems_Order())
    sb.add_request_handler(CompletedDelegateHandler_SearchPoemsAuthor())

    sb.add_request_handler(SessionEndedRequestHandler())
    sb.add_request_handler(IntentRequestHandler())
    skill_adapter = pythonSkillAdpater(skill=sb.create(), skill_id='5e54bdd9d71ea7000845789c', app = app)
    result = skill_adapter.dispatch_request()
    return result