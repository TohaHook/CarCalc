#Input
name = input( "Имя" )
surname = input( "Фамилия" )
region = input( "Регион" )
car = input( "Машина" )
year = int(input("Год выпуска"))
hp = int(input( "Лошадиные силы" ))
own = int(input("Срок владения месяцев"))
#Output
print("Привет!", name, surname)
print("Регион", region, "." , "Машина", car, "," , "год выпуска", year, "мощность" , hp, "лошадиных сил")
# Функция расчета налоговой ставки в зависимости от мощности
def tax(x):
    print("Налог в год составляет" , x * hp)
    print("Налог за время владения" , x * hp*(own/12))
if ( hp >= 5 and hp < 100):
    x = 12
elif ( hp >= 100 and hp < 150):
    x = 35
elif(hp >150 and hp <200):
    x = 45
elif(hp >= 200 and hp <225 ):
    x =55
elif(hp >= 225 and hp <250 ):
    x = 75
elif(hp >= 250):
    x = 150
tax(x)
# Функция расчета среднего расхода и стоимости километра
x=int(input("Объем бака"))
y=float(input("Стоимость за литр"))
z=float(input("Общий пробег до пустого бака"))
def f2(x,z):
    return x /z*100
a=f2(x,z)
print("Средний расход топлива","{:.2f}".format(a),"литров")
def f1(a,y):
    return(((a*y)/100))
b=f1(a,y)
f1(a,y)
print("Стоимость километра","%.2f" % (b),"рублей")