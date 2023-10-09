#TITLE
APP_TITLE = "New Optimised Calculator"

#size
APP_SIZE = (340, 610)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

#font
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    'gap': 0.5,
    'corner-radious': 0
}

OPERATORS = {
    'clear': {"col": 0, 'row': 2, 'text': "AC"},
    'percent': {'col': 2, 'row': 2, 'text': '%'}
}

COLORS = {
    'light-grey': {'fg': ('#505050', '#D4D4D2'), 'hover': ('#686868', '#efefed'), 'text': ('white', 'black')},
    'dark-grey': {'fg': ('#D4D4D2', '#505050'), 'hover': ('#efefed', '#686868'), 'text': ('black', 'white')},
    'orage': {'fg': '#FF9500', 'hover': '#FBB143', 'text': ('black', 'white')},
    'orange-heiglight': {'fg': 'white', 'hover': 'white', 'text': ('black', '#FF9500')}
}

NUM_POSITIONS = {
    '.': {'col': 2, 'row': 6, 'span': 1},
    '0': {'col': 0, 'row': 6, 'span': 2},
    '1': {'col': 0, 'row': 5, 'span': 1},
    '2': {'col': 1, 'row': 5, 'span': 1},
    '3': {'col': 2, 'row': 5, 'span': 1},
    '4': {'col': 0, 'row': 4, 'span': 1},
    '5': {'col': 1, 'row': 4, 'span': 1},
    '6': {'col': 2, 'row': 4, 'span': 1},
    '7': {'col': 0, 'row': 3, 'span': 1},
    '8': {'col': 1, 'row': 3, 'span': 1},
    '9': {'col': 2, 'row': 3, 'span': 1},
}

BLACK = '#000000'
WHITE = '#EEEEEE'
