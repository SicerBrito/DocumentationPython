# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
# Write a program that displays the string Hello World! on the screen.
print("¡Hello World!")


# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
# Write a program that stores the string (¡This text string is inside a variable!) in a variable and then display the contents of the variable on the screen.
menssage = "¡This text string is inside a variable!"
print(menssage)



# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
# Write a program that asks the console for the user's name and after the user enters it, displays the string Hello <name>!, where <name> is the name the user entered.
# \n\t se utiliza para insertar un salto de línea (\n) y una tabulación (\t)
# \n\t is used to insert a newline (\n) and a tab (\t)
name = input("Hello, what is your name? \n\t")
print("¡Hello " + name + "!")
#this is concatenation
print(f"¡Hello {name}!")