
# Imports
import sys, os
from key_value_BST.help import key_value_help,key_value_invalid
from key_value_BST.models import set_value,get_value

# Fuction to find store the 
# key and value as pair in BST
def main():
    args = sys.argv[1:]
    if len(args):

        # Some Commands for the CLI Tool
        commands = {
            "--help": key_value_help,
            "-h": key_value_help,
            "set": set_value,
            "get": get_value
        }

        # Calling for the Desired Function
        # Default as the Invalid Command 
        commands.get(args[0], key_value_invalid)(args[1:])
    else:
        key_value_help()


# Driver code
if __name__ == "__main__":
    main()