module SpecalPen.Update exposing (update, Msg(..))

import SpecalPen.Model exposing (Model)
import SpecalPen.Port exposing (emit)


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
