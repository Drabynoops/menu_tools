# Brendan Bard
# 12/04/2022
# Supplementary file

# The purpose of this code is to provide a series of command line interface
# tools for projects
from os import get_terminal_size
TERMINAL_WIDTH = get_terminal_size().columns
DEFAULT_BORDER_WIDTH = 3

def fullscreenSymbols(symbol):
    '''
    Outputs a full terminal width of specified symbol

    Parameters
    ----------
    symbol : str
        The symbol to be printed
    '''
    print(TERMINAL_WIDTH * symbol, end="")


def titleWithBorder(symbol:str, title:str, border_width=DEFAULT_BORDER_WIDTH):
    '''
    Provided that there is enough space, prints a title phrase with
    a border of specified symbols.

    Parameters
    ----------
    symbol : str
        the symbol used as a border
    text : str
        the title to be displayed
    border_width : int
        how many symbol appear on each side of the title
    '''
    available_space = 0 #initialization
    title_length = len(title)
    if title_length > TERMINAL_WIDTH: #Title is way too long TODO:Come up with a solution
        pass #Nothing to do
    elif title_length > (TERMINAL_WIDTH - (2 * border_width)): # Long 
        # Reduce border width to prioritize tile
        border_width = (TERMINAL_WIDTH - title_length) // 2
        available_space = TERMINAL_WIDTH - (2 * border_width) - title_length
    else:
        #Normal avaiable space calculation
        available_space = TERMINAL_WIDTH - (2 * border_width) - title_length
        
    first_spacing = available_space // 2 #Floor division
    # Below: Account for odd numbers being divided
    second_spacing = (first_spacing if (available_space % 2 == 0) else first_spacing + 1)
    print(symbol * border_width + " " * first_spacing + title + " " * second_spacing + symbol * border_width, end="")


def calculatePreceedingSpaces(text:str):
    '''
    Given submitted text, uses the terminal size to return the number of spaces
    before a text to make it somewhat centered. 
    
    Parameters
    ----------
    text : str
        text that you are basing the spacing off of
    
    Returns
    -------
    num_spaces : int
        the number of spaces to somewhat center the text provided
    '''
    length_of_text = len(text)
    num_spaces = (TERMINAL_WIDTH - length_of_text) // 2
    return num_spaces
