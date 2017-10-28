module Update exposing (update, Msg(..))

import Model exposing (Model)
import Port exposing (emit)


type Msg
    = Emit String
    | On String


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Emit message ->
            ( model, Cmd.batch [ emit "Hello World" ] )

        On message ->
            ( message :: model, Cmd.none )
