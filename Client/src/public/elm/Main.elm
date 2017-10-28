module Main exposing (..)

import Html exposing (program)

import Model exposing (Model)
import Update exposing (update, Msg(..))
import Subscriptions exposing (subscriptions)
import Init exposing (init)
import View exposing (view)


main : Program Never Model Msg
main =
    program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }
