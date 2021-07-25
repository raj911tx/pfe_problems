# d=dict()

# file_path=input("Enter the File Path: ")
# file=open(file_path,'r')
# for f in file:
#     f=f.rstrip()
#     if f.startswith('From'):
#         f=f.split()
#         add=f[1]
#         d[add]=d.get(add,0)+1
# l=list()
# for key,val in d.items():
#     l.append((val,key))

# l=sorted(l,reverse=True)

# print(l[0][1],l[0][0])


# d=dict()
# file_path=input("Enter the file path: ")
# file=open(file_path,'r')
# for f in file:
#     f=f.rstrip()
#     if f.startswith('From'):
#         f=f.split()
#         if len(f)>2:
#             data=f[5]
#             data=data.split(':')
#             data=data[0]
#             d[data]=d.get(data,0)+1
# l=list()
# for key,val in d.items():
#     l.append((key,val))
# l.sort()
# for key,val in l:
#     print(key,val)
        

import string

d=dict()
file_path=input("Enter the File Path: ")
file=open(file_path,'r')
for line in file:
    line=line.strip()
    line=line.translate(line.maketrans('','',(string.punctuation)))
    line=line.translate(line.maketrans('','',(string.digits)))
    line=line.translate(line.maketrans('','',(string.whitespace)))
    line=line.lower()
    for cha in line:
        d[cha]=d.get(cha,0)+1

total=sum(d.values())
f=dict()
for key,val in d.items():
    f[key]=(val/total)*100
print(f)


import matplotlib.pyplot as plt
plt.hist(f,10)
plt.show()
    