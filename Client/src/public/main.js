import Elm from './elm/Main.elm'

import io from './static/js/socket.io.js'

const socket = io()

const app = Elm.Main.fullscreen()
app.ports.setTitle.subscribe( title => document.title = title )

socket.on( 'message', message => {
  app.ports.on.send( message )
} )

app.ports.emit.subscribe( message => {
  socket.emit( 'message', message )
} )
