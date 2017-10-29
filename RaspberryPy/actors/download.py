# -*- coding: utf-8 -*-

import pykka

import os
from subprocess import Popen, PIPE

import requests
import zipfile

from message import parse

def download_file( url ):
    file_name = url.split( '/' )[-1]
    r = requests.get( url, stream=True )
    with open( file_name, 'wb' ) as f:
        for chunk in r.iter_content( chunk_size=1024 ) :
            if chunk :
                f.write( chunk )
                f.flush()
        return file_name
    return False

def unzip( file_name ):
    with zipfile.ZipFile( file_name ,'r' ) as f :
        f.extractall( './plugins/' )

class DownloadActor( pykka.ThreadingActor ) :

    def __init__( self ) :
        super().__init__()

    def on_receive( self, message ) :
        message = parse( message )
        print( 'DownloadActor Received ' + message.get_event_name() + ' ' + message.get_message() )

        if message.get_event_name() == 'download' :
            url = message.get_message()
            file_name = download_file( url )
            unzip( file_name )
            os.remove( './' + file_name )
            return file_name

        return True
