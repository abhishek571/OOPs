file=open('text.txt','w')
file.write("this is text file")
file.close()

file=open('text.txt','r')
content=file.read()
print(content)
file.close()


file=open('text.txt','r')
# print(file.readlines())
content=file.read(5)
# file.seek(16)
# print(content)
# print(file.read())
print(content)
# print(file.tell())

