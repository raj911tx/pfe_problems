count=0
total=0
string='X-DSPAM-Confidence:'

try:
    file_path=input('Enter File Name: ')
    file=open(file_path,'r')
    col=string.find(':')

    for s in file:
        s=s.rstrip()
        if string in s:
            total+=float(s[col+1:])
            count+=1
    file.close()
    print(total/count)
except Exception as e:
    if file_path=='na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print(e,"Check file path again")



