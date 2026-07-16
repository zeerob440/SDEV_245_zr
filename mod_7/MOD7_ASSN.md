
# PART A

FIXME: format. Delete when part a complete

1. Which variable is incorrect?
2. Why is it incorrect or insecure?
3. Code refactor
4. Why refactor corrects issue. 

## 1 (Java) 

```
public class Exercise1 {

  public static void main(String[] args) {

      z = 24;
      System.out.println("The value of z is: " + z);
  }
}

```
1. Which variable is incorrect?
    -z
2. Why is it incorrect or insecure?
    - z is incorrectly declared. Java expects vars to be declared with types. This code would create a compile time error, because according to Java, z does not exist. This is similar to a Python function a function cannot be invoked before it is declared. 
3. Code Refactor
```
public class Exercise1 {

  public static void main(String[] args) {

      int z = 24;
      System.out.println("The value of z is: " + z);
  }
}
```
4. Why refactor corrects issue. 
    - this refactor corrects z's declaration. This code would run without compile time error.

## 2 (Java)

```
public class Exercise2 {

    public static void main(String[] args) {

      String y = 10;
      System.out.println("The value of y is: " + y);
  }
}

```
1. Which variable is incorrect?
    - y
2. Why is it incorrect or insecure?
    - The type is mismatched. y is an integer but declared as a string. This would cause a compile time error. 
3. Code refactor
```
public class Exercise2 {

    public static void main(String[] args) {

      int y = 10;
      System.out.println("The value of y is: " + y);
  }
}
```
4. Why refactor corrects issue.
    - The refactor corrects the issue because the type now matches the value. This code would execute without a compile time error. 

## 3 (Python)

```
# Output the sum of an array's values
items = [10, 20, 30, 40, 50]

def sum_array(arr):
    total = 0

    for i in range(len(arr)):
        total += arr[i]
    return total

result = sum_array(items)

print("Sum of elements in the array:", result)
```

1. Which variable is incorrect?
    - I'm not certain if it is really incorrect, or if is not explicit enough. 
2. Why is it incorrect or insecure?
    - I can't detect an issue with the code. I supposed to be perfectly correct, arrays are called lists in Python. So I would change the code base to reflect that. I could add type hints, make the loop more legible, and explicitly force integers in the vars. 

3. Code refactor
```
# Output the sum of a list's values
items: list = [10, 20, 30, 40, 50]

def sum_list(a_list_of_integers_goes_here):

    total: int = int(0)

    for item in a_list_of_integers_goes_here:
        total += item
    return total

result: int = int(sum_list(items))

print("Sum of elements in the list:", result)

```
4. Why refactor corrects issue.
    - I'm not sure if I would call it a correction. In this refactor the code is more explicit. It includes type hints, explicitly enforces int types in each variable with type conversion, and it calls arrays lists as is the Pythonic convention. The input is hard coded, so I cannot determine if list is intended to be a constant or if user input will populate list at some point in the future. If there was anything wrong with the original code it would only be incorrect if list is intended to be populated by user input at some point in its future development. 

## 4 (Python)

```
# Simple Python program to calculate the sum of a set of numbers supplied by the user

integer total = 1
integer num_count = 1
float num = 1

num_count = int(input("How many numbers do you want to add? "))

for i in range(num_count):
    num = float(input("Enter number {}: ".format(i+1)))
    
    total += num

print("The sum of the numbers you entered is:", total)
```

1. Which variable is incorrect?
    - total, num_count, and num
2. Why is it incorrect or insecure?
    as written this code will produce syntax errors. This code will not enter runtime. The problem is because total, num_count, and num are incorrectly declared. The code itself produces an off-by-one error, however due to vague documentation, I cannot determine if this was the developer intent or if it is truly an error. The program also adds integers but returns a float. I'm not certain if this was intentional because of vague documentation.    
3. Code refactor
```
# Simple Python program to calculate the sum of a set of numbers supplied by the user
# refactored total to start with 0, to remove off-by-one error. uncertain if that was intended. 
total: int = int(0)
num_count: int = int(1)
num: float = float(1.0)

num_count = int(input("How many numbers do you want to add? "))

for number in range(num_count):
    num: float = float(input("Enter number {}: ".format(number + 1)))
    
    total += num

print("The sum of the numbers you entered is:", total)
```
4. Why refactor corrects issue. 
    - This refactor properly declares the three undeclared variable which prevents the SyntaxError at run time. Type hints are added for legibility and type conversions are enforced throughout. 
