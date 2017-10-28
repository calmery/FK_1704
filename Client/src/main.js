import path from 'path'
import express from 'express'
import socketIo from 'socket.io'

const app = express()

path.resolve( __dirname, 'public' )
  |> express.static
  |> app.use

const server = app.listen( () => {
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
