
# PART A

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

## 5 (C#) 
```
using System;

class Program
{
    static void Main(string[] args)
    {
        int number = int.MaxValue;
        number += 1;
        Console.WriteLine("The incremented value is: " + number);
    }
}
```
1. Which variable is incorrect?
    - number
2. Why is it incorrect or insecure?
    - C languages need integer length to be explicitly declared. number is set at the maximum value of an int datatype which is the maximum values of a 32-bit integer or 2,147,483,647. When int is incremented by one in the program the number would become 2,147,483,648 which in greater than what an int can hold at 32-bits. This program would still compile and but cause an integer overflow runtime error. The number would actually ***decrement*** to -2,147,483,648 instead of incrementing 2,147,483,648. Which could cause absolute chaos in an application.
3. Code refactor
```
using System.
class Program
{
    static void Main(string[] args)
    {
        long number = int.MaxValue;
        number += 1;
        Console.WriteLine("The incremented value is: " + number);
    }
}
```
4. Why refactor corrects issue. 
    by assigning the long datatype to number the program can safely increment to 2,147,483,648 with out causing an integer overflow bug at run time.

# Part B

## 1 (Java)

```
import java.util.regex.*;

public class URLExtractor {
    public static void main(String[] args) {
        String text = "Visit my website at http://www.url example.com";
        String regex = "https?://.+";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            System.out.println("URL: " + matcher.group());
        }
    }
}
```
1. Identify the regular expression code.
    - the regex is https?://.+
2. Explain why the regex used is incorrect or answer the questions provided.
    - the regex in this example allows http or https,followed by "://" and lastly followed by 1 or more chars. This regex is a little too permissive since it allows one or more of any character including whitespace at the end of the expression.
3. Correct the code.
```https?://\\S+```
4. Explain why the corrected code fixes the issue.
    - This allows for https or http followed by :// but it restricts the match to one or more non-whitespace characters. This prevents more words added after the URL

## 2 (Java)

```
import java.util.regex.*;
import java.util.Scanner;

public class ZipCode {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            Pattern zipPattern = Pattern.compile("^\\d{5}(\\d{4})?$");
            System.out.println("Enter a Zipcode as xxxxx or xxxxx-xxxx: ");
            String zipCode = scanner.nextLine();

            if ( !zipPattern.matcher(zipCode).matches() ) {
                System.out.println("Incorrect Zipcode");
            }
            else {
                System.out.println("Correct Zip");
            }
        }
    }
}
```
1. Identify the regular expression code.
    - ^\\d{5}(\\d{4})?$
2. Explain why the regex used is incorrect or answer the questions provided.
    - This regex does not allow a dash between the 5-digit zip code block and the optional 4-digit zipcode block. 
3. Correct the code.
```
^\\d{5}(-\\d{4})?$
```
4. Explain why the corrected code fixes the issue.
    - This corrects the issue by allowing a dash between the 5-digit block and the optional 4-digit block. This is done by placing the dash inside the optional expression.

## 3 (HTML)
```
<!DOCTYPE html>
<!-- HTML Form to validate a phone number --> 
<html>
<head>
<style>
    input:invalid {border: red solid 3px;}
</style>
</head>

<p>
  <label>
    Enter your phone number in the format 123-456-7890
    <input
      name="tel1"
      type="tel"
      pattern="[0-9]{4}"
      placeholder="###"
      aria-label="3-digit area code"
      size="2" 
    />
    -
    <input
      name="tel2"
      type="tel"
      pattern="\d{3}"
      placeholder="###"
      aria-label="3-digit prefix"
      size="2" 
    />
    -
    <input
      name="tel3"
      type="tel"
      pattern="\D{4}"
      placeholder="####"
      aria-label="4-digit number"
      size="3" 
    />
  </label>
</p>
</html>
```
1. Identify the regular expression code.
    - [0-9]{4}, \d{3}, \D{4}
2. Explain why the regex used is incorrect or answer the questions provided.
    - [0-9]{4}, this code allows 4 digits but only 3 are needed
    - \d{3}, this code is fine, but HTML field size is set to 2
    - \D{4} this code allows non-digit characters, and the HTML field size is too small
3. Correct the code.
```
<!DOCTYPE html>
<!-- HTML Form to validate a phone number --> 
<html>
<head>
<style>
    input:invalid {border: red solid 3px;}
</style>
</head>
<body> <!-- body tag missing in original code -->
<p>
  <label>
    Enter your phone number in the format 123-456-7890
    <input
      name="tel1"
      type="tel"
      pattern="/d{3}"
      placeholder="###"
      aria-label="3-digit area code"
      size="3" 
    />
    -
    <input
      name="tel2"
      type="tel"
      pattern="\d{3}"
      placeholder="###"
      aria-label="3-digit prefix"
      size="3" 
    />
    -
    <input
      name="tel3"
      type="tel"
      pattern="\d{4}"
      placeholder="####"
      aria-label="4-digit number"
      size="4" 
    />
  </label>
</p>
</body>
</html>
```
4. Explain why the corrected code fixes the issue.
    - This refactors the original code by ensuring all regex accept the correct quantity of digits and the field sizes matched the expected input lengths for a typical phone number. Additionally, the <body> tags were missing in the HTML. 

## 4 (Python)

```
import re

def validate_date(date_str):
    pattern = r"^(1[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])/\w{4}$"
    
    # Check if the date matches the pattern
    if re.match(pattern, date_str):
        print("Valid date format.")
    else:
        print("Invalid date format. Please enter the date in the format MM/DD/YYYY.")

date_input = input("Please enter a date in the format MM/DD/YYYY: ")
validate_date(date_input)
```

1. Identify the regular expression code.
    - ^(1[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])/\w{4}$
2. Explain why the regex used is incorrect or answer the questions provided.
    - (1[1-9]|1[0-2]), this regex is supposed to match a MM date, however both digits must lead with 1.
    - /(0[1-9][12][0-9]|3[01]) this expression matches 01-31, it functions as expected.
    - /\w{4}$ this expression matches chars instead of digits. 
3. Correct the code.
```
^(0[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])/\d{4}$
```
4. Explain why the corrected code fixes the issue.
    - this implementation allows the leading MM digit to be 0, and does not allow the YYYY value to contain anything but digits. 

## 5 (Python)

```
import re

def validate_filename(filename):
    # Regular expression pattern for a filename with an extension
    pattern = r"^[\s]+\.(java,py,cs,txt)$"
    
    # Check if the filename matches the pattern
    if re.match(pattern, filename):
        print("Valid filename format.")
    else:
        print("Invalid filename format. Please enter a filename with an extension.")

filename_input = input("Please enter a filename containing code with one of the following extensions: java, py, cs, txt")
validate_filename(filename_input)
```

1. Identify the regular expression code.
    - ^[\s]+\.(java,py,cs,txt)$
2. Explain why the regex used is incorrect or answer the questions provided.
    - This expression allows whitespaces in a filepath which is problematic. There is a syntax error in the () commas do not delimit choices in regex, | does that.
3. Correct the code.
```
^[\S]+\.(java|py|cs|txt)$
```
4. Explain why the corrected code fixes the issue.
    - The corrected expression requires non-white space chars and correctly delimits choice matches. 


