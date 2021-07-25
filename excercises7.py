import re


# file=open("mbox-short.txt",'r')
# for line in file:
#     # if re.search("^From:.+@",line):
#     #     print(line)
#     lst=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]',line)
#     if len(lst)>0:
#         print(lst)
# _______________________________________________________________________________
# file=open("mbox-short.txt",'r')
# for line in file:
#     lst=re.findall('^X\S*: ([0-9.]+)',line)
#     if len(lst)>0:
#         print(lst)
# ---------------------------------------------------------------------------
# count=0
# exp=input("Enter a regular expression: ")
# file=open("mbox-short.txt",'r')
# for line in file:
#     if re.search(exp,line)!=None:
#         count+=1
# print(f"mbox.txt had {count} lines that matched {exp}")

file=open("mbox-short.txt",'r')
num=list()
for line in file:
    line=line.rstrip()
    lst=re.findall('^New Revision: ([0-9]+)',line)
    if lst:
        num.append(int(lst[0]))
print(sum(num)//len(num))