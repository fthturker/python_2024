names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

#1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')  # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

#2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')  #['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']
names.insert(-1, 'Mehmet') #['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Mehmet', 'Cenk']
names.insert(len(names), 'Mehmet') # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Mehmet', 'Cenk', 'Mehmet']

#3-  "Deniz" ismini listeden siliniz.

names.remove('Deniz') #['Sena', 'Ali', 'Yağmur', 'Hakan', 'Mehmet', 'Cenk', 'Mehmet']
#names.pop()
#names.pop(1)

#4-  "Deniz" isminin indeksi nedir ?
#index  = names.index('Deniz')
#print(index)
#names.pop(index)

#5-  "Ali" listenin bir elemanı mıdır ?
result = 'Ali' in names
print(result)  # True
result = names.index('Ali')
print(result) #1

#6-  Liste elemanlarını ters çevirin.
names.reverse()  #['Mehmet', 'Cenk', 'Mehmet', 'Hakan', 'Yağmur', 'Ali', 'Sena']

#7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()  #['Ali', 'Cenk', 'Hakan', 'Mehmet', 'Mehmet', 'Sena', 'Yağmur']

#8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()  #['Ali', 'Cenk', 'Hakan', 'Mehmet', 'Mehmet', 'Sena', 'Yağmur']

#9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet,Dacia"
result = str.split(',')
print(result)  # ['Chevrolet', 'Dacia']

#10- years dizisinin en büyük ve en küçük elemanı nedir ?

min = min(years)  # 1987
max = max(years)  # 2000 
print(min, max)   # 1987 2000
print(max) 

#11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)
print(result) #2

#12- years dizisinin tüm elemanlarını siliniz.
years.clear()

#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)
#print(names)