message='Hello There. My name is Fatih Türker'

#message=message.upper() yazının hepsini büyük yapar 
#message=message.lower()  #yazının hepsini küçük yapar
#message=message.title() # Hello There. My Name Is Fatih Türker
#message=message.capitalize() # verilen kelimenin sadece ilk harfini büyük yapar
#message=message.split()
#message=message.strip()
# cümle içerisinde Fatih olup olmadığını kontrol etmek istiyorum.
#index=message.find('Fatih')
#print(index) # 25

#isFound=message.startswith('H') # cümle H ile başlıyor ve True olarak dönüyor
#isFound=message.endswith('r') # cümle r ile bitiyor ve True olarak dönüyor
#print(isFound)

#message=message.replace('Fatih','Yavuz') # cümlede Fatih yerine Yavuz yazacak

message=message.center(50,'*')
print(message)