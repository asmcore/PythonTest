import os

dr=[]
with os.scandir('lessons') as d:
    for dd in d:
        if os.path.isdir(dd):
           dr.append(dd.name) 
print(dr)
