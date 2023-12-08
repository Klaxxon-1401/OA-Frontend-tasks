o=open('demofile.txt','a+')
o.write('\ntestappend')
o=open('demofile.txt','a+')
o.seek(0)
print(o.read())

o.close()
