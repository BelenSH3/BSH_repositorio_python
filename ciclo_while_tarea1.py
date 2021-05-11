#crear un programa que capture las calificasiones
#Hola soy un comentario de cynthia 
print("·········································")
print("Captura las calificasiones de los alumnos")

lim=1
limite=int(input("Cuantos alumnos deseas ingresar= "))

nombre = []
cali=[]

while lim<=limite:
        
        nombre.append(input("Ingresa el nombre del alumno: "))
        cali.append(input("Captura la  calificacion del alumno: "))
         
       
        lim=lim+1

print(nombre)
print(cali)
