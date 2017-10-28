import sys

function = lambda _1, _2: ( _1, _2 )

# get_cache
# clear_cache
# listen
# listen_once

class Plugin :

    def __init__( self, function=function ) :
        self.__function = function
        self.__cache    = []

    def get_cache( self ) :
        return self.__cache

    def clear_cache( self ) :
        self.__cache = []

        return True

    def listen( self, function=None ) :
        if function is not None and callable( function ) :
            self.__function = function

        self.clear_cache()

        while True :
            s = sys.stdin.readline()
            s = s.replace( '\n', '' )

            if s == 'exit' or s == 'quit' :
                break

            self.__cache.append( s )
            self.__function( s, self.get_cache() )

        return True

    def listen_once( self, function=None ) :
        if function is not None and callable( function ) :
            self.__function = function

        is_break = False

        while True :
            s = sys.stdin.readline()
            s = s.replace( '\n', '' )

            if s == '' :
                continue

            if s == 'exit' or s == 'quit' :
                is_break = True
                break

            self.__cache.append( s )
            self.__function( s, self.get_cache() )

            break

        if is_break :
            return False

        return True
