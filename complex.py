from unittest import result


def show(x):
    print(x['r'],'+',x['i'],'i')
def sum(x,y):
    result={}
    result['r']=x['r']+y['r']
    result['i']=x['i']+y['i']
    return result
def sub(x,y):
    result={}
    result['r']=x['r']-y['r']
    result['i']=x['i']-y['i']
    return result
def mul(x,y):
    result={}
    result['r']=x['r']*y['r']
    result['i']=x['i']*y['i']
    return result

a={'r':5,'i':3}
b={'r':7,'i':8}
c=sum(a,b)
show(c)
d=sub(a,b)
show(d)
e=mul(a,b)
show(e)