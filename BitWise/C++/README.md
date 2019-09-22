# ¿Cuántos bits son un byte?

Un [bit](https://es.wikipedia.org/wiki/Bit) es la unidad más pequeña de información que puede contener un sistema digital y solo puede contener **dos estados**.

- 1 ó 0
- ON ó OFF
- Activo o inactivo
- Encendido o apagado

Para poder crear más números se utiliza un conjunto de bits ordenados, que serán representados por un **número binario**, convirtiendo su escala a un **sistema decimal** que es el que solemos utilizar para realizar cálculos.


Los bits se pueden ordenar con un conjunto de **8 bits** a la que denominaremos **Byte**.

![Representacion de bytes](/BitWise/src/SampleByte.jpg)

Con todos estos bytes podemos formados por ceros y unos podemos representar cualquier tipo de dato en nuestro ordenador, números , letras incluso colores. Solamente hay que saber codificar este tipo de información. 
[**Conversor binario a decimal**](https://calculadorasonline.com/calculadora-binaria/)
En el siguiente [**enlace**](https://es.wikihow.com/convertir-binario-a-decimal) se puede observar paso a paso como se puede convertir un número binario a decimal.

# [Empezamos a programar en C++](https://repl.it/languages/cpp) 

**Has elegido el lenguaje de C++**. Este lenguaje es el más apropiado para crear **robots** y es el lenguaje con el que podrás aprender a usar **Arduino**. Si te gusta la **robótica** puedes consultar nuestro [curso de robótica con **Arduino**](https://github.com/ZGZMakerSpace/ArduinoCourse) en el siguiente [enlace](https://zaragozamakerspace.com/index.php/courses/curso-basico-arduino/).

### [Haz **Click aquí** para programar en C++](https://repl.it/languages/cpp) 

Un **numero binario**, siempre debe acompañarse primero de un **0** y una **b** ( correspondiente a **binario** ) seguida de la secuencia de **1's** y **0's** de nuestro ejemplo.
Para hacer aparecer por pantalla la codificación de un numero hay que llamar a la función **print** con la codificación del numero con el metodo [**bin()**](https://www.cprogramming.com/tutorial/bitwise_operators.html). Puedes observar a qué número se corresponde con la función **str()**. ¿Cuál es el número máximo que puedes obtener en un byte?

```cpp
#include <iostream>
#include <bitset>

unsigned int x = { 0b11001000 };

int main() {
  
  std::cout << "Byte: " << std::bitset<8>(x) << "\n";
  std::cout << "Numero: " << x;
  
}
```
## El inverso
Para hacer el inverso de un número binario podemos utilizar el símbolo **~**. En teoría el resultado de ejecutar este operador debería corresponder con la siguiente imagen.

![Inverso de un byte](/BitWise/src/InverseSampleByte.jpg)

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t x = { 0b11001000 };

int main() {
  
  std::cout << "Byte: " << std::bitset<8>(~x) << "\n";  //00110111
  std::cout << "Numero: " << ~x;     //-201 ¿?
  
}
```

Esta solución no es la correcta y se debe a que el número que hemos introducido contiene una codificación que afecta también a los números negativos. Para solucionar este caso vamos a definir el rango de los números enteros a enteros po


```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t x = { 0b11001000 };

int main() {
  
  std::cout << "Byte: " << std::bitset<8>(~x) << "\n";
  std::cout << "Numero: " << uint8_t(~x);
  
}
```

Ahora podemos comprobar que el resultado es correcto a la **operación de inversión**. Los ceros a la izquierda no tienen relevancia.

Para utilizar los operadores a nivel de bit, necesitamos comparar uno respecto de otro. A uno lo llamaremos **code** y al otro lo llamaremos **seed**. Los resultados que nos deberán de aparecer serán los siguientes.

![bit_samples](/BitWise/src/truthTable.jpg)

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t code = { 0b11001000 };
uint8_t seed = { 0b01101101 };
int main() {
  std::cout << "Code: " << std::bitset<8>( code  ) << "\n";
  std::cout << "Seed: " << std::bitset<8>( seed ) << "\n";
  std::cout << "AND: " << std::bitset<8>( code & seed ) << "\n";
  std::cout << "OR: " << std::bitset<8>( code | seed ) << "\n";
  std::cout << "XOR: " << std::bitset<8>( code ^ seed ) << "\n";  
} 
```

¿Sabrías decir cuál es el resultado de las siguientes operaciones?

- **code & \~code = ?**
- **code | \~code = ?**

¿Te salen bien los resultados de la imagen de arriba? 
Si el resultado es correcto, ya has ganado **10 puntos**.

## Desplazando bits

Dentro de una secuencia de bits podemos desplazar todos los bits hacia la izquierda o hacia la derecha un número determinado de veces. Para ello usaremos el operador de **desplazamiento de bits** **<<** o **>>**.

Este desplazamiento es el equivalente a multiplicar o dividir por una potencia de **2 elevado a n**, siendo **n** el numero de desplazamientos.

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t code = { 0b11001000 };

int main() {
  std::cout << int(code) << "\n";
  std::cout << "Multiplicar por 2: " << int(code << 1) << " " << std::bitset<8>( code <<1 ) << "\n";
  std::cout << "Divide por 2 : " << int(code  >> 1 )<< " "  << std::bitset<8>( code >> 1 ) << "\n"; 
} 
```
Hay que tener en cuenta que en la lista de bits, la posición que ocupa el bit que aparece por la izquierda o por la derecha es un cero.

## Contando bits

Para contar bits, una acción que podemos realizar es realizar un **bucle** y desplazar el bit hacia la derecha hasta que se acaba. 


```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t code = { 0b11001000 };

int main() {

  int count = 0;
  while (code){
    count += code & 1;
    code >>= 1;
  }

  std::cout << "Total de bits activos: " << int(count) << " " ;
} 
```
Si prestamos atención, este programa afecta al valor total de nuestro código, ya que vamos eliminando información sobreescribiendo sobre él.

Muchas veces es útil desarrollar una función que nos pueda devolver el resultado que estamos buscando sin alterar esta variable.

Para crear una **función en C++**, debemos especificar la palabra **def** seguida de un nombre para la función. 

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t code = { 0b11001000 };

int contarBits( int n ){
  int count = 0;
  while (code){
    count += code & 1;
    code >>= 1;
  }
  return count;
}

int main() {

  std::cout << "Total de bits activos: " << int ( contarBits( code ) );
} 
```
Existe un formato de **ejecución de funciones** denominado **recursivo**. Este modelo permite ejecutarse una función a si misma hasta que deja de cumplir una condición determinada.
Aunque pueda parecer más difícil es una forma inteligente de encapsular ciertas operaciones para obtener un resultado más rápido.

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint8_t code = { 0b11001000 };

int contarBits( int n ){
  int count = 0;
  if (n != 0){
    //Su salida es la suma de un bit activo mas la ejecucion de si misma desplazada un bit
      
    return (n & 1) + contarBits(n >> 1) ;
  }else{
    return 0;
  }
}

int main() {

  std::cout << "Total de bits activos: " << int ( contarBits( code ) );
} 
```

## Bit Color

Uno de los secretos más codiciados de los bits es su codificación para representar unidades de información más grandes. Incluso podemos ocultar información oculta de forma matemática si sabemos manipularlos.

Una de las aplicaciones más divertidas es la **codificación de bits en colores**. Muchas de las pantallas que utilizamos disponen de un procesador que introduce la información de color en cada pixel para poder visualizar imágenes. Por lo que la unidad más pequeña que es el bit se transforma en algo mucho más grande.

Para realizar y programar gráficos en robótica utilizamos muchas veces pantallas TFT que podemos controlar a través de una librería especial para crear dibujos. Pero las pantallas requieren de mucha potencia de procesamiento.

Una forma de codificar colores es la conocida como [RGB ( RED , GREEN, BLUE )](https://es.wikipedia.org/wiki/RGB), que son 3 números con un valor máximo de **255**.

Su valor máximo es **255**, ya que para cada fragmento de color requiere de **1 byte = 2⁸ = 256**.

## RGB888

Por esa regla de 3, para representar cualquier combinación de color con estos 3 colores necesitaremos **3 bytes** o lo que es lo mismo 24 bits de información.

Con el siguiente código conseguiremos transformar un código de color RGB en formato binario. 
En este caso, usaremos un número entero para cada componente de 0 a 255 y debemos observar que internamente siguen siendo bits al usar operadores binarios.

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint32_t code;

uint8_t r = 255;
uint8_t g = 120;
uint8_t b = 67;

uint32_t BitColor( uint8_t r , uint8_t g , uint8_t b  ){
  return r <<16 | g << 8 | b;
}

int main() {
  code = BitColor( r, g, b );
  std::cout << "RGB888 Color: " << std::bitset<24> ( code ) ;
} 
```
Podemos usar el siguiente enlace [COLORES](https://htmlcolorcodes.com/es/) para observar el resultado que debemos obtener. En el programa anterior obtendremos el siguiente color.

![Color_Sample](/BitWise/src/ColorSample.png)

Ahora nuestro objetivo es crear un programa que nos pueda proporcionar las 3 componentes RGB del color a partir de nuestra codificación en bits RGB888.

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint32_t code = { 0b111111110111100001000011 };

uint8_t r; // = 255;
uint8_t g; // = 120;
uint8_t b; // = 67;

int main() {
  // Escribe las instrucciones para obtener los valores anteriores a partir de la codificación de color binaria
  std::cout << "RGB888 Color - r:" << r << " g:"<< g << " b: " << b  ;
} 
```
Para realizar este ejercicio, hay que saber desplazar los bits y eliminar la parte que no nos interesa del código. Partimos de un numero de 32 bits como aparece en la figura y hemos de realizar la siguiente conversión.

![RGB888](/BitWise/src/RGB888.png)

Recuerda que no existe una única solución.


## RGB565

Podemos hacer una reducción de esta codificación usando solo **2 bytes** mediante la codificación [**RGB565**](http://www.barth-dev.de/online/rgb565-color-picker/) con solo **16 bits** de información. Como podemos ver en la imagen, los 5 primeros bits corresponden al color **rojo**, los 6 de en medio corresponden al color **verde** y los 5 bits restantes corresponden al color **azul**. La conversión para pasar de codificación RGB888 a RGB565 se hace seleccionando unos bits determinados.

![RGB888](/BitWise/src/rgb888.jpg)

![RGB565](/BitWise/src/rgb565.jpg)

En la siguiente prueba deberás convertir el siguiente código RGB en formato binario de la misma manera que hemos realizado en el programa anterior, pero ahora debemos seleccionar nuestros bits de manera adecuada.

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint16_t code;

uint8_t r = 255;
uint8_t g = 120;
uint8_t b = 67;

uint32_t BitColor( uint8_t r , uint8_t g , uint8_t b  ){
  return (r >> 3)<< 11 | (g >>2) << 5 | (b >> 3 );
}

int main() {
  code = BitColor( r, g, b );
  std::cout << "RGB565 Color: " << std::bitset<16> ( code ) ;
} 

```

![RGB565](/BitWise/src/RGB565.png)

Ahora nuestro objetivo es crear un programa que nos pueda proporcionar las 3 componentes RGB del color a partir de nuestra codificación en bits. ¿Nos saldrán los mismos valores que en la codificación **RGB888** ?

```cpp
#include <iostream>
#include <stdint.h>
#include <bitset>

uint16_t code = { 0b1111101111001000 } ;

uint8_t r = 0;
uint8_t g = 0;
uint8_t b = 0;


int main() {
  
  r = (code >> 11);
  std::cout << int(r) <<"\n";
  code = code & 0b11111111111 ;
  std::cout << code <<"\n";
  g = code >> 6;
  code = code & 0b11111;
  b = code;

  std::cout << "RGB888 Color - r:" << int(r) << " g:"<< int(g) << " b: " << int(b)  ;
} 
```

La respuesta es que **no nos pueden dar los mismos valores que en el modo de codificación RGB888**, ya que perdemos bits de información, por lo que esos bits perdidos los desconocemos para determinar el valor total de cada componente de color.

## Conversor Hexadecimal

Para finalizar estas pruebas, vamos a convertir estos códigos en formato hexadecimal, ya que los colores suelen interpetrarse con un valor hexadecimal.

Para realizar este cambio solamente tendremos que usar el método**hex()** paraa obtener el código en en **base 16**.

```cpp
#include <iostream>
#include <stdint.h>

uint16_t code = { 0b1111101111001000 } ;

int main() {

  std::cout << "RGB888 Color : 0x" << std::hex << code ;
} 
```

## Por qué hay 6 bits para el color verde y solo 5 para el rojo y el azul

La respuesta a esta pregunta reside en que los ordenadores operan con **bytes** que son **paquetes de 8 bits**. En el caso de la traducción al color conviene que sea el menor número de bytes, ya que los sistemas de imagen utilizan un valor de color para cada pixel de nuestra pantalla y para optimizar memoria requiere que cada configuracion de color no ocupe demasiado.

Dos bytes son 16 bits que no es divisible por 3 en partes iguales, y para aprovechar toda la información debemos ocupar ese **bit perdido** a uno de las 3 componentes de color. ¿Pero a cual?

La respuesta reside en que [**nuestro ojo humano es mas sensible en la variación del color verde**](https://en.wikipedia.org/wiki/CIE_1931_color_space) respecto a las del color rojo y azul. Tal y como se ve en la figura, podemos observar la gama de colores y el color verde por longitudes de onda ocupa un mayor area. 

Al disponer de un bit adicional, podemos guardar más información contenida en el verde con respecto a los otros dos colores y adaptar las imágenes con mayor calidad adaptada a nuestros ojos.

![Color Cones Response](/BitWise/src/colorCones.png)



## El bit más significativo [MSB Most Significant Bit](https://es.wikipedia.org/wiki/Bit_m%C3%A1s_significativo)

**MSB ( Most Significant Bit)** es el bit que de acuerdo con su posición, se encuentra más a la izquierda.
Los bits específicos dentro de un número binario, a cada bit se le asigna un número de bit, creando un rango desde cero a n.
![Índice de un bit](/BitWise/src/IndexSampleByte.jpg)



## El bit menos significativo [LSB Least Significant Bit](https://es.wikipedia.org/wiki/Bit_menos_significativo)


Ahora vamos a crear una secuencia de bits más larga. Si utilizamos dos Bytes, entonces tendremos 16 bits para rellenar. Nuestro objetivo es contar cuantos bits activos tenemos en nuestra lista de unos y ceros.
