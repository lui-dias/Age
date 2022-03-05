from re import sub
from typing import Awaitable

from interactions import *
from interactions.ext import wait_for

from age.components import Grid


class Bot(Client):
    def __init__(self, token, **kwargs):
        super().__init__(token, **kwargs)

        # Add wait_for and wait_for_component in bot
        wait_for.setup(self, True)

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


    # Typing for wait_for_component
    async def wait_for_component(
        self,
        components: Grid,
        check     : Optional[Callable[..., Union[bool, Awaitable[bool]]]] = None,
        timeout   : Optional[float] = None,
    ): ...

    # Typing for wait_for
    async def wait_for(
        self,
        name   : str,
        check  : Optional[Callable[..., Union[bool, Awaitable[bool]]]] = None,
        timeout: Optional[float] = None,
    ): ...

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