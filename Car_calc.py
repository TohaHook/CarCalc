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