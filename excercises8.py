import socket

# sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('data.pr4e.org',80))
# cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# sock.send(cmd)

# while True:
#     data=sock.recv(512)
#     if len(data)<1:
#         break
#     print(data.decode(),end='')
# sock.close()
# --------------------------------------------------------------------------------------
# sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('data.pr4e.org',80))
# cmd='GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
# sock.send(cmd)

# picture=b""
# while True:
#     data=sock.recv(5120)
#     if len(data)<1: break
#     picture+=data

# header_pos=picture.find(b'\r\n\r\n')
# print(picture[:header_pos].decode())

# picture=picture[header_pos+4:]
# file=open('dummy.jpg','wb')
# file.write(picture)
# file.close()
# ------------------------------------------------------------------------------------
import urllib.request
# print(dir(urllib.request))
# fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for file in fhand:
#     print(file.decode().strip())

# img=urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
# file=open('dummy2.jpg','wb')
# while True:
#     blocks=img.read(10)
#     if len(blocks)<1: break
#     file.write(blocks)
# file.close()
# ------------------------------------------------------------------------------------------

import ssl
import re

# context =ssl.create_default_context()
# context.check_hostname=False
# context.varify_mode=ssl.CERT_NONE

# url=input("Enter URL :___")
# fhand=urllib.request.urlopen(url,context=context).read()
# links=re.findall(b'href="(http[s]?://.+?)"',fhand)
# for link in links:
#     print(link.decode())

# --------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup

# context=ssl.create_default_context()
# context.check_hostname=False
# context.varify_mode=ssl.CERT_NONE

# url=input("Enter URL :___")
# fhand=urllib.request.urlopen(url,context=context).read()
# bsoup=BeautifulSoup(fhand,"html.parser")

# tags=bsoup("a")
# for tag in tags:
#     print(tag.get("href",None))

# -------------------------------------------------------------------------------------------------
# sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# url=input("Enter The URL: ")
# host=url.split('/')[2]
# try:
#     sock.connect((host,80))
#     cmd=('GET '+url+' HTTP/1.0\r\n\r\n').encode()

#     sock.send(cmd)

#     while True:
#         data=sock.recv(512)
#         if len(data)<1:
#             break
#         print(data.decode(),end='')
# except:
#     print("Type correct url")

# sock.close()
# ---------------------------------------------------------------------------------

# try:
#     count=0
#     sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     url=input("Enter The URL: ")
#     host=url.split('/')[2]
#     sock.connect((host,80))
#     cmd=('GET '+url+' HTTP/1.0\r\n\r\n').encode()

#     sock.send(cmd)

#     while True:
#         data=sock.recv(512)
#         count+=len(data)
#         if len(data)<1 or count>=3000:
#             break        
#         print(data.decode(),end='')
#     print(f"Total Number of Chars: {count}")
# except:
#     print("Type correct url")

# sock.close()
# ----------------------------------------------------------------------------------
# context =ssl.create_default_context()
# context.check_hostname=False
# context.varify_mode=ssl.CERT_NONE

# url=input("Enter URL :___")
# fhand=urllib.request.urlopen(url,context=context)
# count=0
# while True:
#     blocks=fhand.read(512)
#     if len(blocks)<1 or len(blocks)>=3000: break
#     print(blocks.decode().strip())
#     count+=len(blocks)
# print(count)
# -----------------------------------------------------------------------------------------
# context=ssl.create_default_context()
# context.check_hostname=False
# context.varify_mode=ssl.CERT_NONE

# url=input("Enter URL :___")
# fhand=urllib.request.urlopen(url,context=context).read()
# bsoup=BeautifulSoup(fhand,"html.parser")

# tags=bsoup("p")
# count=0
# for tag in tags:
#     count+=1
# print(count)
# ----------------------------------------------------------------------------------
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url=input("Enter The URL: ")
host=url.split('/')[2]
try:
    sock.connect((host,80))
    cmd=('GET '+url+' HTTP/1.0\r\n\r\n').encode()

    sock.send(cmd)
    store=""
    while True:
        data=sock.recv(512)
        if len(data)<1:
            break
        store+=data.decode()
    header_pos=store.find('\r\n\r\n')
    print(store[header_pos+4:])
except:
    print("Type correct url")

sock.close()