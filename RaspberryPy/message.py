# -*- coding: utf-8 -*-

class Message :

    def __init__( self, event_name='', message='' ) :
        self.__event_name = event_name
        self.__message    = message

    def get_event_name( self ) :
        return self.__event_name

    def get_message( self ) :
        return self.__message

def dump( message ) :
    if isinstance( message, Message ) :
        return { 'event_name': message.get_event_name(), 'message': message.get_message() }

    return {}

def parse( message ) :
    if isinstance( message, dict ) and 'event_name' in message and 'message' in message :
        return Message( message['event_name'], message['message'] )

    return Message()
