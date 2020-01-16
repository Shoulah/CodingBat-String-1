""" Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!' """
""" 
def hello_name(name):
    return "Hello " + name + "!"


print(hello_name('Bob'))

 """

"""  Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat' """
""" 
def make_abba(a, b):
    return a + b + b + a

print(make_abba("Hi", "Bye"))    
 """



def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags("i", "Yay"))    