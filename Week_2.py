#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factors(n):
    if n == 0:
        return([0])
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist.append(i)
    return(factorlist)

def square(n):
    return(len(factors(n))%2 == 1)

def threesquares(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            if square(i) and square(j) and square(n-(i+j)):
                return(True)
    return(False)

##################################################


def repfree(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return(False)
    return(True)


##################################################

def ascending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] < l[1] and ascending(l[1:]))

def descending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] > l[1] and descending(l[1:]))

def hill(l):
    for i in range(1,len(l)-1):
        if ascending(l[:i+1]) and descending(l[i:]):
            return(True)
    return(False)

def valley(l):
    for i in range(1,len(l)-1):
        if descending(l[:i+1]) and ascending(l[i:]):
            return(True)
    return(False)

def hillvalley(l):
    return(hill(l) or valley(l))

##################################################

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "threesquares":
   arg = parse(farg)
   print(threesquares(arg))
elif fname == "repfree":
   arg = parse(farg)
   print(repfree(arg))
elif fname == "hillvalley":
   arg = parse(farg)
   print(hillvalley(arg))
else:
   print("Function", fname, "unknown")
            

