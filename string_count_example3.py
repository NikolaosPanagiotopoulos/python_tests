string="""In computer programming, a string is traditionally
a sequence of characters,either
as a literal constant or as some kind of variable.
The latter may allow its elements to be
mutated and the length changed,
or it may be fixed (after creation).
A string is generally considered as a data type and
is often implemented as an array data structure of bytes
(or words) that stores a sequence of elements,
typically characters, using some character encoding.
String may also denote more general arrays
or other sequence (or list) data types and structures."""
substring=string[0:64]
print(substring)
print(substring.count(" ")+1)
print(substring.count(" "))
badstring=""" In computer programming, a string is traditionally
a sequence of characters,either as a literal constant
or as some kind of variable. """
print(badstring)
print(badstring.strip())
print(badstring.lstrip())
print(badstring.rstrip())
