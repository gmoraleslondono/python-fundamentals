# Python - Fundamentals

## Class 1 - 08-09-2026

## Console

```python
print("Hello, World!")
```

## Operations

```python
print(2 + 3)   # 5
print(2 - 3)   # -1
print(2 * 3)   # 6
print(2 / 3)   # 0.6666666666666666
print(2 // 3)  # 0
print(2 ** 3)  # 8
print(2 % 3)   # 2
```

## Converting types

```python
x = 1
y = 0
print(bool(x))  # True
print(bool(y))  # False

z = ""
print(bool(z))  # False
```

## String

```python
text = "python"
print(len(text))  # 6
print(text[0])    # p
print(text[-1])   # n
print(text[-2])   # o
```

## Slicing

```python
text = "python"
print(text[0:3])  # pyt
print(text[3:6])  # hon

text = "abcdefghij"
print(text[::2])   # acegi - step every other letter
print(text[::-1])  # jihgfedcba - revert the string
```

## Immutability

```python
word = "python"
word[0] = "J"  # this will throw an error because strings are immutable
print(word)    # python

word = "python"
word = "J" + word[1:]
print(word)  # Jython
```

## Trim

```python
message = "   Hello, World!   "
print(message.strip())   # Hello, World! - removes whitespace from both ends
print(message.lstrip())  # Hello, World!    - removes whitespace from the left end
print(message.rstrip())  #    Hello, World! - removes whitespace from the right end

message = "Hello, World!"
print(message.upper())  # HELLO, WORLD! - converts to uppercase
print(message.lower())  # hello, world! - converts to lowercase

message = "Python is fun"
print(message.replace("fun", "powerful"))  # Python is powerful - replaces "fun" with "powerful"

data = "apple, banana, orange"
print(data.split(", "))  # ['apple', 'banana', 'orange'] - splits the string into a list based on the delimiter ", "
```
