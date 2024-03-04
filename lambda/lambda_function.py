# -*- coding: utf-8 -*-
# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.

import logging

#just added
import os
import boto3
from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_dynamodb.adapter import DynamoDbAdapter

ddb_region = os.environ.get('DYNAMODB_PERSISTENCE_REGION')
ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')

ddb_resource = boto3.resource('dynamodb', region_name=ddb_region)
dynamodb_adapter = DynamoDbAdapter(table_name=ddb_table_name, create_table=False, dynamodb_resource=ddb_resource)
sb = CustomSkillBuilder(persistence_adapter = dynamodb_adapter)

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

globalScoreTeamOne = 0
globalScoreTeamtwo = 0
globalCounter=0
globalCounter2=0
lastourbid = 0 
lasttheirbid = 0
name_one = "none"
name_two  = "none"
name_three  = "none"
name_four  = "none"

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        global lastourbid
        global lasttheirbid
        global name_one  
        global name_two  
        global name_three  
        global name_four  
        globalScoreTeamOne = 0
        globalScoreTeamtwo = 0
        lastourbid = 0 
        lasttheirbid = 0
        name_one = "none"
        name_two  = "none"
        name_three  = "none"
        name_four  = "none"
        speak_output = "Welcome to premium spades, Who's playing?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )



class createGroupsIntentHandler(AbstractRequestHandler):
    """Handler for createGroupsIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("createGroups")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        global lastourbid
        global lasttheirbid
        global name_one  
        global name_two  
        global name_three  
        global name_four  
        globalScoreTeamOne = 0
        globalScoreTeamtwo = 0
        lastourbid = 0 
        lasttheirbid = 0
        name_one = "none"
        name_two  = "none"
        name_three  = "none"
        name_four  = "none"
        slots = handler_input.request_envelope.request.intent.slots 
        name_one = slots['NameOne'].value
        name_two = slots['NameTwo'].value
        name_three = slots['NameThree'].value
        name_four = slots['NameFour'].value
        logging.info(name_one)
        attr = handler_input.attributes_manager.persistent_attributes
        attr[str(name_one) + str(name_two) +'Score']=0
        attr[str(name_three) + str(name_four) +'Score']=0
        attr[str(name_one) + str(name_two) +'Present']=0
        attr[str(name_three) + str(name_four) +'Present']=0
        attr['logic']=0
        attr['logic2']=0
        attr['Hand']=1
        attr['negativeone']=0
        attr['negativetwo']=0
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        speak_output = "Ok. " + name_one + " and " + name_two + " are Team 1 and " + name_three + " and " + name_four + " are Team 2, " + " what is your first bid?"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class ourTeamIntentHandler(AbstractRequestHandler):
    """Handler for ourTeamIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ourTeam")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global lastourbid 
        global name_one  
        global name_two
        global globalCounter
        slots = handler_input.request_envelope.request.intent.slots 
        num_one = slots['number'].value
        logging.info(num_one)
        lastourbid = int(num_one) * 10 
        globalScoreTeamOne = int(num_one) * 10 
        logging.info(globalScoreTeamOne)
        if(globalScoreTeamOne<=130 and globalScoreTeamOne != 0):
            attr = handler_input.attributes_manager.persistent_attributes
            #attr[str(name_one) + str(name_two) +'Score']+= globalScoreTeamOne
            attr[str(name_one) + str(name_two) +'Present']= globalScoreTeamOne
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
            if(attr['logic']==0):
                speak_output = str(name_one) + " and " + str(name_two) + " bids " + str(globalScoreTeamOne)+". Whats Team two's bid?"
                attr = handler_input.attributes_manager.persistent_attributes
                attr['logic']=1
                handler_input.attributes_manager.session_attributes = attr
                handler_input.attributes_manager.save_persistent_attributes()
            else:
                speak_output= "ok. i have team one bid of "+str(attr[str(name_one) + str(name_two) +'Present']) +" and team two bid of "+str(attr[str(name_three) + str(name_four) +'Present'])+". lets play the  hand "+str(attr['Hand'])
        else:
            speak_output = str(name_one) + " and " + str(name_two) + " bids must be less than 13 at a time!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class oppenentTeamIntentHandler(AbstractRequestHandler):
    """Handler for oppenentTeamIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("oppenentTeam")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOnes
        global globalScoreTeamtwo
        global lasttheirbid
        global name_one  
        global name_two
        global name_three  
        global name_four  
        global globalCounter2
        slots = handler_input.request_envelope.request.intent.slots 
        name_ones = slots['number'].value
        logging.info(name_one)
        lasttheirbid = int(name_ones) * 10 
        globalScoreTeamtwo = int(name_ones) * 10 
        logging.info(globalScoreTeamtwo)
        if(globalScoreTeamtwo<=130):
            attr = handler_input.attributes_manager.persistent_attributes
            #attr[str(name_three) + str(name_four) +'Score']+= globalScoreTeamtwo
            attr[str(name_three) + str(name_four) +'Present']= globalScoreTeamtwo
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
            globalScoreTeamOnes = int(attr['logic'])
            #speak_output = speak_output = str(name_three) + " and " + str(name_four) + " bids " + str(globalScoreTeamtwo)+" Whats your next bid?"
            if(globalScoreTeamOnes ==0):
                speak_output= str(name_three) + " and " + str(name_four) + " bids " + str(globalScoreTeamtwo)+". Whats Team one's bid?"
                attr = handler_input.attributes_manager.persistent_attributes
                attr['logic']=1
                handler_input.attributes_manager.session_attributes = attr
                handler_input.attributes_manager.save_persistent_attributes()
            else:
                speak_output= "ok. i have team one bid of "+str(attr[str(name_one) + str(name_two) +'Present']) +" and team two bid of "+str(attr[str(name_three) + str(name_four) +'Present'])+". lets play the  hand "+str(attr['Hand'])
                
        else:
            speak_output = str(name_three) + " and " + str(name_four) + " bids must be less than 13 at a time!"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class oppenentTeamFirstIntentHandler(AbstractRequestHandler):
    """Handler for oppenentTeamIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("opponentTeamFirsts")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        global lasttheirbid
        global name_one  
        global name_two
        global name_three  
        global name_four  
        global globalCounter2
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        #speak_output = speak_output = str(name_three) + " and " + str(name_four) + " bids " + str(globalScoreTeamtwo)+" Whats your next bid?"
        speak_output= "ok. i have team one bid of "+str(attr[str(name_one) + str(name_two) +'Present']) +" and team two bid of "+str(attr[str(name_three) + str(name_four) +'Present'])+". lets play the  hand "+str(attr['Hand'])
            
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )



class ourMadeIntentHandler(AbstractRequestHandler):
    """Handler for ourMadeIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ourMade")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        global lasttheirbid
        #global name_three  
        #global name_four  
        global globalCounter2
        slots = handler_input.request_envelope.request.intent.slots 
        name_ones = slots['number'].value
        logging.info(name_one)
        lasttheirbid = int(name_ones) * 10 
        globalScoreTeamtwo = int(name_ones) * 10 
        logging.info(globalScoreTeamtwo)
        attr = handler_input.attributes_manager.persistent_attributes
        attr[str(name_one) + str(name_two) +'Present']=globalScoreTeamtwo
        attr['logic']=0
        attr[str(name_one) + str(name_two) +'Score']+= attr[str(name_one) + str(name_two) +'Present']
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        if(attr["logic2"]==0):
            speak_output = "OK. Team 1 now has " + str(attr[str(name_one) + str(name_two) + 'Score']) + ". And what about Team 2?"
            attr = handler_input.attributes_manager.persistent_attributes
            attr['logic2']=1
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
        else:
            attr = handler_input.attributes_manager.persistent_attributes
            attr['Hand']+=1
            attr['logic2']=0
            attr['negativeone']=0
            attr['negativetwo']=0
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
            speak_output= "Ok. Team 1 Now has  "+ str(attr[str(name_one) + str(name_two) +'Score'])+" and team two has  "+ str(attr[str(name_three) + str(name_four) +'Score'])+". lets play the  hand "+str(attr['Hand'])
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class theirMadeIntentHandler(AbstractRequestHandler):
    """Handler for TheirMadeIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("theirMade")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        global lasttheirbid
        global name_three  
        global name_four  
        global globalCounter2
        slots = handler_input.request_envelope.request.intent.slots 
        name_ones = slots['number'].value
        logging.info(name_ones)
        lasttheirbid = int(name_ones) * 10 
        globalScoreTeamtwo = int(name_ones) * 10 
        logging.info(globalScoreTeamtwo)
        attr = handler_input.attributes_manager.persistent_attributes
        attr[str(name_three) + str(name_four) +'Score']+= attr[str(name_three) + str(name_four) +'Present']
        #attr['Hand']+=1
        attr['logic']=0
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        if(attr['logic2']==1):
            attr = handler_input.attributes_manager.persistent_attributes
            attr['Hand']+=1
            attr['negativeone']=0
            attr['negativetwo']=0
            attr['logic2']=0
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
            speak_output= "ok. i have team one now has "+str(attr[str(name_one) + str(name_two) +'Score']) +" and team two has "+str(attr[str(name_three) + str(name_four) +'Score'])+". lets play the  hand "+str(attr['Hand'])
        else:
            speak_output= "Ok. Team 2 Now has  "+ str(attr[str(name_three) + str(name_four) +'Score']) +". And what about Team 1?"
            attr = handler_input.attributes_manager.persistent_attributes
            attr['logic2']=1
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
#=======================================================================
class negativeTeamOneIntentHandler(AbstractRequestHandler):
    """Handler for negativeTeamOneIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("negativeTeamOne")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        global lasttheirbid
        global name_one  
        global name_three  
        global globalCounter2
        globalScoreTeamOne =  10 
        logging.info(globalScoreTeamOne)
        attr = handler_input.attributes_manager.persistent_attributes
        if(attr['negativeone']==0):
            globalScoreTeamOne=attr[str(name_one) + str(name_two) +'Score']- attr[str(name_one) + str(name_two) +'Present']
            attr['negativeone']=1
            attr['logic2']=1
            attr[str(name_one) + str(name_two) +'Score']=globalScoreTeamOne
            attr['negativeone']=1
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
        speak_output = speak_output = str(name_one) + " and " + str(name_two) + " now have negative " + str(attr[str(name_one) + str(name_two) +'Present'])+ " points."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

#=======================================================================
class negativeTeamTwoIntentHandler(AbstractRequestHandler):
    """Handler for negativeTeamTwoIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("negativeTeamTwo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        global lasttheirbid
        global name_three  
        global name_four  
        global globalCounter2
        globalScoreTeamtwo =  10 
        logging.info(globalScoreTeamtwo)
        attr = handler_input.attributes_manager.persistent_attributes
        if(attr['negativetwo']==0):
            globalScoreTeamtwo=attr[str(name_three) + str(name_four) +'Score']- attr[str(name_three) + str(name_four) +'Present']
            attr['negativetwo']=1
            attr['logic2']=1
            attr[str(name_three) + str(name_four) +'Score']=globalScoreTeamtwo
            handler_input.attributes_manager.session_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()
        speak_output = speak_output = str(name_three) + " and " + str(name_four) + " now have negative " + str(attr[str(name_three) + str(name_four) +'Present'])+ " points."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
#==========================================================================================================================
class ourBoardIntentHandler(AbstractRequestHandler):
    """Handler for ourBoardIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ourBoard")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        globalScoreTeamOne = 4 * 10 + globalScoreTeamOne
        speak_output = "Your bid is a " + str(globalScoreTeamOne)
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        globalScoreTeamOne =attr[str(name_one) + str(name_two) +'Present']

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class ourBostonIntentHandler(AbstractRequestHandler):
    """Handler for ourBostonIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ourBoston")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        globalScoreTeamOne = 13 * 10 + globalScoreTeamOne
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        globalScoreTeamOne =attr[str(name_one) + str(name_two) +'Present']
        speak_output = "Your bid is a " + str(globalScoreTeamOne)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class oppenentBoardIntentHandler(AbstractRequestHandler):
    """Handler for oppenentBoardIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lastThierBid")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        globalScoreTeamtwo = 4 * 10 + globalScoreTeamtwo
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        globalScoreTeamtwo =attr[str(name_three) + str(name_four) +'Present']
        speak_output = "Their bid is a " + str(globalScoreTeamtwo)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class oppenentBostonIntentHandler(AbstractRequestHandler):
    """Handler for oppenentBostonIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("oppenentBoston")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamtwo
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        globalScoreTeamtwo =attr[str(name_three) + str(name_four) +'Present']
        speak_output = "Their bid is a " + str(globalScoreTeamtwo)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class showScoreIntentHandler(AbstractRequestHandler):
    """Handler for showScoreIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("showScore")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        global name_one  
        global name_two  
        global name_three  
        global name_four
        attr = handler_input.attributes_manager.persistent_attributes
        globalScoreTeamtwo=attr[str(name_three) + str(name_four) +'Score']
        globalScoreTeamOne=attr[str(name_one) + str(name_two) +'Score']
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        speak_output = str(name_one) + " and " + str(name_two) + " has "+ str(globalScoreTeamOne) + " and " + str(name_three) + " and " + str(name_four) + " has " + str(globalScoreTeamtwo)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class ourScoreIntentHandler(AbstractRequestHandler):
    """Handler for ourScoreIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ourScore")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        speak_output = "Team 1 has " + str(attr[str(name_one) + str(name_two) +'Score']) +" Points." 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class oppenentScoreIntentHandler(AbstractRequestHandler):
    """Handler for oppenentScoreIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("oppenentScore")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        attr = handler_input.attributes_manager.persistent_attributes
        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
        speak_output = "Team 2 has " + str(attr[str(name_three) + str(name_four) +'Score']) +" Points." 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class whoWinningIntentHandler(AbstractRequestHandler):
    """Handler for whoWinningIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("whoWinning")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        if globalScoreTeamOne > globalScoreTeamtwo:
            speak_output = "Team 1 has " + str(globalScoreTeamtwo) +" Points." 
        else:
            speak_output = "Team 2 has " + str(globalScoreTeamtwo) +" Points." 
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class wholosingIntentHandler(AbstractRequestHandler):
    """Handler for wholosingIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("wholosing")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        if globalScoreTeamOne > globalScoreTeamtwo:
            speak_output = "Team 1 has " + str(globalScoreTeamtwo) +" Points." 
        else:
            speak_output = "Team 2 has " + str(globalScoreTeamtwo) +" Points." 
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class lastOurBidIntentHandler(AbstractRequestHandler):
    """Handler for lastOurBidIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lastOurBid")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global lastourbid
        speak_output = "Your last bid was  " + str(lastourbid)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class lastThierBidIntentHandler(AbstractRequestHandler):
    """Handler for lastThierBidIntentHandler Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lastThierBids")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global lastThierBid
        speak_output = "there last bid was  " + str(lastThierBid)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global globalScoreTeamOne
        global globalScoreTeamtwo
        global lastourbid
        global lasttheirbid
        globalScoreTeamOne = 0
        globalScoreTeamtwo = 0
        lastourbid = 0 
        lasttheirbid = 0
        speak_output = "Welcome to spades live, Who's playing?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again. "+str(exception)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


#sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(createGroupsIntentHandler())
sb.add_request_handler(ourTeamIntentHandler())
sb.add_request_handler(ourMadeIntentHandler())
sb.add_request_handler(theirMadeIntentHandler())
sb.add_request_handler(negativeTeamOneIntentHandler())
sb.add_request_handler(negativeTeamTwoIntentHandler())
sb.add_request_handler(oppenentTeamIntentHandler())
sb.add_request_handler(oppenentTeamFirstIntentHandler())
sb.add_request_handler(oppenentBoardIntentHandler())
sb.add_request_handler(oppenentBostonIntentHandler())
sb.add_request_handler(ourBostonIntentHandler())
sb.add_request_handler(ourBoardIntentHandler()) 
sb.add_request_handler(showScoreIntentHandler()) 
sb.add_request_handler(oppenentScoreIntentHandler()) 
sb.add_request_handler(ourScoreIntentHandler()) 
sb.add_request_handler(wholosingIntentHandler()) 
sb.add_request_handler(whoWinningIntentHandler())
sb.add_request_handler(lastThierBidIntentHandler())
sb.add_request_handler(lastOurBidIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()