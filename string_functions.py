#!/bin/python3

def rev_str(s):
    #reverse_string=s[::-1]
    return s[::-1]

#ori_str=input("Enter a string to reverse: ")
#print(f"reversed string: {rev_str(ori_str)}")

def rev_estr(s): #split(),join()
    words=s.split()
    rev_words=' '.join(word[::-1] for word in words)
    return rev_words
#ori_str=input("Enter a string: ")
#print(f"Reversed each word: {rev_estr(ori_str)}")

def count_char(s):
    cln_str=s.replace(' ','').lower()
    char_count={}
    for char in cln_str:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count
#Str=input("Enter the string:")
#result=count_char(Str)
#print("Duplicate characters:")
#for char,count in result.items():
#        if count > 1:
#            print(f"{char}: {count} times")

def count_characters(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

#Str=input("Enter the string:")
#print(f"{count_characters(Str)}")
#result=count_characters(Str)
#for char,count in result.items():
#    print(f"{char}: {count} times")

def count_words(s):
    words=s.split()
    print(words)
    return len(words)
#Str=input("Enter the string:")
#print(f"The number of words: {count_words(Str)}")

#Python program to find all permutations of a given string
import itertools
def find_permutations(s):
    perm=[''.join(p) for p in itertools.permutations(s)]
    return perm

#example usage
#input_str='abc'
#permutations=find_permutations(input_str)
#print(permutations)

#print(f"All permutations of '{input_str}':")
#for p in permutations:
#    print(p)


#Python Program to find if a string is palindrome
def is_palindrome(s):
    s=s.replace(' ','').lower()
    return s == s[::-1]

#Example
#user_input=input("Enter a string: ")
#if is_palindrome(user_input):
#    print("It's is a palindrome")
#else:
#    print("It's is not a palindrome")

#Python Program to find if two strings are anagrams
def is_anagram(str1,str2):
    str1=str1.replace(' ','').lower()
    str2=str2.replace(' ','').lower()
    return sorted(str1)==sorted(str2)

#Example usage
#string1=input("Enter the string1: ")
#string2=input("Enter the string2: ")

#if is_anagram(string1, string2):
#    print("The strings are anagram")
#else:
#    print("The strings are not anagram")

def count_vowels_consonants(text):
    vowels="aeiou"
    vowel_count=0
    consonant_count=0

    text=text.lower()
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count, consonant_count

#Example usage
string=input("Enter a string: ")
vowels,consonants=count_vowels_consonants(string)
print(f"vowels: {vowels}")
print(f"consonants: {consonants}")
