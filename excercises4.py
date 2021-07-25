# lst=list()
# try:
#     file_path=input("Enter File Path: ")
#     file=open(file_path,'r')
#     for f in file:
#         f=f.rstrip()
#         words=f.split()
#         for word in words:
#             if word not in lst:
#                 lst.append(word)

#     print(lst)
# except:
#     print("Enter correct path")


# count=0
# file_path=input("Enter file path: ")
# file=open(file_path, 'r')
# for f in file:
#     f=f.rstrip()
#     if f.startswith('From'):
#         words=f.split()
#         print(words[1])
#         count+=1

# print(f'There were {count} lines in the file with From as the first word')

lst=list()
while True:
    try:
        data=input("Enter a Number: ")
        lst.append(int(data))
    except:
        if data=='done':
            # print(lst,max(lst))
            print("Maximum:{}\nMinimum:{}".format(max(lst),min(lst)))
            break
        print("Check input")