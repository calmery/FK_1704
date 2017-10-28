import path from 'path'
import express from 'express'

const app = express()

path.resolve( __dirname, 'public' )
  |> express.static
  |> app.use

const port = app.listen( () => {
  console.log( 'Running app on localhost:' + port )
} ).address().port
