import path from 'path'
import express from 'express'
import socketIo from 'socket.io'

import createWindow from './electron'

const app = express()

path.resolve( __dirname, 'public' )
  |> express.static
  |> app.use

const server = app.listen( process.env.PORT || undefined, () => {
  console.log( 'Running app on localhost:' + server.address().port )
} )

const port = server.address().port

const io = socketIo( server )

io.sockets.on( 'connection', socket => {
  console.log( 'Connected' )

  socket.on( 'message', message => {
    console.log( new Date(), message )
    socket.emit( 'message', 'Recieved ' + new Date() )
  } )
} )

createWindow( {
  width: 800,
  height: 600,

} )
  .then( window => {
    window.loadURL( 'http://localhost:' + port + '/' )
    window.setFullScreenable( false )
    window.setResizable( false )
    window.setMenu( null )
  } )
