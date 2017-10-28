port module Subscriptions exposing (subscriptions)

import Model exposing (Model)
import Update exposing (Msg(..))
import Port exposing (on)


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.batch
        [ on On
        ]
