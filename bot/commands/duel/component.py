from age import *

def duel_component(attacks):
    """ Used in /duel command """

    select = Select('duel__select',
        options=[
            Option(label=attack, value=attack)
            for attack in attacks
        ],
        placeholder="I'll attack with",
        max=1,
    )

    return Grid([
        [select],
    ])

