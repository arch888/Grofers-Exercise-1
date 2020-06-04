
# Imports
import os
from key_value_BST.help import key_value_invalid

# BASE Directory of the File Storage
BASE_DIR = os.path.join(os.getcwd(), "key_value_BST/static")
SUCCESS = "Success!"

"""
@param f: file
@return: list of Lines
"""
def readAllLinesOfFile(f):
    content = f.readlines()
    content = [x.strip() for x in content]
    return content

"""
@param key: Key of the new Node
@param value: Value of the new Node
@return bool: To show the insertion is successful
"""
def addCurrentNode(key, value):
    currentNode = open(os.path.join(BASE_DIR, key), "x")
    currentNode = open(os.path.join(BASE_DIR, key), "w")
    currentNode.writelines([key+"\n", value+"\n", "\n", "\n"])
    currentNode.close()
    return True


"""
@param key: Key of the new Node
@param value: Value of the new Node
@return bool: To show the insertion is successful
"""
def insertAtRoot(key, value):

    # Adding the root node as the current key
    try:
        root = open(os.path.join(BASE_DIR, "root"), "x")
    except:
        pass
    root = open(os.path.join(BASE_DIR, "root"), "w")
    root.write(key+"\n")
    root.close()

    # Adding the current node
    addCurrentNode(key, value)
    return True

"""
@param treeNode: Current Node of BST
@param key: New Key to be Inserted
@param value: Value of the Key
"""
def insertBST(treeNode, key, value):
    # Condition when there are no Node
    if not treeNode:
        insertAtRoot(key, value)
        return True
    try:
        treeRoot = open(os.path.join(BASE_DIR, treeNode), "x")
    except:
        pass
    treeRoot = open(os.path.join(BASE_DIR, treeNode), "r")
    content = readAllLinesOfFile(treeRoot)
    treeKey, treeValue, left, right = content[0], content[1], content[2], content[3]
    treeRoot.close()

    # Condition when the right child is the 
    # desired insertion or the new key place
    if treeKey < key:
        if right:
            insertBST(right, key, value)
        else:
            treeRoot = open(os.path.join(BASE_DIR, treeNode), "w")
            treeRoot.writelines([treeKey+"\n", treeValue+"\n", left+"\n", key+"\n"])

            # Adding the current node
            addCurrentNode(key, value)
            treeRoot.close()
    elif treeKey == key:
        treeRoot = open(os.path.join(BASE_DIR, treeNode), "w")
        # Updating the value
        treeRoot.writelines([treeKey+"\n", value+"\n", left+"\n", right+"\n"])
        treeRoot.close()
    else:
        if left:
            insertBST(left, key, value)
        else:
            treeRoot = open(os.path.join(BASE_DIR, treeNode), "w")
            treeRoot.writelines([treeKey+"\n", treeValue+"\n", key+"\n", right+"\n"])

            # Adding the current node
            addCurrentNode(key, value)
            treeRoot.close()
    return True

"""
@param rootNode: Current Node of BST
@param key: Key value to search for
@return bool: Boolean value that key is found or not
"""
def searchBST(rootNode, key):
    if not rootNode:
        print("Doesn't Exist!")
        return False
    try:
        rootFile = open(os.path.join(BASE_DIR, rootNode), "x")
        print("Doesn't Exist!")
        return False
    except:
        pass
    rootFile = open(os.path.join(BASE_DIR, rootNode), "r")
    content = readAllLinesOfFile(rootFile)
    if rootNode == key:
        if len(content) > 1:
            print(content[1])
            return True
        else:
            print("Doesn't Exist!")
            return False
    if len(content) and content[0] > key:
        try:
            return searchBST(content[2], key)
        except:
            print("Doesn't Exist!")
            return False
    else:
        try:
            return searchBST(content[3], key)
        except:
            print("Doesn't Exist")
            return False


"""
@param args: key and value as list
@param bool: To show the insertion is successful
"""
def set_value(args):

    # Not Enough arguments
    if len(args) < 2:
        key_value_invalid()
        return

    # Open the root file
    root = os.path.join(BASE_DIR, "root")
    key = args[0]
    value = args[1]
    try:
        rootFile = open(root, "x")
        rootFile = open(root, "r")
    except:
        rootFile = open(root, "r")
    content = readAllLinesOfFile(rootFile)
    treeRoot = content[0] if content else None
    insertBST(treeRoot, key, value)

    # Successfully inserted the key value pair
    print(SUCCESS)
    rootFile.close()
    return

"""
@parm args: Key to search for
@return bool: Boolean value that it is found or not
"""
def get_value(args):
    
    # Not enough arguments
    if len(args) < 1:
        key_value_invalid()
        return False

    # Key of the node
    key = args[0]
    root = os.path.join(BASE_DIR, "root")

    # Exception to check if the root file exist 
    # or not in the directory
    try:
        rootFile = open(root, "x")
        print("Doesn't Exist!")
        return False
    except:
        pass
    rootFile = open(root, "r")
    content = readAllLinesOfFile(rootFile)
    rootNode = content[0] if content else None

    # Condition to check if the root Node
    # exist or not in the directory
    if not rootNode:
        print("Doesn't Exist!")
        return False
    else:
        return searchBST(rootNode, key)