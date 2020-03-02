#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def orangecap(orangecap):
    players=[]
    for match in orangecap.keys():
        for player in orangecap[match].keys():
            if player not in players:
                players.append(player)
    total={}
    for batter in players:
        total[batter]=0
        for match in orangecap.keys():
            if batter in orangecap[match]:
                total[batter] +=orangecap[match][batter]
    max=0
    for i in total.values():
        if max<i:
            max=i
        else:
            max=max           
    key_list = list(total.keys()) 
    val_list = list(total.values()) 
    return((key_list[val_list.index(max)],max))
  
def addpoly(p1,p2):
    for i in range(len(p1)):
        for item in p2:
            if p1[i][1] == item[1]:
                p1[i] = ((p1[i][0] + item[0]),p1[i][1])
                p2.remove(item)
    p3 = p1 + p2
    p4=[]
    for item in (p3):
        if item[0] == 0:
            p4.append(item)
    for i in p4:
        if i in p3:
            p3.remove(i)
    p3.sort(key=lambda tup: tup[1], reverse=True)
    return p3

    
      
def multpoly(p1,p2):
    p=[]
    s=0
    for i in p1:
        c=[]
        for j in p2:
            s=i[0]*j[0]
            e=i[1]+j[1]
            c.append((s,e))
        p=addpoly(c,p)
    return p 

  
  
  



# Hidden code below

import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

def tostring(s):
  lquote = s.find('"')
  rquote = s.rfind('"')
  return(s[lquote+1:rquote])

def tolist(s):
  lbrack = s.find('[')
  rbrack = s.rfind(']')
  slist = s[lbrack+1:rbrack].split(',')
  if slist == ['']:
    slist = []
  else:
    for i in range(0,len(slist)):
      slist[i] = int(slist[i])
  return(slist)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg),end="")
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2),end="")
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2),end="")
else:
   print("Function", fname, "unknown")

