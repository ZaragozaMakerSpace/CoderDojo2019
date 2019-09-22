# CoderDojo2019 ZMS BitWise
Durante esta sesión vamos a desarrollar algunos ejercicios relacionados con las unidades más pequeñas de la computación.

Vamos a bajar a **nivel de bit** y vamos a aprender cómo desarrollar con grupos de bits para obtener algunos resultados.

En estos ejercicios se valorarán las soluciones que se puedan integrar en pocas lineas de código. Cada uno de los ejercicios tiene una puntuación que puede variar en función de la dificultad. El objetivo es conseguir la máxima puntuación. 

Para desarrollar los siguientes ejercicios se pueden elegir entre estos dos lenguajes de programación. **Elige uno**
- ### [Python](Python/README.md) 
- ### [C++](C++/README.md) 


### Haz click sobre la imagen para ver a BIT en la película de Tron (1982)

[![TRON_Bit](src/TronBIT.jpg)](https://www.youtube.com/watch?v=2OgWHeQ0UlY)



# [BitWise Operators](https://es.wikipedia.org/wiki/Operador_a_nivel_de_bits)

Lo primero que tenemos que aprender es qué son los operadores a nivel de bit.

- **&**  --> El operador [**AND**](https://es.wikipedia.org/wiki/Conjunci%C3%B3n_l%C3%B3gica). Al comparar dos bits, el resultado es un bit activo solo si los dos bits están activos. 
- |**  --> El operador [**OR**](https://es.wikipedia.org/wiki/Disyunci%C3%B3n_l%C3%B3gica) . Al comparar dos bits, el bit resultado esta activo si al menos uno de ellos también esta activo. 
- **^**  --> Operador [**XOR**](https://es.wikipedia.org/wiki/Disyunci%C3%B3n_exclusiva).
- **~**  --> **Negacion** de bit. Devuelve el valor opuesto de su bit.
- **`>>`** --> [Desplazamiento](https://en.wikipedia.org/wiki/Logical_shift) a la derecha.
- **<<** --> [Desplazamiento](https://en.wikipedia.org/wiki/Logical_shift) a la izquierda.


![bit_samples](src/truthTable.jpg)

# Paso a paso, bit a bit

Primero has de elegir el lenguaje con el que vas a crear tus bits.

**Elige un lenguaje de programación**
- ### [Python](Python/README.md) 
- ### [C++](C++/README.md) 

Si nunca te han explicado cómo funcionan los operadores a nivel de bit, te proporcionamos unas cuantas páginas de consulta para que puedas aprender por tu cuenta.

- **Numeros binarios** (https://brilliant.org/wiki/binary-numbers/)
- **Codificación binaria decimal BCD** (https://brilliant.org/wiki/binary-coded-decimal-or-bcd/)
- **Puertas lógicas** (https://brilliant.org/wiki/logic-gates/)
- **Manipulación de bits** (https://brilliant.org/wiki/bit-manipulation-hacks/)

Si lo que necesitas es aprender un poco de **Python** te recomendamos que consultes la siguiente [página con **cursos de Python gratuitos**](https://www.datacamp.com/courses/intro-to-python-for-data-science).


# Ejercicios propuestos

Dada una secuencia de unos y ceros cualesquiera almacenados en una dirección de memoria. Se pide:


- Contar cuantos bits son unos. **[15 puntos]**
- Detectar que un número es **impar** mediante operaciones con bits. **[10 puntos]
- **MSB (Most Significant bit )**. Encontrar la posición del primer bit con valor uno. **[10 puntos]**
- **LSB (Least Significant bit )**. Encontrar la posición del último bit con valor uno. **[10 puntos]**
- Codificación de formato de color **RGB888**. **[15 puntos]**
- Codificación de formato de color **RGB565**. **[20 puntos]**
- Obtener la operación que habría que realizar para obtener el resultado de la siguiente imagen. **[20 puntos]**
![bitWise_Comparison](src/bitwiseComparison.png)
- \***Desplazamiento circular**. Cuando se desplaza un bit, se pierde información en uno de los extremos. El desplazamiento circular se basa en recuperar la información perdida en un extremo para que aparezca en el extremo contrario. **[+20 puntos]**