
def reverse_string(s):
    return s[::-1]

string = "manoj"
print("reversed string: ", reverse_string(string))

def reverse_each_word(s):
    words = s.split()
    reverse = [word[::-1] for word in words]
    return ' '.join(reverse)

string = "my name is manoj"
print("reversed each word: ", reverse_each_word(string))

def duplicate(s):
    seen = {}
    for ch in s:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] += 1
    duplicates = [(cha,num) for cha,num in seen.items() if num != 1]
    return duplicates

string = "hello"
print("duplicates are: ", duplicate(string))
