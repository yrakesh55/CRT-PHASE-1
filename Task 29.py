#list
friends=["Rakesh",528,555,"Kishore",3021,"Mukesh",246,3.22]
print(friends)


friends.append("forever")
print(friends)


friends.insert(4,"Sahithi")
print(friends)


print(friends[0])
print(friends[3])
print(friends[4])
print(friends[6])


for i in range(0,len(friends)):
    print(friends[i])

for i in friends:
    print(i)


print(friends[2:5])
print(friends[:5])
print(friends[1:])
print(friends[::-1])
print(friends[1:8:2])


friends[2]="Prathyu"
print(friends)
