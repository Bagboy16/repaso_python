lista_nombres = ["Andy", "Pedro", "Juan", "Hugo Rafael Chávez Frías"]

#LISTAS:
#List ---> Array

lista_nombres[0] # Andy
lista_nombres[1] # Pedro
lista_nombres[2] # Juan
lista_nombres[3] # Hugo Rafael Chávez Frías

lista_nombres[-1] # Hugo Rafael Chávez Frías
lista_nombres[-2] # Juan
lista_nombres[-3] # Pedro
lista_nombres[-4] # Andy


#TUPLAS:
#Tupla ---> Array inmutable

tupla_fases_de_goku = ("SSJ", "SSJ2", "SSJ3", "SSG", "SSB")

tupla_fases_de_goku[0] # SSJ
tupla_fases_de_goku[1] # SSJ2
tupla_fases_de_goku[2] # SSJ3
tupla_fases_de_goku[3] # SSG
tupla_fases_de_goku[4] # SSB

tupla_fases_de_goku[-1] # SSB
tupla_fases_de_goku[-2] # SSG
tupla_fases_de_goku[-3] # SSJ3
tupla_fases_de_goku[-4] # SSJ

#EJEMPLO DE MUTABILIDAD:

lista_nombres[0] = "Antonio" # una lista es mutable

#EJEMPLO DE NO MUTABILIDAD:

#tupla_fases_de_goku[0] = "SSJ4" # una tupla es inmutable (no se puede modificar)

#DICCIONARIOS:
#Array asociativo:
#Los elementos son propiedades (claves / keys) y tienen un valor asociado (valores / value)
#Corresponde a la estructura de datos Tabla Hash, Diccionario, Map, Object, HashMap, entre otros
#Se accede a los elementos mediante las claves
#Son mutables
#Las claves son únicas, y generalmente de tipo String (str en python)
#Los valores pueden ser de cualquier tipo de dato, incluido otro diccionario

#Ejemplo diccionario básico
dict_colores = {
    #Clave: Nombre del Color
    #Valor: Código HEX del color
    "Rojo": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarillo": "#FFFF00",
    "Naranja": "#FFA500",
    "Morado": "#800080",
    "Blanco": "#FFFFFF"
}
#Acceder a un elemento del diccionario mediante notación de corchetes
dict_colores["Rojo"] # #FF0000
dict_colores["Amarillo"] # #FFFF00
dict_colores["Blanco"] # #FFFFFF

#La notación de corchetes presenta un problema cuando se accede a un elemento que no existe en el diccionario
try:
    print(dict_colores["Negro"])
except KeyError:
    print("EXEPCION: El color no existe en el diccionario")

#Existe otra forma de acceder a los elementos de un diccionario de forma segura

dict_colores.get("Morado") # #800080

#El método get() devuelve None si la clave no existe en el diccionario
color = dict_colores.get("Negro") # None

#El método get() recibe otro parámetro opcional que será retornado si el valor no existe en el diccionario
color = dict_colores.get("Negro", "Lo sentimos, el color no fué encontrado") # Lo sentimos, el color no fué encontrado  

#AGREGAR ELEMENTOS AL DICCIONARIO
dict_colores["Negro"] = "#000000"
dict_colores["Rosa"] = "#FF00FF"

#ELIMINAR ELEMENTOS AL DICCIONARIO
del dict_colores["Amarillo"] # Elimina el elemento con la clave "Amarillo"

print(dict_colores)

elemento_eliminado = dict_colores.pop("Rosa") # Elimina el elemento con la clave "Rosa" y lo devuelve

print(elemento_eliminado)

nombre_color = input("Ingrese el nombre del color: ")
hex_color = input(f"Ingrese el código HEX del color {nombre_color}: ")

dict_colores[nombre_color] = hex_color

print(dict_colores)

#Ejemplo diccionario complejo
dict_persona = {
    "datos_personales": {
        "nombre": "Isaac",
        "apellido":"Galviz"
    },
    "cargos": [
        "Director",
        "Gerente"
    ]
}

dict_persona["datos_personales"]["nombre"] # Isaac
dict_persona["cargos"][1] # Gerente




