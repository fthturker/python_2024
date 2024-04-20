maasAli=5000
maasAhmet=4000
vergi=0.27

print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

# degisken tanimlama kurallari
# rakam ile baslayamaz
number1=10
print(number1) #10
number1=20
print(number1) #20

number1 +=30
print(number1) #50

# buyuk kucuk harf duyarliligi vardir.
age=10
AGE=20
print(age) # 10
print(AGE)  # 20

# turkce karakter kullanmayalim
yaş = 20
_age=20

x=1                 # int
y=2.3               # float
name="Cinar"        # string
isStudent=True      # bool

x,y,name,isStudent= (1,2.3,"Cinar",True)

a=10
b=20
print(a+b)  # 30

a="10"
b="20"
print(a+b)  #1020

firstName="Fatih"
lastName="Turker"
print(firstName +" "+lastName)   #Fatih Turker