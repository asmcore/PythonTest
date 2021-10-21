import lib
import os

lib.display()
dir = lib.directory()
for i in dir:
    print(i)
    less = lib.open_file('lessons/less01/less-01.txt')
lib.show_less(less)
for i in range(len(less)):
    string = lib.to_list(less[i])
    x_str=input('  ')
    if len(x_str)!=len(string):
        print('error len >')
        break
    if lib.is_ok(string, x_str):
        pass
    else:
        for j in range(len(string)):
            string[j] = x_str[j]
        print('  '+ lib.to_string(string)+' - error')
        break
print('*'*45)
input()
os.system('clear')
