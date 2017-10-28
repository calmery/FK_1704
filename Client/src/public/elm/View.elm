module View exposing (view)

import Html exposing (..)
import Html.Events exposing (..)
import Model exposing (Model)
import Update exposing (Msg(..))


view : Model -> Html Msg
view model =
    div []
        [ div []
            [ text <| toString model ]
        , a [ onClick <| Emit "Hello" ]
            [ text "Send message" ]
        ]
