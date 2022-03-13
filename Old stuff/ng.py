
#ye ye ye ye ye
print("welcome to random name Generator! ")

print("Press ENTER for name magic")

x= input()



with open(r'D:\adj.txt') as infile:
    data=[line.rstrip() for line in infile]
    adj=data

with open(r'D:\noun.txt') as infile:
    data1=[element.rstrip() for element in infile]
    noun=data1


from random import randint


l = len(adj) - 1
L = len(noun) - 1

y = adj[randint(0,l)]
x = noun[randint(0,L)]
print(y,x)

y = input()

print('Now GO AWAY')

xx = input()