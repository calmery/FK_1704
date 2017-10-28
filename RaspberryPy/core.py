from actors.plugin import PluginActor
from message import Message, dump

def main() :
    plugin_actor = PluginActor.start()

    plugin_actor.ask( dump( Message( 'reasoned', '1' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '2' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '3' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '4' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '5' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '6' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '7' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '8' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '9' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', '0' ) ) )
    plugin_actor.ask( dump( Message( 'reasoned', 'exit' ) ) )

    plugin_actor.ask( dump( Message( 'close' ) ) )
    plugin_actor.stop()

if __name__ == '__main__' :
    main()
