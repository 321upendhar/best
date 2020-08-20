Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(25,32,45,56)
>>> tup
(25, 32, 45, 56)
>>> tup[1]
32
>>> tup[1]=33
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1]=33
TypeError: 'tuple' object does not support item assignment
>>> set={22,21,4,5,26,28}
>>> s
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s={22,34,5,52,25,31}
>>> s
{34, 5, 52, 22, 25, 31}
>>> s={22,43,67,87,90}
>>> s
{67, 43, 22, 87, 90}
>>>  data{1:'navin',2:'kiran',4:'harsh'}
 
SyntaxError: unexpected indent
>>> data{1;'kiran',2:'navin',3:'harsh'}
SyntaxError: invalid syntax
>>> data={1:'kiran',2:'navin',3:'harsh'}
>>> data
{1: 'kiran', 2: 'navin', 3: 'harsh'}
>>> data[3]
'harsh'
>>> data[1]
'kiran'
>>> data.get(1)
'kiran'
>>> data(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data(3)
TypeError: 'dict' object is not callable
>>> data.get(3)
'harsh'
>>> data.get(4)
>>> print(data.get(1))
kiran
>>> print(data.get(4))
None
>>> data.get(1,'Not Found')
'kiran'
>>> data.get(4,'Not Found')
'Not Found'
>>> keys=['Navin','Kiran','Harsh']
>>> values=['Python','Java',JS]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    values=['Python','Java',JS]
NameError: name 'JS' is not defined
>>> keys=['Navin','Kiran','Harsh']
>>> values=['Python','Java','JS']
>>> data=dict(zip(keys,values))
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Harsh': 'JS'}
>>> data['Kiran']
'Java'
>>> data['Monika']='CS'
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Harsh': 'JS', 'Monika': 'CS'}
>>> del data['Harsh']
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Monika': 'CS'}
>>> prog={'JS':'Atom','CS':'VS,'Python':['Pycharm','Sublime'],'JAVA':{'JSE':'Netbeans','JEE':'Eclipse'}}
      
SyntaxError: invalid syntax
>>> prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'JAVA':{'JSE':'Netbeans','JEE':'Eclipse'}}
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'JAVA': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog[JS]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    prog[JS]
NameError: name 'JS' is not defined
>>> 	prog['JS']
	
SyntaxError: unexpected indent
>>> prog['JS']
'Atom'
>>> prog['cs']
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    prog['cs']
KeyError: 'cs'
>>> prog['CS']
'VS'
>>> prog['Python']
['Pycharm', 'Sublime']
>>> prog[0]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    prog[0]
KeyError: 0
>>> prog['Python'][0]
'Pycharm'
>>> prog['Python'][1]
'Sublime'
>>> prog['Java']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    prog['Java']
KeyError: 'Java'
>>> prog['JAVA']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['JAVA']['JEE']
'Eclipse'
>>> prog['JAVA']['JSE']
'Netbeans'
>>> 