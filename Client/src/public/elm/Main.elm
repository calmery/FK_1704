port module Main exposing (..)

import Html exposing (Html, program, div, a, text)
import Html.Events exposing (onClick)
import List


type alias Model =
    List String


type Msg
    = Emit String
    | On String


port setTitle : String -> Cmd a


port emit : String -> Cmd a


port on : (String -> msg) -> Sub msg


init : ( Model, Cmd Msg )
init =
    let
        model =
            []

        cmd =
            [ setTitle "" ]
    in
        ( model, Cmd.batch cmd )


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Emit message ->
            ( model, Cmd.batch [ emit "Hello World" ] )

        On message ->
            ( message :: model, Cmd.none )


view : Model -> Html Msg
view model =
    div []
        [ div []
            [ text <| toString model ]
        , a [ onClick <| Emit "Hello" ]
            [ text "Send message" ]
        ]


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.batch
        [ on On
        ]


main : Program Never Model Msg
main =
    program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }
