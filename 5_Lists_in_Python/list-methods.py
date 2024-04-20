numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val =min(numbers)  #1 
val=max(numbers)  #16

val =min(letters)  #a 
val=max(letters) #y

val=numbers[3:6] #[16, 4, 9]
val=numbers[:3]  #[1, 10, 5]
val=numbers[4:]  #[4, 9, 10]

numbers[4]=40  # [1, 10, 5, 16, 40, 9, 10]

numbers.append(49)  # [1, 10, 5, 16, 40, 9, 10, 49]
numbers.insert(3,11)  # [1, 10, 5, 11, 16, 40, 9, 10, 49]

numbers.sort()  # [1, 5, 9, 10, 10, 11, 16, 40, 49]
numbers.reverse()  # [49, 40, 16, 11, 10, 10, 9, 5, 1]

print(val)
print(numbers)

print(len(numbers)) # 9
print(numbers.count(10)) # 2
