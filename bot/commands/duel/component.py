from age import *

def duel_component(skills):
    """ Used in /duel command """

    select = Select('duel__select',
        options=[
            Option(label=skill.name, value=skill.name)
            for skill in skills
        ],
        placeholder="I'll attack with",
        max=1,
    )

    return Grid([
        [select],
    ])

