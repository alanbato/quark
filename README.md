# quark
`Easy to use functional language.`
## Acerca de 
La visión detrás del proyecto es aprender cómo se diseña e implementa un lenguaje de programación y de la misma forma aprender más sobre los lenguajes funcionales. El objetivo del lenguaje es ayudar a las personas a aprender a programar utilizando el paradigma funcional debido a que la mayoría de las opciones que están disponibles hoy en día no son tan amigables con el usuario. La categoría del lenguaje es funcional tomando inspiración de lenguajes como Haskell, Elixir y Python (aunque el último no es funcional). El lenguaje como tal no es complicado y por ende su alcance va principalmente ligado con definición de módulos ya que son los que se utilizan para hacer condicionales y ciclos mediante recursión.

## Manual de usuario
### Tipos y operaciones
`quark` cuenta con los tipos tradicionales definidos:
* Int
* Bool
* Float
* String
* non (vacío)

De la misma forma se puede definir un nuevo tipo de la siguiente forma:
```
type Rect <- [Int];
```
Donde se especifica que ahora un rectángulo es un arreglo de enteros para denotar su tamaño.

Dentro de `quark` el operador `<-` es utilizado para realizar asignaciones ya que el operador `=` se utiliza para denotar igualdad en una comparación.
```
Int one <- 1;
Int three <- one + 2;
print(three);
# 3
print(one = three);
# False
```
Dentro de `quark` se cuenta con los operadores tradicionales para realizar operaciones matemáticas: `+, -, *, /, %, >, <, >=, <=, =, !=`. Es importante notar que si se realizan operaciones de dos `Int` el resultado será `Int`, mientras que si se realiza un `Int` y `Float`, el resultado será `Float`.

### Listas
En quark las listas no necesitan un tamaño definido ya que se crean conforme se van utilizando. Es importante notar que en quark las listas **solamente pueden ser de enteros**.
Para crear una nueva lista se puede realizar de la siguiente forma:
```
[Int] mi_lista <- [1, 2, 3, 4];
```
Se cuentan con 3 funciones definidas para la manipulación de listas:
```
head(mi_lista);
# 1
tail(mi_lista);
# [2, 3, 4]
append(mi_lista, [5, 6, 7]);
# [1, 2, 3, 4, 5, 6, 7]
```
Cada vez que se usa la función `tail` o `append` se crea una lista nueva, `head` regresa un entero.

### Funciones
En las funciones se encuentra la funcionalidad principal del lenguaje ya que se pueden usar para realizar ciclos por medio de la recursión y hacer uso de sus cláusulas condicionales para marcar el flujo del programa.
```
def factorial(n: Int) -> Int {
  (n <= 1) {
      1;
  }
  default {
      n * factorial(n-1);
  }
}

Int n <- 4;
Int res <- factorial(n);
print(res);
# 24
```
Cada función puede tener 0 o más claúsulas condicionales y una condición default, a la cual entrará si ninguna de las otras condiciones fueron verdaderas.
