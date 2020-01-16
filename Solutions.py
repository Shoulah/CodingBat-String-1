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


""" 
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags("i", "Yay"))    
 """
""" 
def make_out_word(out, word):
     if len(out) == 4:
         return out[0:2] + word + out[2:4]

print(make_out_word("<<>>", "Ahmed Shoulah"))
 """         


def extra_end(str):
    return str[len(str)-2: len(str)] * 3

print(extra_end("ABCD"))
