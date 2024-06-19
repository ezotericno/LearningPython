# Strings: A review
- The `len()` function, returns the number of characters contained within the string.
- Multiline strings are done with triple quotation marks.
- strings can be contatenated and replicated.
  - Example:
```python
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
```
OUTPUT: 
```
ab
ba
aaaaa
bbbb
```
- The `ord()` (ordinal) function, prints out the character ASCII/UNICODE code point value.
- On the other hand the `chr()` function is used to print a character from an ASCII/UNICODE code point.
___
# Strings as sequences
- Strings are not lists, but they can act like lists in certain cases

## Indexing
- you can access characters inside of strings by using indexing, example below.
```python
# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
```
OUTPUT:
```
s i l l y   w a l k s
```
- Iterating through strings also works.
EXMAPLE CODE:
```python
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
```
OUTPUT:
```
s i l l y   w a l k s
```
___
## Slices
- Below is an example of how slicing works on strings.
EXAMPLE:
```python
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
```
OUTPUT:
```
bd
efg
abd
e
e
adf
beg
```
___
## The in and not in operators
- The `in` and `not in` operators checks if the left inputted arg is inside the string.
___
## Pythong strings are immutable.
- The example code below will not work.
```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]
```
- It would only delete the string as a whole, not just the first character as instructed.
- You also cannot use the `append()` method to expand the string.
- The former also means the `insert()` method will also fail.
- Taking all of this into account, there still exists ways to operate on strings. Example below:
```python
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
```
OUTPUT:
`abcdefghijklmnopqrstuvwxyz`
___
## Operations on strings: continued
- The `min()` function finds the minimum element of the sequence passed as an argument, the string cannot be empty for this to work.
- The output is usually based on the characters position on the ASCII table. 
- EXAMPLE:
```python
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))
```
OUTPUT:
```
A
[ ]
0
```
- The `max()` function does the oposite of the `min()` function.
- The `index()` method searches the string to find the elemement passed within the argument.
- The `list()` function takes all of the characters inside a string and creates a list containing each one as an element.
- The `count()` method
