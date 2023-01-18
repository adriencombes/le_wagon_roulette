
import csv
import os
import random
import sys

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box,'\n')

def picker(batch):
    try:
        with open(os.path.join('data',f'{batch}.csv'),newline='') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            student = f'~ {random.choice(list(reader))[0]} ~'
        print('\nAnd the winner is :')
        print_msg_box(msg=student,indent=5)
    except FileNotFoundError:
        print('otto')

if __name__ == '__main__':
    picker(sys.argv[1])
