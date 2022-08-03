from cgitb import reset


def show(x):
    print(x['h'],":",x['m'],":",x['s'])
def sum(x,y):
    result={}
    result['h']=x['h']+y['h']
    result['m']=x['m']+y['m']
    result['s']=x['s']+y['s']
    if result['s']>=60:
        result['s'] -=60
        result['m'] +=1
    if result['m']>=60:
        result['m'] -=60
        result['h'] +=1
    return result
def sub(x,y):
    result={}
    result['h']=x['h']-y['h']
    result['m']=x['m']-y['m']
    result['s']=x['s']-y['s']
    if result['s']<0:
        result['s'] +=60
        result['m'] -=1
    if result['m']<0:
        result['m'] +=60
        result['h'] -=1
    return result
def second():
    second=int(input('Enter second: '))
    print('hours: ',end='')
    result = {}
    result['h'] = second // 3600
    result['m'] = (second % 3600) // 60
    result['s'] = (second % 3600) % 60
    return result
def hour():
    result = {}
    result['h'] = int(input('Enter hour: '))
    result['m'] = int(input('Enter minute: '))
    result['s'] = int(input('Enter second: '))
    second = ( int(result['h']) * 3600 ) + ( int(result['m']) * 60 ) + ( int(result['s']) ) 
    print('second:' ,second)


t1={'h':2,'m':30,'s':45}
t2={'h':3,'m':17,'s':40}
t3=sum(t1,t2)
show(t3)
t4=sub(t1,t2)
show(t4)
show(second())
hour()