## Key-Value Pair Store

[![GitHub license](https://img.shields.io/github/license/arch888/key_value?logo=github&)](https://github.com/arch888/key_value/blob/master/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/arch888/key_value?logo=github)](https://github.com/arch888/key_value/) ![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/vinitshahdeo/ParkingLot?logo=snyk&color=green)

### About Problem

To **design a key-value pair store** REST API/CLI Tool with ability to do following tasks -

- REST/CLI to access key-value store

- GET & SET Interface for getting keys and storing data Respectively

- Storing Different types of Data Structures such as Stack/Queue 

- Performing CRUD Operations on those Data Structures

  

### Pre-Requisites

[![GitHub top language](https://img.shields.io/github/languages/top/arch888/key_value?label=Python&logo=Python)](https://github.com/vinitshahdeo/ParkingLot/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arch888/key_value?logo=github&color=teal)](https://github.com/arch888/key_value/) [![Issues](https://img.shields.io/github/issues/arch888/key_value)
](https://github.com/arch888/key_value)

The Source-Code for this project is written using Python. Make Sure you have [Python](https://www.python.org/) Installed on your PC. If you are using Windows/Mac please install from [here](https://www.python.org/downloads/).

Also make sure you have install [pip](https://pypi.org/project/pip/) properly in your system. [Link](https://www.liquidweb.com/kb/install-pip-windows/)

To check if you have Python and pip installed properly please use following commands in your terminal/command prompt.

- **Test Python : -** To see if python installed in your terminal type `python3 --version` in Terminal. This should print the version number. so you'll see something like this `Python 3.6.8` .
- **Test pip :-** To see if pip is installed. type `pip3 --version`.This will print the version number. so you'll see something like this `pip 9.0.1`.

> **Note:** You have to install Python and pip separately.

### How to run ?

This is a CLI Tool written in `Python`. This can run into following mode.

- **Interactive Mode :-** An Interactive Terminal based shell where commands can be typed in to perform different actions.

   

#### Installation

Proceed to the steps below only if you have `Python` installed. If not, please refer [Pre-Requisites](#pre-requisites) section.

Open your Terminal/command prompt and clone this repository using this command.

```
git clone https://github.com/arch888/key_value
```

Navigate (`cd`) to this folder and type following command.

```python
pip3 install .
```

Now, If the Package is Completely installed in your system then you will see something like this.

```
Processing /home/archit/Projects/Grofers/key_value
Installing collected packages: key-value
  Running setup.py install for key-value ... done
Successfully installed key-value-0.1.0
```

Or you can use any one of this commands to verify the installation.

```
key_value
key_value --h
key_value --help
```

After typing any of the above commands you'll see the help section of the Package where you can know small help provided there.

### List of User-Commands

Users can interact with the following simple set of the user commands provided below.

- `--help` or `--h` commands can be used to get help from package detailed explanation can be found [here](#help-command).
- `set` or `Set` or `SET` command can be used to set different types of Data-Structures in CLI Tool. Detailed Explanation of the Tool can be found [here](#set-command).
- `get` or `Get` or `GET` command can be used to get the key-value pair stored in the Database detailed explanation of this command can be found [here](#get-command).
- `getArray` or `getarray` command can be used to get Array elements stored as value in the key-value pair. Detailed Explanation of the Tool can be found [here](#get-array-command).
- `push` or `Push` or `PUSH` command can be used to push the elements in the stack. Detailed Explanation of this command can be found [here](#push-command).
- `pop` or `Pop` or `POP` command can be used to pop element from the Stack. Detailed Explanation of this command can be found [here](#pop-command).
- `Enque` or `enque` or `ENQUE` command can be used to enque element in the queue. Detailed Explanation of this command can be found [here](#enque-command).
- `Deque` or `deque` or `DEQUE` command can be used to deque element in the queue. Detailed Explanation of this command can be found [here](#deque-command).
- `Delete` or `delete` or `DELETE` command can be used to delete any data structure implemented key-value pair with argument as key. Detailed Explanation of this command can be found [here](#delete-command).

#### Help Command

This command is a very simple startup command which can be used to get simple help steps. To run this command you type -

```
key_value --help
```

This command will give you output something like this - 

```
Hello Team !
Let's Dive Deep and see the Features of this App - 


--help or -h - For help
set - For Setting Key Value Pair
get - For Getting Key Value Pair
getarray - For getting Array Data Structure
push - For pushing elements to existing Stack
pop - For poping elements out of existing Stack
enque - To enque elements in Queue
deque - To Deque elements from Queue
delete - To Delete key-value pair
update - Updating the Existing key-value pair


Thanks
Archit Kumar Dwevedi
```

#### Set Command

This command is generally used to store the key value pair data in the Database which is SQLite3 in the local system. This command have various functionality and two arguments are necessary for this command that is first one is the key which is in the form of string and second or the more than one arguments after that can be passed to create a Data Structure such as Array or Stack or Queue.

So Various cases of the Arguments passed is discussed here 

##### No/One Argument

In this case the CLI tool gives a warning that at least two of the arguments is necessary. This command will look something like this -

```python
key_value set
```

​														OR

```python
key_value set single_arg
```

Output for above these cases will look something like this -

```python
Sorry Invalid Command !
```

##### Two Argument

In this case the CLI will successfully store the Key-Value Pair in the Database. This command will look something like this - 

```python
key_value set your_key your_value
```

 This will store the Data Successfully and doesn't output anything if the key-value pair doesn't exists in the   Database otherwise this will give us morning something like this.

```
Key-Value Pair Already Exists !
```

##### > Two Arguments

In this case CLI Tool will store the data in the list format which can be used further in any format such as Array/Queue/Stack as per the Requirement.

Sample of this command will something look like this - 

```python
key_value set your_key value1 value2 value3 value4
```

This will successfully stores the data in the Database without any output where as in case the key-value pair exists then it will give warning shown below.

```
Key-Value Pair Already Exists !
```

#### Get Command

This command is generally used to output all types of Data Structure with the help of the Command user Interface.

Usage of this command is shown below.

```javascript
key_value get your_key
```

This will have different outputs in different cases which is shown following

##### Variable Data-Structure

In this there is only one Value Stored in respect to the key which will be shown as follows.

```
your_key - value
```

##### Array/Queue/Stack D.S.

In this all case this will output as the comma-separated values of the Data Structure.

```
your_key - value1,value2,value3,value4
```

##### Key Not Found

In this case this will give you a warning which will be as follows

```
Key Value Not Found !
```

##### No Key Provided

In this case when user doesn't provides any key for output then also it will give a output which will be as follows.

```
Sorry No Keys Found !
```

#### Get Array Command

In this command we will be able to get the value of the key value pair by its index which can be implemented on any of the Data Structure Array/Queue/Stack. This command will look something like this -

```
key_value getarray your_key index
```

This command also have various cases which can be given as follows - 

##### Key Not Found

In this case this will give you a warning which will be as follows

```
Key Value Not Found !
```

##### Index is not Integer

In this case when user gives index as non-int type then it will give following warning.

```
Sorry Index must be Integer
```

##### Index Out of Bounds

When there is a case when the index is greater than the length of the Array/Stack then it will give following warning.

```
Index Out of Range
```

##### Valid Key-Value-Index

In this case when there is a key having value and which is of array type and having the index as per the provided by the user will give a valid found output as follows - 

```
your_key[index] - value
```

#### Push Command

In this command it is generally used to implement the Stack Data Structure for pushing values to the stack which can be used as follows - 

```
key_value push your_key value
```

This command will also have multiple functionalities which can be given as follows - 

##### Key Not Found

In this case this will give you a warning which will be as follows

```
Key-Value Pair Not Found !
```

##### Value Not Provided

In this case when user doesn't provides the value as the argument then it gives the following warning 

```
Sorry Values Doesn't Exists 
```

##### Valid Command

In this case it simply pushes the data in the list and give no output.

#### Pop Command

This command is used to pop the element from the stack if Stack is not empty which can be given as follows - 

```
key_value pop your_key
```

This command will give the output as the popped value and removes the value from the Stack.

```
your_key.pop() - value
```

The Default Cases such as Key Not Found/Stack Empty will be same as explained above.

#### Enque Command

In this Command we generally wanted to implement a Queue in which we wanted to perform the operation enque for adding element to queue. This command can be used as follows - 

```
key_value enque your_key value
```

This command also doesn't output anything and enque the element out of the queue and the default cases are covered as per explained above that is Key Not Found/ Empty Queue.

#### Deque Command

In this command we generally wanted to implement a Queue in which we wanted to perform the operation deque for removing elements from the queue. This command can be used as follows.

```
key_value deque your_key
```

This command will output the value which is removed in the FIFO format

```
your_key.deque() - value
```

#### Delete Command

In this command we generally wanted to delete any key-value pair irrespective of the data structure which is used in the storing process it will delete that key value.

This command can be used as follows - 

```
key_value delete your_key
```

After deleting the key-value pair this will gives as a following output

```
Entry Deleted Successfully !
```

### Screenshots & Video

Screenshots of almost all cases can be found [here](/screenshots). Video for the same can be found [here](https://youtu.be/Mve0PeeW6Ds)

> Feel free to reach out to me via email. Shoot your doubts at dwevediar@gmail.com

# Thank You !

