from interactions import SelectMenu, SelectOption, Button, ButtonStyle, ActionRow



def Option(label: str, value: str):
    """ Used in Select """
    return SelectOption(label=label, value=value)


def Select(id: str, options: list[Option], placeholder: str, min: int = 1, max: int = 1):
    """
    Create a SelectMenu

    ```py
    Select('select',
        options=[
            Option('Label 1', 'Value 1'),
            Option('Label 2', 'Value 2'),
            Option('Label 3', 'Value 3'),
        ],
        placeholder='Select an option',
        min=1,
        max=3,
    )
    ```
    
    """
    if len(options) > 25:
        raise ValueError('There can be a maximum of 25 options')

    return SelectMenu(
        options=options,
        placeholder=placeholder,
        custom_id=id,
        min_values=min,
        max_values=max
    )

def Btn(id: str, style: ButtonStyle, label: str):
    """ 
    Create a Button [Button styles](https://support.discord.com/hc/article_attachments/1500019725621/buttons.png)

    ```py
    Btn('btn', ButtonStyle.PRIMARY, 'Click me')
    ```
    """
    return Button(label=label, style=style, custom_id=id)


def Grid(grid):
    """ 
    
    Create a components grid

    ```py

    btn  = Btn('btn', ButtonStyle.PRIMARY, 'Click me')
    btn2 = Btn('btn2', ButtonStyle.PRIMARY, 'Click me')
    btn3 = Btn('btn3', ButtonStyle.PRIMARY, 'Click me')

    select = Select('select',
        options=[
            Option('Label 1', 'Value 1'),
            Option('Label 2', 'Value 2'),
            Option('Label 3', 'Value 3'),
        ],
        placeholder='Select an option',
        min=1,
        max=3,
    )

    Grid([
        [select],
        [btn, btn2, btn3],
    ])
    
    """

    isMultidimensional = isinstance(grid[0], list)
    items = []

    if isMultidimensional:
        for row in grid:
            if len(row) > 1 and any(isinstance(col, SelectMenu) for col in row):
                raise TypeError('There can be no other component together with a select on the same row')

            items.append(ActionRow(components=row))

    else:
        if len(grid) > 1 and any(isinstance(col, Select) for col in grid):
            raise TypeError('There can be no other component together with a select on the same row')

        items.append(ActionRow(components=grid))

    return items
    