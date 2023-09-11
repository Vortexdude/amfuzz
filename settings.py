#TITLE
APP_TITLE = "New Optimised Calculator"

#size
APP_SIZE = (400, 600)
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
    'light-grey': {'fg': ('#505050', '#D4D4D2'), 'hower': ('#686868', '#efefed'), 'text': ('white', 'black')},
    'dark-grey': {'fg': ('#D4D4D2', '#505050'), 'hover': ('#efefed', '#686868'), 'text': ('black', 'white')},
    'orage': {'fg': '#FF9500', 'hover': '#FBB143', 'text': ('black', 'white')},
    'orange-heiglight': {'fg': 'white', 'hover': 'white', 'text': ('black', '#FF9500')}
}

BLACK = '#000000'
WHITE = '#EEEEEE'