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
class CompletedDelegateHandler_cancel_search(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("cancel_search")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        stop = ask_utils.get_slot(handler_input, "stop")
        speakOutput = '好的，为您退出';
        title_text = '找手机'
        return (
        	handler_input.response_builder.add_directive(
             RenderTemplateDirective(
              BodyTemplate1(
              title=title_text,
              text_content=get_text_content(primary_text=speakOutput))))
        		.speak(speakOutput)
        		.set_should_end_session(True)
        		.response
        )

"""
非自动委托Dialog的澄清话术，验证槽位，确定槽位和确定意图等部分由Skill控制
部分由网站上配置手动委托给Azero DM去追问
"""
class CombineDialogDelegateHandler_cancel_search(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("cancel_search")(handler_input) and
               (ask_utils.get_dialog_state(handler_input).value == 'STARTED' or
               ask_utils.get_dialog_state(handler_input).value == 'IN_PROGRESS'))
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        stop = ask_utils.get_slot(handler_input, "stop")
        speakOutput = '您可根据判断意图或者所有槽位返回您想回复的话术和模版'
#        handler_input.response_builder.add_directive(ElicitSlotDirective("槽位名称", currentIntent))
#        handler_input.response_builder.add_directive(ConfirmSlotDirective("槽位名称", currentIntent))
#        handler_input.response_builder.add_directive(DelegateDirective(currentIntent))
#        handler_input.response_builder.add_directive(ConfirmIntentDirective(currentIntent))
        return (
        	handler_input.response_builder
        		.add_directive(DelegateDirective(currentIntent))
        		.speak(speakOutput)
        		.set_should_end_session(False)
        		.response
        )

"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图 Handle
若完成当前意图后希望转到新意图set_should_end_session需设为false，且需返回Dialog的Directive
"""
class CompletedDelegateHandler_search(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("search")(handler_input) and
               ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        find = ask_utils.get_slot(handler_input, "find")
        speakOutput = '好的 为您查找';
        command='查找'
        title_text = '找手机'
        return (
            handler_input.response_builder
                .add_directive(
                RenderTemplateDirective(
                    BodyTemplate1(
                        title=title_text,
                        text_content=get_text_content(primary_text=command))))
                .speak(speakOutput)
                .set_should_end_session(True)
                .response
        )


"""
非自动委托Dialog的澄清话术，验证槽位，确定槽位和确定意图等部分由Skill控制
部分由网站上配置手动委托给Azero DM去追问
"""
class CombineDialogDelegateHandler_search(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
               ask_utils.is_intent_name("search")(handler_input) and
               (ask_utils.get_dialog_state(handler_input).value == 'STARTED' or
               ask_utils.get_dialog_state(handler_input).value == 'IN_PROGRESS'))
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        find = ask_utils.get_slot(handler_input, "find")
        speakOutput = '您可根据判断意图或者所有槽位返回您想回复的话术和模版'
#        handler_input.response_builder.add_directive(ElicitSlotDirective("槽位名称", currentIntent))
#        handler_input.response_builder.add_directive(ConfirmSlotDirective("槽位名称", currentIntent))
#        handler_input.response_builder.add_directive(DelegateDirective(currentIntent))
#        handler_input.response_builder.add_directive(ConfirmIntentDirective(currentIntent))
        return (
        	handler_input.response_builder
        		.add_directive(DelegateDirective(currentIntent))
        		.speak(speakOutput)
        		.set_should_end_session(False)
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
    sb.add_request_handler(CompletedDelegateHandler_cancel_search())
    sb.add_request_handler(CombineDialogDelegateHandler_cancel_search())
    sb.add_request_handler(CompletedDelegateHandler_search())
    sb.add_request_handler(CombineDialogDelegateHandler_search())

    sb.add_request_handler(SessionEndedRequestHandler())
    sb.add_request_handler(IntentRequestHandler())
    skill_adapter = pythonSkillAdpater(skill=sb.create(), skill_id='5e54978e334b730008bb782a', app = app)
    result = skill_adapter.dispatch_request()
    return result