# Module 7: Logic and Conditionals

Programming involves writing instructions for a computer to execute. However, what allows computer programs to be most useful is when they are able to _decide which_ instructions instructions to execute based on a particular situation. This is refered to as <a href="https://en.wikipedia.org/wiki/Branch_(computer_science)">code branching</a>, and is used to shape the [flow of control ](https://en.wikipedia.org/wiki/Control_flow) of the computer code. In this module, you will learn how to utilize **conditional statements** in order to include control flow in your Python scripts.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**

- [Resources](#resources)
- [Booleans](#booleans)
  - [Boolean Operators](#boolean-operators)
- [Conditional Statements](#conditional-statements)
  - [Designing Conditions](#designing-conditions)
  - [Modules vs. Scripts](#modules-vs-scripts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Resources
- [Conditional Execution (Downey)](https://books.trinket.io/pfe/03-conditional.html)
- [Conditionals (Severance)](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)
- [Flow Control (Sweigart)](https://automatetheboringstuff.com/chapter2/) (first half)


## Booleans
In addition to the basic data types `int`, `float`, and `str`, Python supports a _logical_ data type called a **Boolean** (class `bool`). A boolean represents "yes-or-no" data, and can be exactly one of two values: `True` or `False` (note the capitalization). Importantly, these **are not** the Strings `"True"` and `"False"`; boolean values are a different type!

```python
type(True)    # <class 'bool'>
type("True")  # <class 'str'>
type(true)    # NameError: name 'true' is not defined
              # e.g., no variable called `true`!
```

- _Fun fact_: logical values are called "booleans" after mathematician and logician [George Boole](https://en.wikipedia.org/wiki/George_Boole), who invented many of the rules and uses of this construction (called [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)).

Boolean values are most commonly the result of applying a **relational operator** (also called a **comparison operator**) to some other data type. Comparison operators are used to compare values and include: `<` (less than), `>` (greater than), `<=` (less-than-or-equal, written as read), `>=` (greater-than-or-equal, written as read), `==` (equal), and `!=` (not-equal).

```python
x = 3
y = 3.15

# compare numbers
x > y  # returns logical value False ("x is bigger than y" is a False statement)
y != x  # returns logical value True ("y is not-equal to x" is a True statement)

# compare x to pi (built-in variable)
y == math.pi  # returns logical value False

# compare strings (based on alphabetical ordering)
"cat" > "dog"  # returns False
```

- **Important** `==` (two equals signs) is a comparison operator, but `=` (one equals sign) is the assignment operator!

Note that boolean variables should be named as _statements of truth_. Use words such as `is` in the variable name:

```python
is_early = True
is_sleeping = False
needs_coffee = True
```

### Boolean Operators
In addition, boolean values support their own operators (called **logical operators** or **boolean operators**). These operators are applied to boolean values and produce boolean values, and allow you to make more complex _boolean expressions_:

- **`and`** (conjunction) produces `True` if both of the operands are `True`, and `False` otherwise
- **`or`** (disjunction) produces `True` if _either_ of the operands are `True`, and `False` otherwise
- **`not`** (negation) is a [unary operator](https://en.wikipedia.org/wiki/Unary_operation) that produces `True` if the operand is `False`, and `False` otherwise

```python
x = 3.1
y = 3.2

# Assign bool values to variables
x_less_than_pi = x < math.pi  # True
y_less_than_pi = y < math.pi  # False

# boolean operators
x_less_than_pi and y_less_than_pi  # False
x_less_than_pi or y_less_than_pi  # True

# this works because Python is amazing
x < math.pi < y  # True


pet = "dog"

# it is NOT the case that pet is "cat"
not pet == "cat"  # True

# pet is "cat" OR "dog"
pet == "cat" or pet == "dog"  # True

# this doesn't work (operators are applied left-to-right; check the types!)
# see "short-circuiting" below, as well as http://stackoverflow.com/a/19213583
pet == "cat" or "dog"  # "dog"
```

Because boolean expressions produce _more_ booleans, it is possible to combine these into complex logical expressions:

```python
# given two booleans P and Q
P = True
Q = False

P and not Q  # True
not P and Q  # False
not (P and Q)  # True
(not P) or (not Q)  # True
```

The last two expressions in the above example are equivalent logical statements for _any_ combination of values for `P` and `Q`, what is known as [De Morgan's Laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws). Indeed, many logical statements can be written in multiple equivalent ways.

Finally, note that when using an `and` operator, Python will **short-circuit** the second operand and never evaluate it if the first is found to be `False` (after all, if the first operand isn't `True` there is no way for the entire `and` expression to be!)

```python
x = 2
y = 0
x == 2 and x/y > 1  # ZeroDivisionError: division by zero
x == 3 and x/y > 1  # no error (short-circuited)

# Use a "guardian expression" (make sure y is not 0)
# to avoid any errors
y != 0 and x/y > 1  # no error (short-circuited)
```

- The reason this works is because Python interpreter reads the expression `P and Q`, it produces `Q` if `P` is `True`, and `P` otherwise. This is because if `P` is `True`, then the overall truth of the expression is dependent entirely on `Q` (and thus that can just be returned). Similarly, if `P` is `False`, then the whole statement is false (equivalent to `P`!)


## Conditional Statements
One of the primary uses of Boolean values (and the _boolean expressions_ that produce them) is to control the flow of execution in a program (e.g., what lines of code get run in what order). While we can use _functions_ are able to organization instructions, we can also have our program decide which set of instructions to execute based on a set of conditions. These deciisions are specified using **conditional statements**.

In an abstract sense, an conditional statement is saying:

```
IF something is true
  do some lines of code
OTHERWISE
  do some other lines of code
```

In Python, we write these conditional statements using the keywords **`if`** and **`else`** and the following syntax:

```python
if condition:
    # lines of code to run if condition is True
else:
    # lines of code to run if condition is False
```

The **`condition`** can be any Boolean value (or any expression that evaluates to a boolean value). Both the **`if`** statement and **`else`** clause are followed by a colon **`:`** and a **block**, which is a set of _indented_ statements to run (similar to the blocks used in functions). It is also possible to _omit_ the `else` statement and its block if there are no instructions to run in the "otherwise" situation:

```r
porridge_temp = 115  # temperature in degrees F

if porridge_temp > 120:
    print("This porridge is too hot!")
else:
    print("This porridge is NOT too hot!")

too_cold = porridge_temp < 70  # a boolean variable
if too_cold:
  print("This porridge is too cold!")

# This line is outside the block, so is not part of the conditional
# (it will always be executed)
print("Time for a nap!")
```

**Blocks** can themselves contain _nested_ conditional statements, allowing for more complex decision making. Nested `if` statements are indented twice (8 spaces or 2 tabs). There is no limit to how many "levels" you can nest; just increase the indentation each time.

```python
# nesting example
if outside_temperature < 60:
    print("Wear a jacket")
else:
    if outside_temperature > 90:
        print("Wear sunscreen")
    else:
        if outside_temperature == 72:
            print("Perfect weather!")
        else:
            print("Wear a t-shirt")
```

Note that this form is nesting is also how we you can use conditionals inside of functions:

```python
def flip(coin_is_heads):
    if coin_is_heads:
        print("Heads you win!")
    else:
        print("Tails you lose")
```

If you consider the above nesting example's logic carefully, you'll notice that many of the "branches" are **mutually exclusive**: that is, the code will choose only 1 of 4 different clothing suggestions to print. This can be written in a cleaner format by using an **`elif`** ("else if") clause:

```python
if outside_temperature < 60:
    print("Wear a jacket")
elif outside_temperature > 90:
    print("Wear sunscreen")
elif outside_temperature == 72:
    print("Perfect weather!")
else:
    print("Wear a t-shirt")
```

In this situation, the Python interpreter will perform the following logic:

1. It first checks the `if` statement's condition. If that is `True`, then that branch is executed and the rest of the clauses are skipped.
2. It then checks each `elif` clause's condition _in order_. If one of them is `True`, then that branch is executed and the rest of the clauses are skipped.
3. If _none_ of the `elif` clauses are `True`, then (and only then!) the `else` block is executed.

This _ordering_ is important, particularly if the conditions are not in fact mutually exclusive:

```python
if porridge_temp < 120:
    print("This porridge is not too hot!")
elif porridge_temp < 70:
  # unreachable statement! the condition will never be both checked and True
    print("This porridge is too cold!")

# contrast with:
if porridge_temp < 120:
    print("This porridge is not too hot!")
if porridge_temp < 70:  # a second if statement, unrelated to the first
    print("This porridge is too cold!")
# both print statements will execute for `porridge_temp = 50`
```

See also the resources listed at the top of the module for explanations with logical diagrams and flowcharts.


### Designing Conditions
Relational operators all have logical opposites (e.g., `==` is the opposite of `!=`; `<=` is the opposite of `>`), and boolean expressions can include negation. This means that there are many different ways to write conditional statements that are _logically equivalent_:

```python
# these two statements are equivalent
if x > 3:
    print("big X!")

if 3 < x:
    print("big X!")
```

- The second example is known as a [Yoda condition](https://en.wikipedia.org/wiki/Yoda_conditions); in Python you should use the former.

Thus you should follow the below guidelines when writing conditionals. These produce more "idiomatic" code which is cleaner and easier to read, as well as less likely to cause errors.

- Avoid checks for mutually exclusive conditions with an `if` and `elif`. Use the `else` clause instead!

  ```python
  # Do not do this!
  if temperature < 50:
      print("It is cold")
  elif temperature >= 50:  # unnecessary condition
      print("It is not cold")

  # Do this instead!
  if temperature < 50:
      print("It is cold")
  else:
      print("It is not cold")
  ```

- Avoid creating redundant boolean expressions by comparing boolean values to `True`. Instead, use an effectively named variable.

  ```python
  # Do not do this!
  if is_raining == True:  # unnecessary comparison
      print("It is raining!")

  # Do this instead!
  if is_raining:  # condition is already a boolean!
      print("It is raining!")
  ```

  Note that this gets trickier when trying to check for `False` values. Consider the following equivalent conditions:

  ```python
  # I believe this is the cleanest option, as it reads closet to English
  if not is_raining:
      print("It is not raining!")

  # This is an acceptable equivalent, but prefer the first option
  if is_raining == False
      print("It is not raining!")

  # Use one of the above options instead
  if is_raining != True
      print("It is not raining!")

  # This can be confusing unless your logic is explicitly based around the
  # ABSENCE of some condition
  if is_not_raining:
      print("It is not raining!")
  ```

Overall, try to develop the simplest, most straightforward conditions you can. This will make sure that you are able to think clearly about the program's control flow, and help to clarify your own thinking about the program's logic.

### Modules vs. Scripts
As discussed in [module5](../../module5-python-basics), it is possible to define Python variables and functoins in `.py` files, which can be run as stand-alone scripts. However, these files can also be [imported as modules](https://docs.python.org/3/tutorial/modules.html), allowing you to access their variables and functions from another script. Thus all Python scripts have two "modes": they can be used as executable scripts (run with the `python` command at the command-line), or they can be imported as modules (libraries of variables and functions, using the `import` keyword in the script).

When the `.py` script is run as an executable [top-level script](https://docs.python.org/3/library/__main__.html), we often want to perform special instructions (e.g., call specific functions, [prompt for user input](https://docs.python.org/3/library/functions.html#input), etc). We can use a special _environmental_ variable called `__name__` to determine whether this is the "main" script that is being run, and `if` so execute those instructions:


```python
if __name__ == "__main__":
    # execute only if run as a script
    print("This is run as a script, not a module!")
```

- The `__` in the variable names and values are a special naming convention used to indicate _to the human_ that these values are **internal** to the Python language and so have special meaning. They are otherwise normal variables names
