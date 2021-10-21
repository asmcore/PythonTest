import os

def display():
    os.system('clear')
    print('Добро пожаловать')
    print('*'*30)
    print()

def is_ok(a1:list, a2:list)->bool:
    flag = bool
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

def to_list(s:str)->list:
    a = []
    for i in range(len(s)):
        a.append(s[i])

    return a

def to_string(l:list)->str:
    s =''
    return s.join(l)

def open_file(s:str)->list:
    with open(s,'r') as f:
        return file_line_strip(f.readlines())

def file_line_strip(a:list)->list:
    for i in range(len(a)):
        a[i] = a[i].rstrip()
    return a

def line(less:list)->str:
    print('+'+'-'*(len(less[0])+2)+'+')

def show_less(less:list)->None:
    print('lesson:')
    line(less)
    for i in range(len(less)):
        print('¦ ' +less[i]+' ¦')
    line(less)

def directory()->list:
    dr=[]
    with os.scandir('lessons') as d:
        for dd in d:
            if os.path.isdir(dd):
                dr.append(dd.name) 
    return dr
