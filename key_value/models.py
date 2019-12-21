

import sqlite3
from key_value.help import key_value_invalid

conn = sqlite3.connect('db.sqlite3')

c=conn.cursor()


def initial():
    c.execute('''CREATE TABLE key_value (key text, value text)''')
    conn.commit()


def get(key):
    key=(key,)
    c.execute('''SELECT value FROM key_value WHERE key=?''',key)
    try:
        l=list(c.fetchone())
    except:
        print("Key Value Not Found !")
        return False
    # print(key[0]," - ",l[0])
    return l[0]






def get_value(keys):
    if len(keys)==0:
        print("Sorry No Keys Found")
    for i in keys:
        out=get(i)
        if out:
            print(i," - ",out)
    return True



def get_array(key,index):
    try:
        index=int(index)
    except:
        print("Sorry Index must be Integer")
        return False
    l=get(key)
    if l:
        l=list(l.strip().split(","))
        if index>=len(l) or index<-len(l):
            print("Index Out of Range")
            return False
        else:
            print(key,"[",index,"]",l[index])
            return l[index]
    else:
        print("Sorry Data Not Found !")
        return False


def check_exists(key):
    key=(key,)
    c.execute('''SELECT value FROM key_value WHERE key=?''',key)
    try:
        l=list(c.fetchone())
        return l[0]
    except:
        return False


def set_val(key,value):
    if check_exists(key):
        print("Key-Value Pair Already Exists !")
    else:
        m=(key,value,)
        c.execute('''INSERT INTO key_value VALUES (?,?)''',m)
        conn.commit()



def set_variable(pair):
    set_val(pair[0],pair[1])
    return True


def set_array(pair):
    key=pair[0]
    values=','.join(pair[1:])
    set_val(key,values)


        
    


def set_value(pair):
    # initial()
    if len(pair)<2:
        key_value_invalid()
    elif len(pair)==2:
        set_variable(pair)
    elif len(pair)>2:
        if pair[0]=="array" or pair[0]=="Array" or pair[0]=="ARRAY" or pair[0]=="list" or pair[0]=="List" or pair=="LIST":
            set_array(pair[1:])
        elif pair[0]=="stack" or pair[0]=="Stack" or pair[0]=="STACK":
            set_array(pair[1:])
        elif pair[0]=="queue" or pair[0]=="Queue" or pair[0]=="QUEUE":
            set_array(pair[1:])
        elif pair[0]=="variable":
            set_variable(pair[1:])
        else:
            print("Sorry Wrong Data-Structure")


def push_array(key,values):
    out=check_exists(key)
    if out:
        l=list(out.strip().split(","))
        if len(values):
            for i in values:
                l.append(i)
            s=','.join(l)
            print(s)
            update(key,s)
        else:
            print("Sorry Values Doesn't Exists")
    else:
        print("Key-Value Pair doesn't Exists")



def pop(keys,index):
    if len(keys)==0:
        print("Sorry Keys Not Found !")
        return False
    else:
        try:
            index=int(index)
        except:
            print("Index must be Integer")
            return False
        for i in keys:
            out=check_exists(i)
            if out:
                l=list(out.strip().split(","))
                if index>=len(l) or index<-len(l):
                    print("Index Out of Bounds")
                else:
                    val=l[index]
                    l.pop(index)
                    print(i," - ",val)
                    s=','.join(l)
                    update(i,s)

            else:
                print("Key Not Found !")
        return True
            



def update(key,value):
    if check_exists(key):
        key=(value,key,)
        c.execute('''UPDATE key_value SET value = ? WHERE key = ?;''',key)
        conn.commit()
    else:
        print("Key-Value Pair Doesn't Exists")


def delete(keys):
    if len(keys)==0:
        print("Sorry Keys Not Found !")
        return False
    else:
        for key in keys:
            if check_exists(key):
                key5=(key,)
                c.execute('''DELETE FROM key_value WHERE key = ?''',key5)
                conn.commit()
            else:
                print("Key Not Found ! - ",key)
    # print("Key-Value Pair Deleted !")
    return True