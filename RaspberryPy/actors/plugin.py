# -*- coding: utf-8 -*-

import pykka

import os
from subprocess import Popen, PIPE

from message import parse

class PluginActor( pykka.ThreadingActor ) :

    def __init__( self ) :
        super().__init__()

        self.__plugins   = os.listdir( 'plugins' )
        self.__processes = []

        for plugin_name in self.__plugins :
            process = Popen( ['python', 'plugins/' + plugin_name + '/' + plugin_name + '.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE )
            self.__processes.append( process )

    def kill_processes( self ) :
        for process in self.__processes :
            print( 'Result ' + str( process.pid ) + ' ' + str( process.communicate() ) )
            process.kill()

        return True

    def on_receive( self, message ) :
        message = parse( message )
        print( 'Received ' + message.get_event_name() + ' ' + message.get_message() )

        if message.get_event_name() == 'close' :
            return self.kill_processes()

        if message.get_event_name() == 'reasoned' :
            c = message.get_message()

            for process in self.__processes :
                p = process.stdin.write( ( c + '\n' ).encode() )

        return True
