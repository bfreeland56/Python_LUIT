Python 3.7.10 (default, Jun  3 2021, 00:02:01) 
[GCC 7.3.1 20180712 (Red Hat 7.3.1-13)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> # variables
>>> 
>>> a_str = "I have to learn about python"
>>> print(a_str)
I have to learn about python
>>> 
>>> my_float = 10.5
>>> print(my_float)
10.5
>>> 
>>> an_integer = 10
>>> print(an_int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'an_int' is not defined
>>> 
>>> print(an_integer)
10
>>> shopping_list = ["apples", "peaches", "watermelon"]
>>> print(shopping_list)
['apples', 'peaches', 'watermelon']
>>> 
>>> 
>>> a_dict = {"userid": "JBloggs"}
>>> 
>>> print(a_dict)
{'userid': 'JBloggs'}
>>> 
>>> my_var = another_variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'another_variable' is not defined
>>> my_var = ("another_variable")
>>> print(my_var)
another_variable
>>> 
>>> 
>>> example_tuple = ("apple", "orange", "pear")
>>> print(example_tuple)
('apple', 'orange', 'pear')
>>> 
>>> 
>>> #strings
>>> 
>>> first_name = "Monty"
>>> last_name = "Python"
>>> print(first_name+last_name)
MontyPython
>>> 
>>> print(first_name + " " + last_name)
Monty Python
>>> 
>>> first_name = "John"
>>> surname = "Doe"
>>> print("My first name is {}. My family name is {}".format(first_name, surname))
My first name is John. My family name is Doe
>>> 
>>> firstname = "Jane"
>>> surname = "Doe"
>>> 
>>> print(f"My first name is {firstname}. My family name is {surname}")
My first name is Jane. My family name is Doe
>>> 
>>> 
>>> 
>>> my_int = 50
>>> sentence = "The total comes to:
  File "<stdin>", line 1
    sentence = "The total comes to:
                                  ^
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> my_int = 50
>>> sentence = "The total comes to: "
>>> 
>>> print(sentence + str(my_int)
... 
... 
... 
... 
KeyboardInterrupt
>>> 
>>> 
>>> >>> user = {"first_name":"Ada"}
  File "<stdin>", line 1
    >>> user = {"first_name":"Ada"}
     ^
SyntaxError: invalid syntax
>>> >>> print(user)
  File "<stdin>", line 1
    >>> print(user)
     ^
SyntaxError: invalid syntax
>>> {'first_name': 'Ada'}
{'first_name': 'Ada'}
>>> 
>>> 
>>> 
>>> user = {"first_name": "Ada"}
>>> print(user)
{'first_name': 'Ada'}
>>> 
>>> 
>>> user = {"first_name": "Ada"}
>>> print(user["first_name"])
Ada
>>> 
>>> 
>>> user["family_name"] = "Byron"
>>> print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}
>>> 
>>> 
>>> user["family_name"] = "Lovelace"
>>> print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}
>>> 
>>> 
>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}
>>> 
>>> 
>>> fruit = ["apples", "oranges", "bananas"]
>>> print(fruit)
['apples', 'oranges', 'bananas']
>>> 
>>> 
>>> len(fruit)
3
>>> 
>>> 
>>> print(fruit[-1])
bananas
>>> print(fruit[-2])
oranges
>>> 
>>> 
>>> fruit.append("kiwi")
>>> print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']
>>> 
>>> 
>>> fruit.insert(2, "passion fruit")
>>> print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']
>>> 
>>> 
>>> print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
>>> 
>>> print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']
>>> 
>>> fruit.sort()
>>> print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
>>> 
>>> 
>>> fruit.reverse()
>>> print(fruit)
['passion fruit', 'oranges', 'kiwi', 'bananas', 'apples']
>>> 
>>> del fruit[1]
>>> print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']
>>> 
>>> favorite_fruit = fruit.pop(1)
>>> print(fresh_fruit)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fresh_fruit' is not defined
>>> fresh_fruit = fruit.pop(1)                                                                                
>>> print(fresh_fruit)
bananas
>>> 
>>> 
>>> fruit.remove('bananas')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> fruit.remove('apples')
>>> print(apples)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'apples' is not defined
>>> 
>>> my_variable = "A string"
>>> print(type(my_variable))
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> my_number = 50
>>> some_string = "The number is '
  File "<stdin>", line 1
    some_string = "The number is '
                                 ^
SyntaxError: EOL while scanning string literal
>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> 
>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + str(my_number))
The number is 50
>>> 
>>> 
>>> pip install boto3
  File "<stdin>", line 1
    pip install boto3
              ^
SyntaxError: invalid syntax
>>> 
>>> 
KeyboardInterrupt
>>> 
>>> 
KeyboardInterrupt
>>> 
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> 
tory:~/environment $ pip install boto3
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: boto3 in /home/ec2-user/.local/lib/python3.7/site-packages (1.24.14)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /usr/local/lib/python3.7/site-packages (from boto3) (1.0.0)
Requirement already satisfied: botocore<1.28.0,>=1.27.14 in /home/ec2-user/.local/lib/python3.7/site-packages (from boto3) (1.27.14)
Requirement already satisfied: s3transfer<0.7.0,>=0.6.0 in /home/ec2-user/.local/lib/python3.7/site-packages (from boto3) (0.6.0)
Requirement already satisfied: urllib3<1.27,>=1.25.4 in /usr/local/lib/python3.7/site-packages (from botocore<1.28.0,>=1.27.14->boto3) (1.26.9)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.7/site-packages (from botocore<1.28.0,>=1.27.14->boto3) (2.8.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.28.0,>=1.27.14->boto3) (1.16.0)
tory:~/environment $ 
tory:~/environment $ pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-22.1.2-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 7.3 MB/s 
Installing collected packages: pip
Successfully installed pip-22.1.2
tory:~/environment $ 
tory:~/environment $ 
tory:~/environment $ pip freeze
astroid==2.3.0
aws-cfn-bootstrap==2.0
awscli==1.25.14
backcall==0.2.0
boto3==1.24.14
botocore==1.27.14
colorama==0.4.4
decorator==5.1.1
Django==2.0.2
docutils==0.14
git-remote-codecommit==1.16
ikp3db==1.4.1
importlib-metadata==4.11.4
ipython==7.34.0
isort==4.3.21
jedi==0.18.1
jmespath==1.0.0
lazy-object-proxy==1.7.1
lockfile==0.11.0
matplotlib-inline==0.1.3
mccabe==0.6.1
parso==0.8.3
pbr==5.9.0
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.29
ptyprocess==0.7.0
pyasn1==0.4.8
Pygments==2.12.0
pylint==2.4.4
pylint-django==2.3.0
pylint-flask==0.6
pylint-plugin-utils==0.7
pystache==0.5.4
python-daemon==2.2.3
python-dateutil==2.8.2
pytz==2022.1
PyYAML==5.4.1
rsa==4.7.2
s3transfer==0.6.0
simplejson==3.2.0
six==1.16.0
stevedore==3.5.0
traitlets==5.2.2.post1
typed-ast==1.5.4
typing_extensions==4.2.0
urllib3==1.26.9
virtualenv==16.2.0
virtualenv-clone==0.5.7
virtualenvwrapper==4.8.4
wcwidth==0.2.5
wrapt==1.14.1
zipp==3.8.0