# STRINGS:  
05
--
- split() method in Python is used to split a string into a list of substrings based on a separator (default is any whitespace).
- words = text.split()

06
--
- itertools module:  Generate all permutations as tuples and join them to form strings
- Note: It does not care if characters are repeated — it treats each position independently.
```
perms = itertools.permutations(s) #Output: ('a', 'b', 'c'), ('a', 'c', 'b'),...
return [''.join(p) for p in perms]
```
07
--
- s[::-1] reverses the string.
- .replace(" ", "") removes spaces (optional, depending on requirements).
- .lower() makes it case-insensitive.
