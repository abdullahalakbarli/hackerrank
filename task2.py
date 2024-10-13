import math
import os
import random
import re
import sys



def transformSentence(sentence):
    lst = sentence.split()
    for word in lst:
        lst2 = list(word)
        for i in range(1,len(lst2)):
            if lst2[i].lower() > lst2[i-1].lower():
                lst2[i] = lst2[i].upper()
            elif lst2[i].lower() < lst2[i-1].lower():
                lst2[i] = lst2[i].lower()
            else:
                continue
        word = ''.join(lst2)
        print(word, end=" ")

if __name__ == '__main__':

    sentence = input()

    result = transformSentence(sentence)

