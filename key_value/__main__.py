





import sys
from key_value.help import key_value_help,key_value_invalid
from key_value.models import set_value,get_value,get_array,push_array,pop,delete

def main():
    args = sys.argv[1:]
    if len(args):
        if args[0]=='--help' or args[0]=='-h':
            key_value_help()
        elif args[0]=='set':
            pair=args[1:]
            set_value(pair)
        elif args[0]=='get':
            keys=args[1:]
            get_value(keys)
        elif args[0]=='getArray' or args[0]=='getarray':
            keys=args[1:]
            if len(keys)>=2:
                get_array(keys[0],keys[1])
            else:
                print("Key/Index Not Found !")
        elif args[0]=='push' or args[0]=='Push' or args[0]=='PUSH' or args[0]=='Enque' or args[0]=='enque' or args[0]=='ENQUE':
            keys=args[1:]
            if len(keys)>=2:
                push_array(keys[0],keys[1:])
            else:
                print("Key/Value Not Found !")
        elif args[0]=='pop' or args[0]=='Pop' or args[0]=='POP':
            keys=args[1:]
            pop(keys,-1)
        elif args[0]=='deque' or args[0]=='Deque' or args[0]=='DEQUE':
            keys=args[1:]
            pop(keys,0)
        elif args[0]=='delete' or args[0]=='Delete' or args[0]=='DELETE':
            keys=args[1:]
            delete(keys)
        else:
            key_value_invalid()
    else:
        key_value_help()
    
    
if __name__ == '__main__':
    main()