# Python Data Types, Variables, and String Formatting

## Introduction

Welcome back! So far, we have covered the absolute basics:

1. What Python is
2. How to run Python code
3. How to print text to your screen

In this lesson, we are leveling up. We will explore:

- How to store values using **variables**
- How those values are represented under the hood using **data types**
- What kinds of **operations** we can perform on them
- How to format and print output dynamically

---

## Data: What Is Your Type?

Let’s start with a tiny bit of computer science reality.

> [!quote] **\"Computers are just rocks we tricked into thinking.\"**

As silly as that sounds, it is fundamentally true. Computers only do exactly what we tell them to do. The machine is not doing the hard thinking for us—we are the ones breaking a problem into small, precise steps that the computer can follow.

That translation from human thought into machine logic is often what makes programming feel intimidating at first. The good news is that Python gives us tools to make that process much easier.

You have probably heard of **binary**—a number system that uses only two digits: `0` and `1`. Collections of bits are how computers represent and process all information.

> [!question] **Core question:** How do we use only zeros and ones to represent things like text, numbers, images, and meaning?

We do it using **data types**. Data types categorize data so the computer knows what it represents, what rules apply to it, and what operations can be performed on it.

### Common Python Data Types

- **`bool` (Boolean):** Truth values—either `True` or `False`
- **`int` (Integer):** Whole numbers without decimals, such as `-1`, `0`, or `42`
- **`float` (Floating-point):** Numbers with decimals, such as `3.14`, `-0.5`, or `2.0`
- **`str` (String):** Text wrapped in quotes, such as `"hello"` or `"Python 3"`

```python
# A quick look at integers and floats in action
cool_int = 5
print(cool_int)

my_float = 2.0
print(my_float)
```

---

## Working with Variables

### Setting Variables

To assign a value to a variable, use the assignment operator (`=`):

```python
cool_var = 21
```

An expression such as `cool_var + 3` evaluates to `24`, but it **does not** permanently change the value stored in `cool_var`.

If you want to update the variable itself, assign the result back to it:

```python
# Both of these lines achieve the same result
cool_var = cool_var + 3
cool_var += 3  # Shortcut syntax
```

### Casting Types

If you have a value of one type and need to convert it to another, use **casting**. To cast a value, wrap it in the target type function:

```python
# Convert a string to an integer
cool_var = "2"
cool_var = int(cool_var)  # cool_var is now the integer 2
```

To check what type Python thinks a value is, use `type()`:

```python
print(type(cool_var))  # Outputs: <class 'int'>
```

You can also convert numbers into strings:

```python
# Convert an integer to a string
cool_var = 2
cool_var = str(cool_var)  # cool_var is now the string "2"
```

### What Happens When Casting Fails?

What if we run this?

```python
cool_var = "apples"
cool_var = int(cool_var)
```

Python raises a `ValueError` because there is no logical way to convert the text `"apples"` into a base-10 integer.

### Predict the Outcome

What happens in these cases?

- `str(True)` → `"True"`
- `bool("False")` → `True` because the string is not empty
- `int(5.99)` → `5` because Python truncates the decimal part instead of rounding

> [!thm] **Rule of thumb:** Convert one step at a time.
>
> If you have a string containing a decimal like `"3.14"`, trying to cast it directly with `int("3.14")` will fail. Instead, convert it in stages:

```python
cool_var = "3.14"
cool_var = float(cool_var)  # Step 1: Turn string into float (3.14)
cool_var = int(cool_var)    # Step 2: Turn float into int (3)
```

---

## Operations

By combining data types with **operators**, you can manipulate data in many useful ways.

| Operation | Operator | Example | Result |
| --- | --- | --- | --- |
| Addition | `+` | `2 + 3` | `5` |
| String concatenation | `+` | `"hi " + "there"` | `"hi there"` |
| Multiplication | `*` | `100 * 4` | `400` |
| String repetition | `*` | `"a" * 5` | `"aaaaa"` |
| Subtraction | `-` | `10 - 7` | `3` |
| Division | `/` | `70 / 7` | `10.0` |
| Integer division | `//` | `71 // 7` | `10` |
| Modulus | `%` | `80 % 7` | `3` |
| Exponent | `**` | `2 ** 5` | `32` |

> [!thm] **Important:** Regular division (`/`) always returns a `float`, even when the answer is a whole number.

---

## Printing Multiple Items

The `print()` function is flexible and can accept multiple arguments separated by commas:

```python
cool_int = 10
print(True, "nice string", cool_int)
# Output: True nice string 10
```

Python automatically inserts a single space between each item.

### Controlling the Spaces

Suppose you want this exact output:

```text
I am at 100% Python!!!
```

If you write:

```python
percent = 100
print("I am at", percent, "% Python!!!")
```

You get:

```text
I am at 100 % Python!!!
```

That extra space before `%` may not be what you want.

Here are three clean ways to fix it.

#### 1. Cast and Concatenate

```python
print("I am at " + str(percent) + "% Python!!!")
```

#### 2. Change the Separator with `sep`

```python
print("I am at ", percent, "% Python!!!", sep="")
```

#### 3. Use an F-string (Recommended)

```python
print(f"I am at {percent}% Python!!!")
```

F-strings are usually the cleanest and most readable option.

---

## Escape Characters

How do you print special characters that would otherwise confuse Python—like quotation marks inside a string, tabs, or line breaks? Use **escape characters** by placing a backslash (`\`) before them.

| Escape Sequence | Meaning |
| --- | --- |
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Literal backslash |
| `\'` | Literal single quote |
| `\"` | Literal double quote |

```python
print("Line one\nLine two")
print("They said, \"Python is awesome!\"")
```

---

## User Input and Expressions

### The `input()` Function

To gather information from a user through the keyboard, use `input()`. This function pauses the program and waits for the user to type something and press Enter.

> [!thm] **Crucial rule:** `input()` **always** returns a string (`str`), even if the user types digits.

```python
user_response = input("Type something: ")
print(f"You wrote: {user_response}")
```

### Understanding Expressions

In computer science, an **expression** is anything that evaluates to a single value.

For example:

```python
my_input = input()
```

- **Right-hand side (RHS):** `input()` is an expression that evaluates to a string
- **Left-hand side (LHS):** `my_input` stores that resulting value

---

## Clean Code: Comments and PEP 8

### Writing Comments

Comments let you leave notes for humans without affecting how the program runs.

- **Single-line comments:** Start with `#`
- **Multi-line comments / docstrings:** Enclosed in triple quotes (`"""`), often used at the top of files or functions

```python
"""
Module: calculator.py
Author: Student Name
Description: A simple script to add user numbers together.
"""

# This line asks for user data
age = int(input("Age? "))
```

### PEP 8 Style Guide

**PEP 8** is Python’s official style guide. Following it helps your code look professional and makes it easier for others to read.

- **Indentation:** Use **spaces**, not hard tabs
- **Standard indentation level:** 4 spaces per block
- **Naming convention:** Use `snake_case` for variables and functions

**Good examples:**

- `user_bonus_points`
- `calculate_total`

**Avoid:**

- `userBonusPoints` (camelCase)
- `UserBonusPoints` (PascalCase)

---

## Real-World Practice

### Worked Example: Convert to Seconds

**Problem:** Write a program called `seconds.py` that asks the user for a duration in days, hours, minutes, and seconds. Then calculate and display the total number of seconds.

Assume all inputs are valid integers.

#### Expected Output

```text
How many days have elapsed? 3
How many additional hours have elapsed? 9
How many additional minutes have elapsed? 12
How many additional seconds have elapsed? 33
The total amount of time elapsed is 292353 seconds
```

> [!pf]- Solution
> ```python
> # Ask the user for input and cast to integers immediately
> days = int(input("How many days have elapsed? "))
> hours = int(input("How many additional hours have elapsed? "))
> minutes = int(input("How many additional minutes have elapsed? "))
> seconds = int(input("How many additional seconds have elapsed? "))
> 
> # Convert everything into seconds
> total_seconds = seconds
> total_seconds += minutes * 60
> total_seconds += hours * 60 * 60
> total_seconds += days * 24 * 60 * 60
> 
> # Display the result using an f-string
> print(f"The total amount of time elapsed is {total_seconds} seconds")
> ```
> 
> ---
> 
> ### Let’s Code: Mini Dice Roll Game
> 
> Let’s tie several concepts together in one practical script. This example uses Python’s `random` module to simulate rolling a 20-sided die.
> 
> ```python
> import random
> 
> print("You are working on your homework late on a Friday night. Will you succeed?")
> 
> # Set up game constants
> dice_sides = 20
> dc = 10  # Difficulty Class to pass the check
> 
> # Simulate a random dice roll between 1 and 20
> roll = random.randint(1, dice_sides)
> 
> # Gather user input and add character bonus
> hero_bonus = int(input("What is your character proficiency bonus? "))
> combined_roll = roll + hero_bonus
> 
> # Display the game state
> print(f"Combined Roll: {combined_roll} (Base Roll: {roll} + Bonus: {hero_bonus}) | DC to beat: {dc}")
> ```
> 
> ### Why This Example Matters
> 
> This short program combines several core ideas:
> 
> - Variables
> - Integers
> - User input
> - Type casting with `int()`
> - Arithmetic operations
> - String formatting with f-strings
> - Importing a module
> 
> If you understand this example, you are already starting to build real programs.
