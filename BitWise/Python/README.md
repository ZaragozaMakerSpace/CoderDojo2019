# Como crear un byte en python

Un [bit](https://es.wikipedia.org/wiki/Bit) es la unidad más pequeña de información que puede contener un sistema digital y solo puede contener dos estados.

- 1 ó 0
- ON ó OFF
- Activo o inactivo
- Encendido o apagado


[Video de bit de la película Tron (1982) ](https://www.youtube.com/watch?v=2OgWHeQ0UlY)


Para poder crear más números se utiliza un conjunto de bits ordenados, que serán representados por un número binario, convirtiendo su escala a un sistema decimal que es el que solemos utilizar para realizar cálculos.


Los bits se pueden ordenar con un conjunto de 8 bits a la que denominaremos **Byte** 

![Representacion de bytes](src/SampleByte.jpg)

Un numero binario, siempre debe acompañarse primero de un 0 y una b ( correspondiente a binario ) seguida de la secuencia de 1's y 0's de nuestro ejemplo.
Para hacer aparecer por pantalla la codificación de un numero hay que llamar a la función print con la codificación del numero con el metodo [bin()](https://wiki.python.org/moin/BitManipulation). Puedes observar a qué número se corresponde con la función str(). ¿Cuál es el número máximo que puedes obtener en un byte?

```python
print( 'Byte: ' + bin( 0b11001000 ) )
print( 'Numero: ' + str( 0b11001000  ))	#200
```
#El inverso
Para hacer el inverso de un número binario podemos utilizar el símbolo **~**. En teoría el resultado de ejecutar este operador debería corresponder con la siguiente imagen.

![Inverso de un byte](src/SampleByte.jpg)

En python 
```python
code =  0b11001000
print( 'Byte: ' + bin( ~code ) )	#-0b11001001
print( 'Numero: ' + str( ~code  )) 	#-201 ?¿?¿
```

Esta solución se debe a que el número que hemos introducido contiene una codificación que afecta también a números negativos. Para solucionar este caso vamos a crear un número unsigned int de 8 bits con la librería [numpy](https://numpy.org/). [numpy](https://numpy.org/) es una librería muy útil para realizar cálculos numéricos en Python con una extensión completa para realizar matemáticas.


```python
import numpy as np

code = np.uint8( 0b11001000 )
print( 'Byte: ' + bin( ~code ) )	#0b110111
print( 'Numero: ' + str( ~code  ))	#55
```

Ahora podemos comprobar que el resultado es correcto a la operación de iversión. Los ceros a la izquierda no tienen relevancia.

Para utilizar los operadores a nivel de bit, necesitamos compararlo respecto a dos bytes. A uno lo llamaremos **code** y al otro lo llamaremos **seed**. Los resultados que nos deberán de aparecer serán los siguientes.

![bit_samples](src/truthTable.jpg)

```python
import numpy as np

code = np.uint8( 0b11001000 )
seed = np.uint8( 0b01101101 )

print( 'Code: ' + bin( code ) )
print( 'seed: ' + bin( seed ) )
print( 'AND: ' + bin( code & seed  ))
print( 'OR: ' + bin( code | seed  ))
print( 'XOR: ' + bin( code ^ seed  ))
```

¿Sabrías decir cuál es el resultado de las siguientes operaciones?

- code & \~code = ?
- code | \~code = ?


#El bit más significativo [MSB Most Significant Bit](https://es.wikipedia.org/wiki/Bit_m%C3%A1s_significativo)

MSB ( Most Significant Bit) es el bit que de acuerdo con su posición, se encuentra más a la izquierda
Los bits específicos dentro de un número binario, a cada bit se le asigna un número de bit, creando un rango desde cero a n.

#El bit menos significativo [LSB Least Significant Bit](https://es.wikipedia.org/wiki/Bit_menos_significativo)


![Índice de un bit](src/IndexSampleByte.jpg)

