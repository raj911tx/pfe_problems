# file_path=input("Enter file path: ")
# d=dict()
# file=open(file_path, 'r')
# for f in file:
#     f=f.rstrip()
#     for word in f.split():
#         d[word]=0
# print(d)
# file.close()

# d=dict()
# try:
#     file_path=input("Enter File path: ")
#     file=open(file_path,'r')
#     for f in file:
#         f=f.rstrip()
#         if f.startswith('From'):
#             f=f.split()
#             if len(f)>2:
#                 seq=f[2]
#                 d[seq]=d.get(seq,0)+1

# except:
#     print("Enter Correct Path")

# print(d)

d=dict()
try:
    file_path=input("Enter File path: ")
    file=open(file_path,'r')
    for f in file:
        f=f.rstrip()
        if f.startswith('From'):
            f=f.split()
            md=f[1]
            d[md]=d.get(md,0)+1

except:
    print("Enter Correct Path")


t=list()
for data in d:
    t.append((d[data],data))
print(max(t)[1],max(t)[0])
    



# d=dict()
# try:
#     file_path=input("Enter File path: ")
#     file=open(file_path,'r')
#     for f in file:
#         f=f.rstrip()
#         if f.startswith('From'):
#             f=f.split()           
#             md=f[1]
#             md=md.split('@')[1]
#             d[md]=d.get(md,0)+1


# except:
#     print("Enter Correct Path")
# print(d)