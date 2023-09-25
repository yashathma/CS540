import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26
    with open('e.txt',encoding='utf-8') as f:
    #with open('/Users/yash/Desktop/School/VSCode/hw2/e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()
    with open('s.txt',encoding='utf-8') as f:
    #with open('/Users/yash/Desktop/School/VSCode/hw2/s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    X=dict()
    X={key: 0 for key in keys}
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        content = f.read()
    for char in content:
        if char.upper() in X:
            X[char.upper()]+=1


    return X

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
dictlist = shred("letter.txt")
#dictlist = shred("/Users/yash/Desktop/School/VSCode/hw2/samples/letter3.txt")

print("Q1")
for key in dictlist:
    print(key+' '+str(dictlist[key]))

print("Q2")
e,s = get_parameter_vectors()
english = dictlist["A"]*math.log(e[0])
spanish = dictlist["A"]*math.log(s[0])
formatted_number = f"{english:.4f}"
print(formatted_number)
formatted_number = f"{spanish:.4f}"
print(formatted_number)

print("Q3")
#English
english = 0
chars = list(dictlist.values())
for i in range(0,len(chars)):
    english+=(chars[i]*math.log(e[i]))
english+=math.log(0.6)
formatted_number = f"{english:.4f}"
print(formatted_number)
#Spanish
spanish = 0
chars = list(dictlist.values())
for i in range(0,len(chars)):
    spanish+=chars[i]*math.log(s[i])
spanish+=math.log(0.4)
formatted_number = f"{spanish:.4f}"
print(formatted_number)

print("Q4")
if (spanish-english >= 100):
    print(0.0000)
elif (spanish-english <= -100):
    print(1.0000)
else:
    finalval = 1/(1+(math.e**(spanish-english)))
    formatted_number = f"{finalval:.4f}"
    print(formatted_number)












            