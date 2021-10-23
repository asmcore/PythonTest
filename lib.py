import os
import shutil

PATH_LESS = 'lessons'

def line_display():
    c = shutil.get_terminal_size()
    return c[0]

def display():
    os.system('clear')
    str='добро пожаловать'
    c = line_display()
    col=int((c-len(str))/2)
    print(' '*col+str)
    print('*'*c)
    print()

def is_ok(a1:list, a2:list)->bool:
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

def line(less:list)->None:
    print('+'+'-'*(width_line(less)+2)+'+')

def width_line(l:list)->int:
    max = 0
    for i in l:
        min = len(i)
        if min > max:
            max = min
    return max

def show_less(less:list)->None:
    print('lesson:')
    line(less)
    for i in range(len(less)):
        print('¦ ' +less[i]+' '*(width_line(less)-len(less[i]))+' ¦')
    line(less)

def directory()->list:
    dr=[]
    with os.scandir(PATH_LESS) as d:
        for dd in d:
            if os.path.isdir(dd):
                dr.append(dd.name) 
    return dr

def files(dic:list)->dict:
    dict = {} 
    files = []
    for i in range(len(dic)):
        file=[]
        with os.scandir(PATH_LESS+'/'+dic[i]) as fl:
            for j in fl:
                if os.path.isfile(j):
                    file.append(j.name)
        files.append(file)
        dict.update({dic[i]:files[i]})
    print(files)
    return dict

dic = directory()
print(files(dic))
