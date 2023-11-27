# Lab 3 - Developing Software Test Cases 
[ET0735 Lab 3 - Developing Software Unit Tests.docx.pdf](https://github.com/izzaops/lab3/files/13467000/ET0735.Lab.3.-.Developing.Software.Unit.Tests.docx.pdf)
### Main entry point
```python
def main():
	print("This is the main entry point")

if __name__ == '__main__':
	main()
```
- Single entry point which the interpreter will first execute
- Lines 4-5 prevents accidental invokes of the script
### Functions
- Used for [[Software Unit Test]]s
- Scope of a function is limited to current [[Python]] file it is located in
- Can be accessed outside using **imports** 
```python
def my_function():  
  print("Hello from a function")  

def main():
	my_function()

if __name__ == '__main__':
	main()
```
### Data types and Structures 
```python
this_str = "str"
# '' Also acceptable
this_int = 1
this_float = 1.23
this_list = [1,2]
this_tuple = (1,2) // Ordered, cannot change
this_set = {1,2} // Unordered, cannot change
this_Bool = True 
#  bytes is a data type
```
- Used [[Vaulted Modules/Y1S1 IEP/Function|Function]] **type()** to show data type 
- **Returns** a **object** which needs to be **converted** to a **string** if used in a **sentence**
```python
temperature = 38.4 
print(type(temperature))
# float
```
#### Lists
```python
thislist = ["apple", "banana", "cherry"]  
for x in thislist:  
  print(x)
```
### Conditional Statements
- Long hand version
```python
a = 200  
b = 33  
if b > a:  
  print("b is greater than a")  
elif a == b:  
  print("a and b are equal")  
else:  
  print("a is greater than b")
```
- Short hand version
```python
a = 2  
b = 330  
print("A") if a > b else print("B")
```
- If else statements **cannot** be **empty** use the word **pass** to avoid this error
- Pythons logical operators are **and**, **or**, and **not**

### Bit-wise operators
- Used for manipulating binary data
![](https://i.imgur.com/v3xI9iM.png)
### Loops
- For loops
```python
for x in range(2, 6):  
  print(x)
  #returns 2,3,4,5
```
- While loops
```python
i = 1  
while i < 6:  
  print(i)  
  i += 1
  #returns 1,2,3,4,5
```
### Importing packages
- Decompose software project into several projects 
- Use **import** mechanism to allow **functions** from other files to be used in another **python** file
```python
#File name called mymodule.py
def greeting(name):  
  print("Hello, " + name)

person1 = {  
  "name": "John",  
  "age": 36,  
  "country": "Norway"  
}
```
```python
#Seperate File
import mymodule  
  
mymodule.greeting("Jonathan")
```
- Possible to rename a module 
```python
#Seperate File
import mymodule as mx
  
mx.greeting("Jonathan")
```
- Possible to import variables
```python
#Seperate File
import mymodule  
  
a = mymodule.person1["age"]  
print(a)
```

### Using PyTest
```python
# import function from another file
import mymodule

# Define test case to be used
def test():
	result = []
	input = "This is a test"
	result = mymodule.isString(input)
	assert (result == 1)
```

### Dictionaries all in 1
- Used to represent data in a key value pair
- Data type not a **DATABASE** 
- No duplicates
- Ordered
- Changeable 
```python
mydict = {"name" : "yixuan", "age" : 18}
# example of a dictionary
print(len(mydict))
# 1 as 0, 1
```

- Accessing Items in a dictionary
```python
mydict = {"name" : "yixuan", "age" : 18}
print(mydict["name"])
print(mydict.get("name"))
# yixuan
```

- Iterating through a dictionary ways
```python
mydict = {"name" : "yixuan", "age" : 18}
# returning values
for key in mydict:
  print(mydict[key])
# yixuan , 18

# returning keys
for key in mydict:
  print(key)
# name, age
```

- Iterating through a list with dictionaries 
```python
myList = [
	{
		'foo':12,
		'bar':14
	},
	{
		'foo':52,
		'bar':641
	},
	{
		'foo':6,
		'bar':84
	}
]

for dictionary in myList:
	print(dictionary['foo'])
# basically loops through the list, at each index there is a dictionary. The second line will take the 'foo' key and print out its value 

for dictionary in myList:
	for key in dictionary:
      		print(key)
# Prints out each key 

ET0735 - DEVOPS FOR AIOT
SCHOOL OF ELECTRICAL AND ELECTRONIC ENGINEERING, SINGAPORE POLYTECHNIC

LABORATORY 3: DEVELOPING SOFTWARE UNIT TESTS

Objectives

By the end of the laboratory, students will be able to
Explain the use of PyTest for Software Unit Testing
Install PyTest in PyCharm
Define Unit Tests in PyTest

Activities
Installation and Setup of PyTest
Configure PyTest for Unit Testing in PyCharm
Create Software Unit Tests using PyTest

Review
PyTest is successfully installed in PyCharm.
PyTest Unit Test cases are created for the Python code for Lab 2 and Lab 3.

Equipment:
Windows OS laptop


Procedures:
Installation of PyTest in PyCharm

Launch the PyCharm software. If prompted to select a project, select the Lab2 project that you had created in Lab2 experiment.

Go to “File → Settings”. This opens the Python Package window in PyCharm. Expand “Project: ET0735_Lab2” and select “Python Interpreter”.

Figure 1 – View the Python Package window in PyCharm.

Under “Python Interpreter”, check if the PyTest Python package has already been installed. For the example shown in Figure 1, there is no sign of PyTest Python package. This means that PyTest has not been installed.

If PyTest has not been installed, then click the “+” icon to add new package.

Figure 2 – Click the ‘+’ icon to add new packages.


The “Available Packages” window pops up, listing packages available to be installed. In the search textbox, enter “pytest”. The PyTest package will be shown and selected. Click the “Install Package” button to install PyTest.

Figure 3 – Search for the PyTest package for installation.
After the installation of the PyTest package has completed, check that PyTest is now listed under the Python Interpreter installed packages list (i.e. repeat Step 1.2). You should find pytest in the list (see Figure 4).

Steps 1.5 and 1.6 can be used to install most of the 3rd party additional Python libraries you might need in the future.




Figure 4 – Verify that the PyTest package has been installed.


Configure PyTest for Unit Testing in PyCharm

After the PyTest package has been installed, we need to setup the current PyCharm project to specify that we will use PyTest for all the Unit Tests defined within the current PyCharm project scope. Take note that this setting have to be enabled for each project that you intend to use pytest.
2.1. Go to “File → Settings → Tools → Python Integrated Tools”. In the “Testing” section, open the dropdown list of the “Default test runner” field, and select “pytest”. Click “Apply”, then click “OK”. This now configures PyCharm to use PyTest as the default Unit Testing Tool.

Figure 5 – Configure PyCharm to use PyTest as the default Unit Testing Tool.

Create and Execute Software Unit Tests using PyTest

In the previous lab we learned the basics of Python programming, we will now extend this to also introduce the basics of Software Unit Testing based on the Python PyTest Unit Testing framework.
The PyTest Unit Test framework uses standard Python code to define Unit Test cases which we can use to test each Python function we have implemented.
Using PyTest, we use the keyword “assert( … )” to evaluate the return value of a Python function with the expected value/s returned by the function under test.
Follow the steps below to clone an example of a sample Python script that sorts some numbers in ascending and descending order,
Go to the C:\ directory of your laptop. Go to “Local_Git_Repository” folder that you have created in lab 1.

Open a CMD prompt window, and change directory to c:\Local_Git_Repository.

Clone the Lab 3 Git repository from the link https://github.com/ET0735-DevOps- AIoT/Lab3.git, using the git command below.

git clone https://github.com/ET0735-DevOps-AIoT/Lab3.git



Figure 6 – Clone a repository from GitHub.


A new folder “Lab3” will be created in the C:\Local_Git_Repository directory. This folder is a clone of the remote GitHub repository that you had specified in Step 3.3. You should find the following 7 items in the Lab3 folder:

.git
.idea
Employee_info.py
Lab3.py
price_info.py
README.md
Test_Lab3.py

To open the newly cloned project for experiments, in PyCharm, click “File → Open”. When the “Open File or Project” window pops up, navigate to C:\Local_Git_Repository, select the Lab3 folder and click “OK”.

Figure 7 – Open the newly cloned project “Lab3” in PyCharm.


When prompted about how to display this project, choose “This window”. The project Lab2 will be closed, and project Lab3 will be opened.

Figure 8 – Project “Lab3” is opened in PyCharm.

Right-click “Lab3.py” and select “Run Lab3” from the dropdown list. This runs the Python file Lab3.py. Check that the correct console output is displayed to sort a list of numbers in ascending or descending order, as shown below.



Figure 9 – Console output when running the Lab3.py file.


In the PyCharm project Lab3, notice that there is an additional file “Test_Lab3.py”. Double-click it to open.

Figure 10 – “Test_Lab3.py” is a Python file that contains the PyTest unit tests.


“Test_Lab3.py” is a Python file where we have defined the PyTest Unit Test to check that all the functions implemented in “Lab3.py” are correct
In “Test_Lab3.py”, the following PyTest Unit Test cases are defined,
Test Case 1 🡪 test_bubble_sort_ascending()
Test Case 2 🡪 test_bubble_sort_descending()
Test_Case3 🡪 test_bubble_sort_invalid()
Test Cases 1 and 2 are known as “Positive” test cases where the test cases check for valid input combinations versus the expected result.
Test Case 3 is for checking what happens when invalid or unexpected inputs are passed into the function “bubble_sort()”.

For each PyTest test, notice the format and syntax below where each test cases ends with an “assert” statement


The “assert” statement in PyTest basically returns a Boolean value True or False of the condition asserted or checked is True or False.
In Software Unit Testing, we basically want to verify and check that the function under test returns some predefined expected values based on a set of corresponding inputs.
To execute PyTest unit test cases inside the PyCharm IDE, there are 2 main methods,
Execute all PyTest Unit Test cases within a Python script
Execute selected individual test cases
If you want to execute all PyTest test cases, just right click on any PyTest Python file (see Figure 11) to run all test functions within the selected Python file.

Figure 11 – To execute all PyTest test cases.
To run selected PyTest functions individually in PyCharm, just click on the green icon on the left margin of the PyTest function you want to execute (see Figure 12).





Figure 12 – To run selected PyTest functions individually in PyCharm.


Try to execute all PyTest test cases in the Test_Lab3.py file, using the approach shown in Figure 11. After running all the PyTest Unit Test case, a Test Status report will be shown in PyCharm, summarizing the test cases that were executed and the test results.







Exercise 1
Figure 13 – Test Status report, summarizing the test cases executed and the test results.

Based on the BMI Python code in “bmi.py” that you implemented in the previous Lab 2, we will now implement suitable PyTest cases to verify that your function “calculate_bmi()” is implemented correctly based on the requirements in Table 2.

Open your Lab 2 pycharm project and access Python file “bmi.py”, modify the function “calculate_bmi()” to also return the following values defined in Table 1 below,

Weight Classification
Return Value
Under weight
-1
Normal weight
0
Over weight
1

Table 1

After successfully implementing the above, commit your changes and push to your lab2 github repository.

In your lab3 pycharm project, using the Lab 3 Git repository, create a new Git submodule based on your Lab 2 Github repository which you have updated in the task above. Write down the Git command/s used in the box below,
git submodule add https://github.com/izzaops/lab2

Using the existing Lab3 PyCharm project, create a new PyTest file “Test_bmi.py” which we will use to define some PyTest Unit Test cases to verify the Lab 2 BMI Python application code.

Add a suitable “import” statement at the top of the new “Test_bmi.py” file to import your Lab 2 “bmi..py” file based on your own folder structure for Lab 2. For example you can add the following import if you had stored all your Lab 2 files in a folder called “ET0735_Lab2”.

import ET0735_Lab2.bmi as bmi

In “Test_bmi.py”, create and implement the PyTest Unit Test functions below based on the requirements defined in Table 2

test_bmi_normal_weight() test_bmi_over_weight() test_bmi_under_weight()


BMI Range
Weight Classification
BMI < 18.5
Under Weight
18.5 ≤ BMI ≤ 25.0
Normal Weight
BMI > 25.0
Over Weight


Table 2

Once the unit test functions are implemented and tested to work, you will need to commit your changes to your local repository to track your progress.
Write the command in the box below to check the files that you need to add and commit.

git add Test_bmi.py
git commit Test_bmi.py

git commit -m "Lab 3 Exercise 1 (g)"


Did you notice in the “untracked files” section there is a new folder    pycache  ?


Question : What files are found in this folder? Do you need to include these files and folder in your git repository? State your reasons.

The __pycache__ directory contains .pyc files corresponding to your Python modules. For example, if you have a Python module named my_module.py, you will find a corresponding my_module.cpython-<version>-<platform>.pyc file in the __pycache__ directory.

You typically don't need to include the __pycache__ directory and its contents in your Git repository for the following reasons:

They are generated files: The .pyc files are generated by Python and are not part of your source code. Including them in your Git repository is unnecessary because they can be regenerated when needed.

Version and platform-specific: The .pyc files are platform-specific and version-specific. Including them in your repository might lead to compatibility issues when working on different platforms or with different Python versions.

They clutter the repository: Including automatically generated files like .pyc files in your Git repository can clutter it and make it harder to manage and collaborate with others.

In order for git to ignore certain specific files or folders, you will need to add a new file .gitignore.
In your code folder create a new file .gitignore. To ignore     pycache  folder, you can add the following code in .gitignore file:

  pycache /


Add and commit the files that you have modified for this section with a message stating your implementation. Do not push your changes to remote repository yet.
git add .gitignore  
git commit -m "Add .gitignore file to ignore __pycache__ directory"

Exercise 2
Based on the requirements defined in Table 3 below, analyse the Python code implemented in Lab3.py and the PyTest Unit Test cases defined in Test_Lab3.py
If you find any parts of the Python code implementation that does not match the requirements defined in Table 3, then please proceed to modify the Python code to match the requirements defined in Table 3.


Requirement ID
Requirement
PyTest Function/s
REQ-01
If < 10 numbers are entered and “SORT_ASCENDING” is passed to the function “bubble_sort()”, then the function returns the list of numbers sorted in ascending order.
def test_bubble_sort_ascending()




REQ-02
If < 10 numbers are entered and “SORT_DESCENDING” is passed to the function “bubble_sort()”, then the function returns the list of numbers sorted in descending order.
def test_bubble_sort_descending()
REQ-03
If >= 10 numbers are entered, the function “bubble_sort()” shall return the integer value 1
def test_bubble_sort_large_input():
REQ-04
If 0 numbers are entered, the function “bubble_sort()” shall return the integer value 0
def test_bubble_sort_empty_input():
REQ-05
If any of the values entered on the command line console are not integers, the function “bubble_sort()” shall return the integer value 2
def test_bubble_sort_non_integer_input():

Table 3

Using Table 3, update the column “PyTest Function/s” for requirements that have an existing Unit Test case defined in Test_Lab3.py.

For all requirements that do not have any test case defined in Table 3, implement the missing Unit Test Cases in Test_Lab3.py.

If any of the requirements defined in Table 3 are either not implemented or implemented differently in the existing code, then you need to update the Python code to match the requirements in Table 3.

Execute all PyTest Unit Test cases and check that all requirements defined in Table 1 are fully tested and pass the PyTest Unit Test Cases.
Add, Commit and Push changes to a new Github repository
Since we cloned the initial Lab 3 Github repository, the remote URL has been already been configured to “https://github.com/ET0735-DevOps-AIoT/Lab3.git” and needs to be changed to the URL of new Lab 3 Github repository

Create a new repository “Lab3” in Github

View the current remote URL with the following Git command and write the results of the git command below,
git remote –v
origin  https://github.com/ET0735-DevOps-AIoT/Lab3.git (fetch)
origin  https://github.com/ET0735-DevOps-AIoT/Lab3.git (push)


Update the remote origin to the URL of your ne Github repository using the command below replacing {URL} with the URL to your new Github “Lab3” repository
git remote set-url origin https://github.com/izzaops/lab3
Add and Commit all changes to the local repository

Create a new Git Tag “Lab3_v1.0”

Push all changes and the new Tag to Github

For any PyTest Unit Test cases that fail, implement the bug fix changes in Lab3.py and the run the PyTest Unit Test cases again until all pass.

Add and Commit the updated code implementation in Lab3.py (m)Create a new Git Tag “Lab3_v2.0” and Push all changes to Github

Exercise 3

Based on the exercises in Lab2.py, create PyTest Unit Test cases for the following functions,

find_min_max()
calc_average()
calc_median_temperature()

Open the PyCharm project Lab2, create a new file “Test_Lab2.py”

Create the new test cases for the functions above in “Test_Lab2.py”

Commit and Push all changes to Github for Lab 2 Git Repository

Create a new Software Release “Lab2_v3.0” in Github

Exercise 4
In this exercise, you will be working with python dictionaries. Dictionaries are a versatile and powerful built-in data structure in the Python programming language. Dictionaries are unordered, mutable, and store key-value pairs, also known as associative arrays or hash maps in other programming languages. Each key in a dictionary is unique, and it maps to a corresponding value, allowing for quick and efficient data retrieval and manipulation.
Now open your lab3 pycharm project and open the file price_info.py. This python file contains 2 dictionaries, one for the price list of fruits named price_list and another for the quantity of fruits that was purchased. The key and values are distinguished by the “:”. Any value can be accessed by using the corresponding key.

There are 2 functions created using the dictionaries provided. For the function cost_of_fruits, given the key for the fruit and quantity, the total cost of the purchase is printed. For the function total_cost_shopping, the 2 dictionaries are traversed and total cost of the purchase is computed based on the quantity in quantity_list for each fruit. Implement the missing code in total_cost_shopping. Test the code to make sure it works correctly.

Create a new file test_price_info and write the unit test cases for the following functions:

total_cost_shopping()
cost_of_fruit()

commit all changes and push your implemented code to your lab 3 repository.

Create new Software Release “Lab2_v4.0” in Github

Exercise 5
In this exercise, you will be working with list of python dictionaries. A list of dictionaries can be used as a simple form of database, where each dictionary in the list represents a record or row in the database, and the keys in each dictionary represent the fields or columns of the database.
For example, you might define a list of dictionaries to represent a table of customer information, where each dictionary in the list represents a customer record with fields such as name, email, phone, and address.
Here is an example of customer records:
customers = [
{'name': 'Alice', 'email': 'alice@example.com', 'phone': '555-1234', 'address': '123 Main St'},
{'name': 'Bob', 'email': 'bob@example.com', 'phone': '555- 5678', 'address': '456 Maple Ave'},
{'name': 'Charlie', 'email': 'charlie@example.com', 'phone': '555-9012', 'address': '789 Oak Rd'},
]
Once you have a list of dictionaries like this, you can easily perform various database operations on it, such as adding or removing records, querying records by specific fields or values, and updating fields in specific records.
You will need to implement some functions for an employee information tracking system python application in this exercise.


Now open your lab3 pycharm project and open the file employee_info.py. The application with some not implemented functions are available. employee_data is a dictionary with key values for “name”, “age”, “department” and “salary”. While the corresponding values for each key is separated by a (‘:’). Some common methods for working with dictionaries include keys(), values(), items(), get(), update(), and pop(). These methods make it easy to interact with and manipulate dictionary data.

In this simple application, there are 4 options available:

Display all the records of employee
Display the average salary
Display the employee details within certain age range
Display employees within a particular department.

	The first requirement is to calculate the average salary of all the employees in the database. The function stub : calculate_average_salary is already provided. Implement the code and test. Refer to the get_employees_by_age_range function for usage of dictionaries. After successfully implementing the function. Commit the code in your local repository with an appropriate message for your reference.

The second requirement is to display employees in a given department. The department name is provided as an parameter to the function get_employees_by_dept. Implement and test for this function. Subsequently commit the code in your local repository.

Create a new file test_employee_info and write pytest cases for the following functions:

get_employees_by_age_range
calculate_average_salary
get_employees_by_dept

Commit all changes and push all your changes to lab3 repository.

Create new Software Release “Lab2_v5.0” in Github

lab 3 - https://github.com/izzaops/lab3
Lab3.py


print("Lab 3 - Software Unit Testing with PyTest")


SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):


   # Check if the input list is empty
   if not arr:
       return 0


   # Check if all elements in the list are integers
   if not all(isinstance(x, int) for x in arr):
       return 2


   # Copy input list to results list
   arr_result = arr.copy()


   # Get number of elements in the list
   n = len(arr_result)


   if n < 10:
       # Traverse through all array elements
       for i in range(n - 1):
           # range(n) also work but outer loop will
           # repeat one time more than needed.


           # Last i elements are already in place
           for j in range(0, n - i - 1):


               if sorting_order == SORT_ASCENDING:
                   if arr_result[j] > arr_result[j + 1]:
                       arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]




               elif sorting_order == SORT_DESCENDING:
                   if arr_result[j] < arr_result[j + 1]:
                       arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


               else:
                   # Return an empty array
                   arr_result = []
   else:
       arr_result = 1 # if n>=10


   return arr_result


def main():
   # Driver code to test above
   arr = [64, 34, 25, 12, 22, 11, 90]


   # Sort in ascending order
   result = bubble_sort(arr, SORT_ASCENDING)
   print("\nSorted array in ascending order: ")
   print(result)


   # Sort in descending order
   print("Sorted array in ascending order: ")
   result = bubble_sort(arr, SORT_DESCENDING)
   print(result)


if __name__ == "__main__":
   main()
employee_info.py


# Define a dictionary to store employee information
employee_data = [
   {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
   {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
   {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
   {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
   {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
   {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]


def get_employees_by_age_range(age_lower_limit, age_upper_limit):
   result = []


   # check for age limits and append the item to result
   for item in employee_data:
       if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
           result.append(item)


   return result






def calculate_average_salary():
   total = 0
   average = 0


   # loop through the employee_data list to find and sum up the total of all the salaries
   for item in employee_data:
       total += item['salary']


   # calculate the average
   if len(employee_data) > 0:
       # check to see if the list is not empty
       average = total / len(employee_data)  # find how many records there are in the list to divide the total


   return average






def get_employees_by_dept(department):
   result = []


   # check the department and append the item to the result if it matches the user's inputted department
   for item in employee_data:
       if str(item["department"]) == department:
           result.append(item)


   # item["department"] /= department


   # department = what the USER inputs
   # item ["department"] = what the LIST has


   return result






def display_all_records():
   print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
   for item in employee_data:
       print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))






def display_records(employee_info):
   print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
   for item in employee_info:
       print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))






def display_main_menu():


   print("\n----- Employee information Tracker -----")


   print("Select option\n")


   print("1 - Display all records")
   print("2 - Display average salary")
   print("3 - Display employee within age range")
   print("4 - Display employee in a department")


   print("Q - Quit")


   option = input("Enter selection =>")






   if option == '1':
       display_all_records()


   elif option == '2':
       average_salary = calculate_average_salary()
       print("Average salary = " + str(average_salary))


   elif option == '3':
       age_lower_limit = input("age (Lower Limit) = ")
       age_upper_limit = input("age (Upper Limit) = ")
       employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
       display_records(employee_info)


   elif option == '4':
       department = input("Name of Department = ")
       employee_info = get_employees_by_dept(department)
       display_records(employee_info)


   elif option == 'Q':
       quit()


def main():


   while (True):
       display_main_menu()




if __name__ == "__main__":
   main()
price_info.py


price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }


quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}




def total_cost_shopping():
   total_cost = 0
   for key in price_list.keys():
       if key in quantity_list:
           # loops for every key in the list - goes thru each fruit and multiplies its respective price and quantity


           cost = quantity_list[key] * price_list[key]
           # basically multipling the price and quantity of each fruit, as the fruits for both lists are in the same order


           # using [key], basically lets me retrieve the value associated with that key
           # [value] IS NOT A THING!! [key] is the correct term
           total_cost += cost


   print("total cost = ", total_cost)
   return total_cost # for testing purposes




def cost_of_fruits(fruit, quantity):
   for key in price_list.keys():
       if key == fruit:
           cost = quantity*price_list[key]
           break


   print("cost of", quantity, fruit, "=", cost)
   return cost # for testing purposes




def main():


   cost_of_fruits('apple', 10)
   total_cost_shopping()




if __name__ == "__main__":
   main()
testing functions


from lab2 import bmi


def test_total_cost_shopping():
   height = 1.73
   weight = 50


   result = bmi.calculate_bmi(height, weight)


   assert result == -1





def test_cost_of_fruit():
   height = 1.73
   weight = 70


   result = bmi.calculate_bmi(height, weight)


   assert result == 0





import employee_info


def test_get_employees_by_age_range():
   age_lower_limit = 20
   age_upper_limit = 30 # age cannot be either 20 or 30


   result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)


   assert result == [
       {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
       {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
   ]





def test_calculate_average_salary():
   result = employee_info.calculate_average_salary()


   assert result == 60166.666666666664





def test_get_employees_by_dept():
   department = 'Sales'


   result = employee_info.get_employees_by_dept(department)


   assert result == [
       {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
       {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
   ]


import Lab3


print("Test_Lab3")


# The “assert” statement basically returns a Boolean value True or False of the
# condition asserted or checked is True or False.


def test_bubble_sort_ascending():
   result = []
   input_arr = [64, 34, 25, 12, 22, 11, 90]
   test_arr = [11, 12, 22, 25, 34, 64, 90]


   result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)


   assert (result == test_arr)





def test_bubble_sort_descending():
   result = []
   input_arr = [64, 34, 25, 12, 22, 11, 90]
   test_arr = [90, 64, 34, 25, 22, 12, 11]


   result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)


   assert (result == test_arr)





def test_bubble_sort_large_input():
   input_arr = [64, 34, 25, 12, 22, 11, 90, 50, 70, 80, 100]  # Input with 11 numbers


   result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)


   assert result == 1
def test_bubble_sort_empty_input():
   input_arr = []  # Empty input list


   result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)


   assert result == 0





def test_bubble_sort_non_integer_input():
   input_arr = [64, 34, 25, 12, "22", 11, 90]  # Input with a non-integer value ("22")


   result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)


   assert result == 2





def test_bubble_sort_invalid():
   result = []
   input_arr = [64, 34, 25, 12, 22, 11, 90]


   result = Lab3.bubble_sort(input_arr, 3)


   assert (result == [])


import price_info


def test_total_cost_shopping():
   total_cost = 46.75


   result = price_info.total_cost_shopping()
   assert result == total_cost





def test_cost_of_fruits():
   fruit = 'apple'
   quantity = 5


   result = price_info.cost_of_fruits(fruit, quantity)
   assert result == 6.00
