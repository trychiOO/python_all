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
"""
class CompletedDelegateHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("BookTrainTicket")(handler_input) and
                ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
 
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date = ask_utils.get_slot(handler_input, "date")
        fromCity = ask_utils.get_slot(handler_input, "fromCity")
        toCity = ask_utils.get_slot(handler_input, "toCity")
        speak_output = "已为您购买" + date.value+fromCity.value+"到"+toCity.value+"的火车票"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)
                .response
        )
 
"""
Dialog委托场景COMPLETED完成之后Skill完成当前意图并转到新意图 Handle
"""
class CompletedDelegateUpdateIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("BookTrainTicket")(handler_input) and
                ask_utils.get_dialog_state(handler_input).value == 'COMPLETED')
 
    def handle(self, handler_input):
        date = ask_utils.get_slot(handler_input, "date")
        fromCity = ask_utils.get_slot(handler_input, "fromCity")
        toCity = ask_utils.get_slot(handler_input, "toCity")
        speak_output = "已为您购买" + date.value+fromCity.value+"到"+toCity.value+"的火车票"
        anotherIntent = {
            'name': "BookHotel",
            'slots': {
                'date': date,
                'toCity': toCity,
            },
            'confirmation_status':'NONE'
        }
        return (
            handler_input.response_builder.add_directive(
                    DelegateDirective(anotherIntent)
                )
                .speak(speak_output)
                .set_should_end_session(False)
                .response
        )
 
"""
全手动委托唤醒Dialog当前意图 Handle
"""
class ManualDelegateHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("BookTrainTicket")(handler_input) and
                (ask_utils.get_dialog_state(handler_input).value == 'STARTED' or
                 ask_utils.get_dialog_state(handler_input).value == 'IN_PROGRESS'))
 
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        return (
            handler_input.response_builder.add_directive(
                    DelegateDirective(currentIntent)
                )
                .response
        )
 
"""
全部由skill code控制Dialog的澄清话术，验证槽位，确定槽位和确定意图等 Handle
"""
class SkillCodeControlDelegateHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("BookTrainTicket")(handler_input) and
                (ask_utils.get_dialog_state(handler_input).value == 'STARTED' or
                 ask_utils.get_dialog_state(handler_input).value == 'IN_PROGRESS'))
 
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        date = ask_utils.get_slot(handler_input, "date")
        fromCity = ask_utils.get_slot(handler_input, "fromCity")
        toCity = ask_utils.get_slot(handler_input, "toCity")
        if (fromCity.value == '' or fromCity.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("fromCity", currentIntent))
            handler_input.response_builder.speak("从哪个城市出发？")
        elif(fromCity.confirmation_status.value != 'CONFIRMED'):
            handler_input.response_builder.add_directive(ConfirmSlotDirective("fromCity", currentIntent))
            handler_input.response_builder.speak("确定从"+fromCity.value+"出发吗？")
        elif(date.value == '' or date.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("date", currentIntent))
            handler_input.response_builder.speak("需要哪一天的？")
        elif(toCity.value == '' or toCity.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("toCity", currentIntent))
            handler_input.response_builder.speak("到哪一个城市？")
        elif(currentIntent.confirmation_status != 'CONFIRMED'):
            handler_input.response_builder.add_directive(ConfirmIntentDirective(currentIntent))
            handler_input.response_builder.speak("确定购买" + date.value+fromCity.value+"到"+toCity.value+"的火车票吗？")
 
        return handler_input.response_builder.response
 
"""
非自动委托Dialog的澄清话术，验证槽位，确定槽位和确定意图等部分由Skill控制部分由网站上配置手动委托给Azero DM去追问
"""
class CombineDialogDelegateHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_request_type("IntentRequest")(handler_input) and
                ask_utils.is_intent_name("BookTrainTicket")(handler_input) and
                (ask_utils.get_dialog_state(handler_input).value == 'STARTED' or
                 ask_utils.get_dialog_state(handler_input).value == 'IN_PROGRESS'))
 
    def handle(self, handler_input):
        currentIntent = handler_input.request_envelope.request.intent
        date = ask_utils.get_slot(handler_input, "date")
        fromCity = ask_utils.get_slot(handler_input, "fromCity")
        toCity = ask_utils.get_slot(handler_input, "toCity")
        if (fromCity.value == '' or fromCity.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("fromCity", currentIntent))
            handler_input.response_builder.speak("从哪个城市出发？")
        elif(fromCity.confirmation_status.value != 'CONFIRMED'):
            handler_input.response_builder.add_directive(ConfirmSlotDirective("fromCity", currentIntent))
            handler_input.response_builder.speak("确定从"+fromCity.value+"出发吗？")
        elif(date.value == '' or date.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("date", currentIntent))
            handler_input.response_builder.speak("需要哪一天的？")
        elif(toCity.value == '' or toCity.confirmation_status.value == 'DENIED'):
            handler_input.response_builder.add_directive(ElicitSlotDirective("toCity", currentIntent))
            handler_input.response_builder.speak("到哪一个城市？")
        elif(toCity.confirmation_status.value != 'CONFIRMED'):
            handler_input.response_builder.add_directive(DelegateDirective(currentIntent))
        elif(currentIntent.confirmation_status != 'CONFIRMED'):
            handler_input.response_builder.add_directive(ConfirmIntentDirective(currentIntent))
            handler_input.response_builder.speak("确定购买" + date.value+fromCity.value+"到"+toCity.value+"的火车票吗？")
        else:
            handler_input.response_builder.add_directive(DelegateDirective(currentIntent))
        return handler_input.response_builder.response
 
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
 
        return handler_input.response_builder.response
 
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
    sb.add_request_handler(CombineDialogDelegateHandler())
    sb.add_request_handler(SkillCodeControlDelegateHandler())
    sb.add_request_handler(ManualDelegateHandler())
    sb.add_request_handler(CompletedDelegateUpdateIntentHandler())
    sb.add_request_handler(CompletedDelegateHandler())
    sb.add_request_handler(SessionEndedRequestHandler())
    sb.add_request_handler(IntentRequestHandler())
    skill_adapter = pythonSkillAdpater(skill=sb.create(), skill_id='5db14b013dff9557bc772e9f', app = app)
    result = skill_adapter.dispatch_request()
    return result