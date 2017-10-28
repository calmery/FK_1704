module SpecalPen.View exposing (view)

import Html exposing (..)
import Html.Events exposing (..)
import SpecalPen.Model exposing (Model)
import SpecalPen.Update exposing (Msg(..))
import List


view : Model -> Html Msg
view model =
    div []
        [ div []
            (List.map (\response -> div [] [ text response ]) model)
        , a [ onClick <| Emit "Hello" ]
            [ text "Send message" ]
        ]
