from re import sub

from interactions import Client


class Bot(Client):
    def command(self, **kwargs):
        """ Decorator for creating a command """

        # I can't use super inside get_command_infos,
        # I need to save it in a variable to use
        a = super()

        '''
            Use the text above the arrow as a description of the bot
            The arrow and the bottom text are not added to the bot description

            @bot.command
            def foo(...):
                """ 
                Bot description

                <----------------->
                
                Function description
                """        
        
        '''
        
        def get_command_infos(f):
            d = kwargs | {'name': f.__name__, 'description': sub(
                    r'<-+>(.+|\n)+',
                    '',
                    sub(
                        r' {2,}',
                        '',
                        f.__doc__)
                ) # Discord already strip
            }
            a.command(**d)(f)

        return get_command_infos

    def add_event(self, coro, name=None):
        """
        Creates a new event in the bot
        
        I use this to create an event even after the bot is started
        """

        self._websocket._dispatch.register(coro, f'component_{name or coro.__name__}')

    def emit(self, event_name, *args, **kwargs):
        """
        Emits an event in the bot
        
        I use this to emit an event manually
        """
        self._websocket._dispatch.dispatch(event_name, *args, **kwargs)