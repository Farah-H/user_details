# User Details Task, Sparta Global
## Task Requirements 

Take the following information from trainees:
1. full name (inc middle name if applicable)
2. Address
3. National Insurance Number
4. Course 
5. Most recent education

Displaying the information in a professional way, keeping the following standards in mind:
1. Ensure first letter of the each string is capital
2. Ensure to take appropriate data type in, use casting to change data type

## Pre-Requisites 
It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## Syntax 
You can use the following syntax to get data from a user and assign it to a variable. Inputs are strings by default.

```python
variable = input('your message to the user')
```

If you want to take a specific type of input, e.g an integer, you can modify the syntax as follows to return an error when the inputted string cannot be converted to your desired data-type:
```python
variable = data_type(input('Your message to the user.'))

# E.G:
age = int(input('What is your age?'))
```
Please see [this list](https://www.w3schools.com/python/python_datatypes.asp) of datatypes in Python. 

If you want to take in a string, but modify this to meet a stylistic requirement (e.g capitalisation), you can modify the syntax as follows. 
```python
string_variable = input('Your message to the user.').string_method()

#E.G
first_name = input('What is your first name?.').capitalize()
```
Here is a [list of string methods](https://www.w3schools.com/python/python_ref_string.asp) which you can use, please note that American naming conventions are needed, such as `capitalize()` not `capitalise()`. 

Finally, to display the data in a user-friendly way, you can use a `print()` statement. A formatted string (f-string) can be used to avoid some issues with concatenation using `+`, such as the requirement for variables to be in string format. The syntax is as follows: 
```python
print(f'Your sentence containing {variable1} and {variable2}')
```
If you want to use the `+` concatenation method, the syntax is as follows, although be aware that each variable needs to be a string:

```python
#E.G
print('Your age is' +  str(age) + 'and you were born on ' + dob + '.')
```