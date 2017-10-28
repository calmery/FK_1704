module Init exposing (init)

import Model exposing (Model)
import Update exposing (Msg(..))
import Port exposing (setTitle)


init : ( Model, Cmd Msg )
init =
    let
        model =
            []

        cmd =
            [ setTitle "" ]
    in
        ( model, Cmd.batch cmd )
