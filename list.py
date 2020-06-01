#adding basic variables List/array
random_number=[8,7,9,4,12]
friends=["karen","jim","james","oscar","toby"]
#append fuction
friends.append("tori")
#extend fuction
friends.extend(random_number)
#insert fuction with index
friends.insert(2,"yoon")
print(friends)
#modify variables with index
friends[1:3]="mike","toby"
#remove list
friends.remove("toby")
print(friends)
#clear list
friends.clear()
print(friends)
friends.append("tori")
print(friends)
friends=["kori","tori","tori","toby"]
print(friends)

#pop fuction
friends.pop()
print(friends)
#find index number of a list
print(friends.index("tori"))
#count element in a list
print(friends.count("tori"))
#sort ascending list 
friends.sort()
random_number.sort()
print(friends)
print(random_number)
#reverse list
random_number.reverse()
print(random_number)

#copy list
luckynumber= random_number.copy()
print(luckynumber)
