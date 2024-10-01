# eptm.py

from commands import *
from parser import parse_command

def execute_commands(command_file):
    """Read and execute commands from a file."""
    with open(command_file, 'r') as f:
        for line in f:
            command, args = parse_command(line)
            if command is None:
                continue
            elif command == 'MOVE':
                if len(args) == 2:
                    move(*args)
                else:
                    print("MOVE command requires 2 arguments.")
            elif command == 'LEFT_CLICK':
                left_click()
            elif command == 'RIGHT_CLICK':
                right_click()
            elif command == 'DRAG_DROP':
                if len(args) == 4:
                    drag_drop(*args)
                else:
                    print("DRAG_DROP command requires 4 arguments.")
            elif command == 'TYPE':
                text = ' '.join(args)
                type_text(text)
            elif command == 'KEY_PRESS':
                if len(args) == 1:
                    key_press(args[0])
                else:
                    print("KEY_PRESS command requires 1 argument.")
            elif command == 'KEY_RELEASE':
                if len(args) == 1:
                    key_release(args[0])
                else:
                    print("KEY_RELEASE command requires 1 argument.")
            elif command == 'SCREENSHOT':
                if args:
                    screenshot(args[0])
                else:
                    screenshot()
            else:
                print(f"Unknown command: {command}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python eptm.py commands.txt")
    else:
        execute_commands(sys.argv[1])
