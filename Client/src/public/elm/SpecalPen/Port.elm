port module SpecalPen.Port exposing (setTitle, emit, on)


port setTitle : String -> Cmd a


port emit : String -> Cmd a


port on : (String -> msg) -> Sub msg
