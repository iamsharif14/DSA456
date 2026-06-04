# Author: Shariful Islam	
# Student Number: 106975246


# Function 1 Analysis

def function1(number):
    total = 0

    for i in range(number):
        x = i + 1
        total += x * x

    return total

The loop runs 'number' times.

The line (total += x * x) executes 'number' times and actually adds the squares of all numbers from 1 to the specified number

Therefore the running time grows linearly with the input size.

**Time Complexity: O(n)**




# Function 2 Analysis


def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6


This function does not have any loops. So It only runs one time and performs one arithmetic formula.

**Time Complexity: O(1)**



# Function 3 Analysis


def function3(list):
    n = len(list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp

The outer loop runs 'n - 1' times.

The inner loop runs { (n - 1) + (n - 2) + ... + 1 } times, which we can write as n(n - 1)/2 operations. After simplifying, we get (n²-n)/2

After removing constants and lower-order terms,

**Time Complexity: O(n²)**



# Function 4 Analysis

def function4(number):
    total = 1

    for i in range(1, number):
        total *= i + 1

    return total

The loop runs number - 1 times which is actually a factorial formula. 

The work grows linearly with the input size.

**Time Complexity: O(n)**
