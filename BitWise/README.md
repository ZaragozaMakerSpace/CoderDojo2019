# CoderDojo2019 ZMS BitWise
Durante esta sesión vamos a desarrollar algunos ejercicios relacionados con las unidades más pequeñas de la computación.

Vamos a bajar a nivel de bit y vamos a aprender cómo desarrollar con grupos de bits para obtener algunos resultados.

En estos ejercicios se valorarán las soluciones que se puedan integrar en pocas lineas de código. Cada uno de los ejercicios tiene una puntuación que puede variar en función de la dificultad. El objetivo es conseguir la máxima puntuación. 

Para desarrollar los siguientes ejercicios se pueden elegir entre estos dos lenguajes de programación.
- [Python](https://repl.it/languages/python3) 
- [C++](https://repl.it/languages/cpp) 

# BitWise Operators

Lo primero que tenemos que aprender es qué son los operadores a nivel de bit.

- &  --> El operador AND funciona como una puerta lógica AND donde solo se activa el bit si los dos están activos. 
- |  --> El operador OR funciona como una puerta lógica OR donde se activa el bit si al menos uno esta activo. 
- ^  --> Operador XOR.
- ~  --> Negacion de bit.
- `>>` --> Desplazamiento a la derecha.
- << --> Desplazamiento a la izquierda.


![bit_samples](src/truthTable.jpg)



# Ejercicios propuestos

Dada una secuencia de unos y ceros cualesquiera almacenados en una dirección de memoria. Se pide:

- Position of rightmost set bit. Encontrar la posición del primer bit con valor uno. [5 puntos]. 
- Position of rightmost zero bit. Encontrar la posición del primer bit con valor cero. [5 puntos]. 
- Contar cuantos bits son unos. [5 puntos]
- Encontrar la longitud de 1s que se repiten a partir de la aparicion del primer bit. [8 puntos]
- Desplazamiento circular. Cuando se desplaza un bit, se pierde información en uno de los extremos. El desplazamiento circular se basa en recuperar la información perdida en un extremo para que aparezca en el extremo contrario. [10 puntos]
- Erode - Si tenemos un conjunto de bits activos, eliminar un bit activo en cada uno de sus extremos. [10 puntos]
- Dilate - Dado un conjunto de bits agrupados, extender en una unidad por sus extremos. [10 puntos]
- Dibujar un emoticono por pantalla de 10 filas y 10 columnas con unos y ceros usando bits. [10 puntos]
- Detectar que un número es impar mediante operaciones con bits. [5 puntos]
- Detectar si un numero en binario no aparece un uno a coninuación de otro. [10 puntos]
- Desplazar los bits hacia el exterior desde la mitad de la longitud. 001010011011 -> 010100001101 [10 puntos]
- Sacar la operación que habría que realizar para obtener el resultado de la siguiente imagen. [12 puntos]
![bitWise_Comparison](src/bitwiseComparison.png)


