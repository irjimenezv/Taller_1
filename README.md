# Taller-1
Primero que nada, muy buenos dias, tardes o noches, nos presentamos, somos Print("Los gatos de Schrodinger") y este es nuetro repo, aquí se hará evidencia de nuestro trabajo como equipo:D
# Punto #1 Quiz
En este apartado evidenciamos nuestros resultados en la evaluación << Python begginer >>, resultado Kevin: (Me tocó repetirla varias veces porque no sabía mucho)

![image](https://github.com/irjimenezv/Taller_1/assets/141859143/08cf4f85-40f3-44f3-a340-376284f6b3c0)

Resultado Ivan:

Ya con la prueba adjunta, procedemos con el desarrollo de los siguientes puntos propuestos en el taller.

# Punto #2
Aquí creamos el programa capaz de determinar que de 3 números reales, se sepa que numero es mayor de los 3 mismos, el funcionamientO es relativamente sencillo, ya que por medio del programa detecta automaticamente que numero es mayor a cual, sol hace falta condicionar bien el progama, en palabras mas programadoras:

I) El programa recopila tres números (x, y, z) que el usuario ingresa.

II) Luego, compara estos números en una serie de declaraciones condicionales if para determinar cuál de ellos es el mayor.

III) Cada declaración condicional if verifica si un número es mayor que los otros dos utilizando operadores de comparación (por ejemplo, x > y). Si la condición es verdadera, significa que ese número es el mayor y se muestra un mensaje que indica que ese número es el mayor.

IV) Si ninguno de los números es mayor que los otros dos, no se mostrará ningún mensaje.

![Punto_2](https://github.com/irjimenezv/Taller_1/assets/141859143/22a0f70a-ffd5-4053-b4d2-8b6a7ab23fca)

# Punto #3
Para determinar si un número es impar o no, podemos usar la funcion de residuo, es decir, que se divide entre dos y si el residuo es igual a 0, significa que el número ingresado es par, el caso contrario es cuando el número que ingresamos tiene un residuo diferente a 0, en esta situación el numero ya no sería par, por ende, el programa nos escribe que nuestro numero es impar:

I) El programa comienza solicitando al usuario que ingrese un número entero (x) utilizando la función input().

Luego, evalúa si el número ingresado (x) es par o impar utilizando una declaración condicional if.

En la línea if x % 2 == 0:, se calcula el residuo de la división de x entre 2 utilizando el operador %. Si el residuo es igual a 0, significa que x es divisible por 2 y, por lo tanto, es un número par. En este caso, se imprime un mensaje que indica que el número (x) es par.

Si el residuo de la división de x entre 2 no es igual a 0, la declaración else se ejecuta, lo que significa que x es un número impar. En este caso, se imprime un mensaje que indica que el número (x) es impar.

https://colab.research.google.com/github/irjimenezv/Taller_1/blob/main/Punto3.ipynb#scrollTo=fw1MBlnSw7nr&line=1&uniqifier=1

# Punto #4
Si queremos saber si un número es multiplo de otro basta con realizar un proceso bastante similar al anterior, aquí tenemos que definir un primer numero para que posteriormente sea divido por el segundo número, para determinar si es multiplo el residuo debe ser igual a 0, si no es así, se escribira que no es multiplo del primer numero:

El programa comienza solicitando al usuario que ingrese dos números reales (x e y) utilizando la función input(). Estos dos números se almacenan en las variables x e y.

Luego, el código evalúa si 'x' es un múltiplo de 'y' utilizando una declaración condicional if.

En la línea if x % y == 0:, se calcula el residuo de la división de x entre y utilizando el operador %. Si el residuo es igual a 0, significa que x es completamente divisible por y sin dejar ningún residuo, lo que indica que x es un múltiplo de y.

Si el residuo de la división de x entre y no es igual a 0, la declaración else se ejecuta, lo que significa que x no es un múltiplo de y. En este caso, se imprime un mensaje que indica que x no es múltiplo de y.

![Punto_4](https://github.com/irjimenezv/Taller_1/assets/141859143/0c4aa697-35ce-4e81-8e8c-f22bb3e4e3da)

# Punto #5
En este punto tenemos que crear un programa en el cual se tendrá que introducir 3 números reales, los dos primeros serán sumados y comparados con un tercer número tambien real, la razón de ser de este programa será determinar si la suma de los dos primeros números es mayor al tercero:

El programa comienza solicitando al usuario que ingrese tres números reales (x, y, z) utilizando la función input(). Estos tres números se almacenan en las variables x, y y z.

Luego, el código realiza una serie de comparaciones para determinar la relación entre la suma de x y y con respecto a z.

En la primera declaración condicional if x + y == z:, se verifica si la suma de x y y es igual a z. Si esta condición es verdadera, se imprime el mensaje "la suma x+y es igual a z".

Si la condición en el primer if no es verdadera, el programa pasa a la siguiente declaración condicional elif x + y > z:. En esta parte, se verifica si la suma de x y y es mayor que z. Si esta condición es verdadera, se imprime el mensaje "la suma x+y es mayor a z".

Si ninguna de las condiciones anteriores es verdadera, es decir, si la suma de x y y no es igual a z y tampoco es mayor que z, entonces se ejecuta la parte else, y se imprime el mensaje "la suma x+y es menor a z".

[![](https://mermaid.ink/img/pako:eNplkb9OwzAQh1_ldFMr0oktEkW0SdpKwFK2muEUu61FbCPHFuTfi7HyYri1AgU8_eT7_J3O12FpuMAU95V5K49kHTxlTN9NNlqW0kxns_lit9HOGu5LaeEa9OeHEtbUYAVVoob3BJoE2memIZwFhBew7PJQuGpgDi3cDrG0PJX6rewh290T1F7RmQkORY2xQN-WiD6aHvLuEr2BdrTlo6z4K5MHT9WFLB9dq39thf7VNgvkOsbiJ65iXE8KqadMY4JhfkWSh1_rTghDdxRKMExD5GRfGDI9BI68M9tGl5g660WC_pWTE5mkgyWF6Z6qOtwKLp2xD3EN520MX3NEfnI?type=png)](https://mermaid.live/edit#pako:eNplkb9OwzAQh1_ldFMr0oktEkW0SdpKwFK2muEUu61FbCPHFuTfi7HyYri1AgU8_eT7_J3O12FpuMAU95V5K49kHTxlTN9NNlqW0kxns_lit9HOGu5LaeEa9OeHEtbUYAVVoob3BJoE2memIZwFhBew7PJQuGpgDi3cDrG0PJX6rewh290T1F7RmQkORY2xQN-WiD6aHvLuEr2BdrTlo6z4K5MHT9WFLB9dq39thf7VNgvkOsbiJ65iXE8KqadMY4JhfkWSh1_rTghDdxRKMExD5GRfGDI9BI68M9tGl5g660WC_pWTE5mkgyWF6Z6qOtwKLp2xD3EN520MX3NEfnI)

![Punto_5](https://github.com/irjimenezv/Taller_1/assets/141859143/23371381-ca48-442f-92a2-a9eb40e38c5f)


# Punto #6
Ahora cambiando un poco del tema de números, nos vamos por el lado de las vocales y consonantes, en esta ocasión crearemos un programa que sea capaz de identidficar si la letra que nosotros introducimos es una vocal o consonante, para determinar esto basta con determinar cuales son las vocales (a, e, i, o y u), aunque tambien se podía dar solución por el modelos ASCI, nosotros elegimos esta manera. El resto de letras serán consideradas automaticamente como consonantes tal que:

El programa comienza solicitando al usuario que ingrese un carácter (string) utilizando la función input(). El carácter se almacena como una cadena (string) en la variable x.

Luego, el código evalúa si el carácter ingresado (x) es una vocal o una consonante utilizando una declaración condicional if.

En la línea if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":, se compara el carácter x con las letras "a", "e", "i", "o" y "u". Si x es igual a cualquiera de estas letras, la condición es verdadera y se ejecuta el bloque de código dentro del if. En este caso, se imprime el carácter x seguido del mensaje "es una vocal".

Si la condición en el if no es verdadera, se ejecuta la parte else del código, lo que significa que el carácter x no es igual a ninguna de las vocales mencionadas ("a", "e", "i", "o", "u"). En este caso, se imprime el carácter x seguido del mensaje "es una consonante".

[![](https://mermaid.ink/img/pako:eNpl0LFOw0AMBuBXsTwVKX2BDFS0aaQOsISt18HcufREYleXOxBK8u5YtAMSk3_Z32B7Qq-BscZzr1_-QinDa-PkaXWQ6KM-WFyvH7dOtseD5KSh-Jig55wIAvdAb-w5UIp6MmN052Q3deVOeASqgCFWoBWUzWJTQ_OLzs3xrypC4FVGFZLMpzvr4rz_xz7VU2-iMdE62d9Ku2qj2LpY4cBpoBjsqMkJgMN84YEd1hZt1Q-HThZzVLJ23-KxzqlwheUaKHMT6T3RgPWZ-tG6HGLW9Hz70u-zlh9ehmhV?type=png)](https://mermaid.live/edit#pako:eNpl0LFOw0AMBuBXsTwVKX2BDFS0aaQOsISt18HcufREYleXOxBK8u5YtAMSk3_Z32B7Qq-BscZzr1_-QinDa-PkaXWQ6KM-WFyvH7dOtseD5KSh-Jig55wIAvdAb-w5UIp6MmN052Q3deVOeASqgCFWoBWUzWJTQ_OLzs3xrypC4FVGFZLMpzvr4rz_xz7VU2-iMdE62d9Ku2qj2LpY4cBpoBjsqMkJgMN84YEd1hZt1Q-HThZzVLJ23-KxzqlwheUaKHMT6T3RgPWZ-tG6HGLW9Hz70u-zlh9ehmhV)

![Punto_6](https://github.com/irjimenezv/Taller_1/assets/141859143/2f8e4b00-bcd2-4ef5-b3b9-3d6d29359d91)


# Punto #7
Con el código que tenemos a conitnuación; haremos unos cálculos ya un poco mas avanzados, primero que todo pediremos al usuario que ingrese 5 números reales y en base a esos datos registrados se realizara en cáclulo de:
* La mediana
* El promedio
* Promedio multiplicativo
* Se ordenarán de mayor a menor
* Se ordenarán de menor a mayor
* La potencia del número elevado al número menor
* La raiz cubica del número menor


# Punto #8
El programa comienza solicitando al usuario que ingrese una frecuencia (frec) en forma de un número real (float) utilizando la función input(). Esta frecuencia representa la frecuencia de una onda electromagnética.

Luego, el código utiliza múltiples declaraciones condicionales if y elif  para evaluar la frecuencia ingresada y determinar en qué parte del espectro electromagnético se encuentra.

Cada declaración condicional compara la frecuencia ingresada (frec) con un rango específico de valores en orden ascendente, desde frecuencias muy bajas hasta muy altas. Si la frecuencia está dentro de uno de estos rangos, se ejecuta el bloque de código correspondiente.

El programa imprime un mensaje descriptivo indicando a qué parte del espectro electromagnético pertenece la frecuencia ingresada. Por ejemplo, si la frecuencia está en el rango de "30E3" (30,000) o menos, se considera "Muy Baja Frecuencia - Radio".

Si la frecuencia no coincide con ninguno de los rangos especificados en las declaraciones condicionales anteriores, no se ejecuta ninguna de ellas, y el programa no imprime ningún mensaje, ya que no se ha proporcionado un caso predeterminado.

![Punto_8](https://github.com/irjimenezv/Taller_1/assets/141859143/cba9ddeb-9f6b-42b5-850c-c2f5d1b92935)


# Punto #9
El programa solicita al usuario que ingrese el nombre de un país de Sudamérica utilizando la función input(). El nombre del país se almacena como una cadena (string) en la variable x.

Luego, el código utiliza múltiples declaraciones condicionales if y elif  para comparar la cadena ingresada (x) con los nombres de varios países de Sudamérica.

Cada declaración condicional compara la cadena ingresada (x) con el nombre de un país específico. Si la cadena coincide con el nombre de un país en la lista, se ejecuta el bloque de código correspondiente y se imprime la capital de ese país.

Si la cadena ingresada no coincide con ningún país en la lista especificada en las declaraciones condicionales, se ejecuta la parte else del código y se imprime "pais no identificado" para indicar que el país ingresado no se encontró en la lista.

https://colab.research.google.com/github/irjimenezv/Taller_1/blob/main/Punto9.ipynb#scrollTo=1qPxKv52uLRM&line=1&uniqifier=1

# Punto #10
El programa comienza solicitando al usuario que ingrese una distancia en metros utilizando la función input(). La distancia ingresada se almacena como un valor de punto flotante (float) en la variable distancia.

Luego, el código calcula el tiempo que le tomaría a la luz recorrer la distancia ingresada. Para esto, divide la distancia por la velocidad de la luz, que es de aproximadamente 299,792,458 metros por segundo. El resultado se almacena en la variable t_vLuz.

Se imprime el tiempo calculado en la primera parte del código, indicando que es el tiempo que le tomaría a la luz recorrer la distancia ingresada.

A continuación, se calcula el tiempo que le tomaría al sonido recorrer la misma distancia. Se divide la distancia por la velocidad del sonido en el aire, que es de aproximadamente 343.2 metros por segundo. El resultado se almacena en la variable t_vSonido.

Se imprime el tiempo calculado en la segunda parte del código, indicando que es el tiempo que le tomaría al sonido recorrer la distancia ingresada.

Luego, se calcula el tiempo que le tomaría al vehículo comercial más rápido (SSC Tuatara) recorrer la distancia. Se divide la distancia por la velocidad de este vehículo, que es de aproximadamente 141.111 metros por segundo. El resultado se almacena en la variable t_vAuto.

Se imprime el tiempo calculado en la tercera parte del código, indicando que es el tiempo que le tomaría al vehículo comercial más rápido recorrer la distancia ingresada.

Finalmente, se calcula el tiempo que le tomaría al corredor Usain Bolt recorrer la distancia. Se divide la distancia por la velocidad de Usain Bolt, que es de aproximadamente 11.6667 metros por segundo. El resultado se almacena en la variable t_vBolt.

Se imprime el tiempo calculado en la última parte del código, indicando que es el tiempo que le tomaría a Usain Bolt recorrer la distancia ingresada.

![Punto_10](https://github.com/irjimenezv/Taller_1/assets/141859143/d537e97c-48fb-471a-96be-5cb368a7d43f)

