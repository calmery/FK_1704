port module SpecalPen.Subscriptions exposing (subscriptions)

import SpecalPen.Model exposing (Model)
import SpecalPen.Update exposing (Msg(..))
import SpecalPen.Port exposing (on)


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.batch
        [ on On
        ]
