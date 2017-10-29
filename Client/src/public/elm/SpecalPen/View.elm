module SpecalPen.View exposing (view)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import SpecalPen.Model exposing (Model)
import SpecalPen.Update exposing (Msg(..))
import List


menu : Model -> Html Msg
menu model =
    div [ class "hero-foot" ]
        [ nav [ class "tabs is-boxed is-fullwidth" ]
            [ div [ class "container" ]
                [ ul []
                    [ li [ class "is-active" ]
                        [ a []
                            [ text "Home" ]
                        ]
                    , li []
                        [ a []
                            [ text "Connection" ]
                        ]
                    , li []
                        [ a []
                            [ text "Plugins" ]
                        ]
                    ]
                ]
            ]
        ]


view : Model -> Html Msg
view model =
    section [ class "hero is-success is-fullheight" ]
        [ div [ class "hero-head" ]
            [ header [ class "navbar" ]
                [ div [ class "container" ]
                    [ div [ class "navbar-brand" ]
                        [ a [ class "navbar-item" ]
                            [ text "Specal Pen Client"
                            ]
                        ]
                    ]
                ]
            ]
        , div [ class "hero-body" ]
            [ div [ class "container has-text-centered" ]
                [ h1 [ class "title" ]
                    [ text "Specal Pen" ]
                , h2 [ class "subtitle" ]
                    [ text "JPHACKS 2017 Fukuoka" ]
                ]
            ]
        , menu model
        ]


wifi : Model -> Html Msg
wifi model =
    div [ class "container is-fluid" ]
        [ div [ id "form" ]
            [ div [ class "field" ]
                [ label [ class "label" ]
                    [ text "SSID" ]
                , div [ class "control" ]
                    [ input [ class "input", type_ "text", placeholder "SSID" ] [] ]
                ]
            , div [ class "field" ]
                [ label [ class "label" ]
                    [ text "Password" ]
                , div [ class "control" ]
                    [ input [ class "input", type_ "password", placeholder "PASSWORD" ] [] ]
                ]
            , div [ class "field" ]
                [ label [ class "label" ]
                    [ text "Message" ]
                , div [ class "control" ]
                    [ div [ class "select" ]
                        [ select []
                            [ option [] [ text "WEP" ]
                            , option [] [ text "WPA" ]
                            ]
                        ]
                    ]
                ]
            , div [ class "field is-grouped" ]
                [ div [ class "control" ]
                    [ button [ class "button is-link" ] [ text "Connect" ] ]
                ]
            ]
        , div []
            [ div []
                (List.map (\response -> div [] [ text response ]) model)
            , a [ onClick <| Emit "Hello" ]
                [ text "Send message" ]
            ]
        ]
