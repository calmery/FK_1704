module SpecalPen.Init exposing (init)

import SpecalPen.Model exposing (Model)
import SpecalPen.Update exposing (Msg(..))
import SpecalPen.Port exposing (setTitle)


init : ( Model, Cmd Msg )
init =
    let
        model =
            []

        cmd =
            [ setTitle "" ]
    in
        ( model, Cmd.batch cmd )
