module Main exposing (..)

import Html exposing (program)
import SpecalPen.Model exposing (Model)
import SpecalPen.Update exposing (update, Msg(..))
import SpecalPen.Subscriptions exposing (subscriptions)
import SpecalPen.Init exposing (init)
import SpecalPen.View exposing (view)


main : Program Never Model Msg
main =
    program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }
