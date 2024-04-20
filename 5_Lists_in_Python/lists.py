"""
Pythonda liste nedir ve nasıl kullanılır?

Python Collections (Arrays)
Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.

List, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.
Tuple, elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.
Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.
Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.
"""
"""
Pythonda Liste
String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanıdır ve 
her bir elemana indeks numarası ile ulaşabiliriz.

Gene aynı mantıkla list veri tipinde ise tek bir karakter yerine farklı veri tiplerindeki bilgileri gruplayabiliyoruz.
Karakter dizilerinde (string) olduğu gibi her bir eleman indekslenebilir.
"""
message = 'Hello There. My name is Sadık Turan'.split()
#print(message)    # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
#print(message[0]) # Hello

"""
Birinci liste elemanlarının hepsi aynı veri tipindeyken ikinci liste elemanları 
farklı veri tipinde tanımlanabilir dolayısıyla Python listeleri homojen bir yapıda olmayabilir.,
"""
#my_list=[1,2,3]
#my_list=['bir',2,True,5.6]
#print(my_list)

#İki farklı listeyi bir liste içinde gruplayabiliriz.
list1=['one','two','there']
list2=['four','five','six']

numbers=list1 + list2
print(numbers)  # ['one', 'two', 'there', 'four', 'five', 'six']

"""
Listelerde Eleman Sayısı
Python listelerinde eleman sayısını len() metodu ile öğrenebiliriz. 
Aynı metodu string içinde kullanıp karakter sayısını öğrenebiliriz.
"""
print(len(numbers)) #6
print(numbers[2]) #there

"""
Liste Elemanlarına Erişim
Python listelerindeki her bir elemanına soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz. 
Aynı şekilde sağdan -1. indeks numarasından başlamalıyız.
"""
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']

print(message[2])   # My
print(message[4])   # is
print(message[-1])  # Turan
print(message[-3])  # is

#Aynı şekilde liste içinde bir başka liste tanımladığımızda ise alt liste elemanı içinde [ ] kullanmamız gerekir. 
liste = [[1,2,3],[4,5,6],[7,8,9],10]

print(liste[0])     # [1,2,3]
print(liste[1][2])  # 6