# prog_data_sci_uoc

Este repositorio contiene los ejercicios para el PEC 4 del curso de Programación para Ciencia de Datos de la UOC.

## Descripción

En este curso, se exploran los fundamentos de la programación utilizando Python, centrándose en aplicaciones relacionadas con la ciencia de datos. Los ejercicios incluidos en este repositorio cubren los incisos 1 al 6 del PEC 4, y el inciso 7 se encuentra respondido en este README.

## Estructura del repositorio

El repositorio está organizado de la siguiente manera:

- `/preprocessing`: repositorio que contiene un archivo basic.py con las funciones básicas para pre-procesar texto para realizar análisis de sentimiento.
- `/text_analysis`: repositorio que contiene un archivo word_cloud.py con funciones relacionadas a la generación de nubes de palabras.
- `main.py`: archivo principal del repositorio.
- `/twitter_reduced`: carpeta con los datos procesados.
- `/data`: carpeta con los datos en crudo.

## Requisitos

Los requisitos se encuentran en el archivo requirements.txt.

## Instrucciones de uso

Para recorrer el PEC 4 de la mano de este repositorio, solo hace falta ejecutar el archivo llamando a la función correspondiente.

Por ejemplo, así se llama al ejercicio 1:

```
python main.py ejercicio_1
```
De la misma manera se puede llamar hasta el ejercicio 6.

Para recorrer todo el PEC 4 de una sola vez, se puede usar:

```
python main.py run_all
```
## Respuestas al ejercicio 7

- a. ¿Cuáles son las palabras más utilizadas en las críticas positivas?

Las palabras más usadas son "im", "good", "love", "like", "get", "day", "thanks", entre otras, que denotan sentimientos positivos. Resaltan las palabras "good" = "bueno" y "love" = "amar"/"amor"

![Figure_2_positive](https://github.com/Enrique-Manzo/prog_data_sci_uoc/assets/30445121/f984e53c-c913-404d-a0bc-bb1dd930d908)
![Figure_2_word_cloud_positive](https://github.com/Enrique-Manzo/prog_data_sci_uoc/assets/30445121/ce41a8f6-fd68-4e9f-bafa-c1bed21f6421)

  
- b. ¿Cuáles son las palabras más utilizadas en las críticas negativas?

Entre las críticas negativas, también tenemos palabras generales como "im" o "go", pero también palabras negativas como "dont" y seguido "like" ("no me gusta"),  "cant", y curiosamente la palabra "work".

![Figure_word_cloud_negative](https://github.com/Enrique-Manzo/prog_data_sci_uoc/assets/30445121/98ee2b6b-5670-4b7f-99cc-16be31d86aa8)
![Figure_1_negative](https://github.com/Enrique-Manzo/prog_data_sci_uoc/assets/30445121/94f14e0e-4d22-4718-9e80-9959298cc317)


- c. ¿Hay palabras que aparezcan tanto en las críticas positivas como en las negativas?
Sí, algunos ejemplos son "im", "go", get", "day", ya que son palabras bastante generales.

- d. A partir de la word cloud, ¿qué se puede deducir sobre el sentimiento general de cada grupo?
El grupo positivo resalta sentimientos como "good", "great", "love", "new", y "hope". También aparece entre las primeras palabras el término "twitter". Mientras que el grupo negativo tiene como principal término "work", y le siguen términos como "bad", "cant", "miss". "need". Creo que todos estamos un poco desgastados de tanto trabajar.

## Cobertura

La cobertura es bastante buena suponiendo que se recorre toda la PEC 4 de una sola vez. Para esto, he testeado con coverage.py usando la instrucción:

```
coverage run --source=. main.py run_all
```

Y una vez finalizado el análisis, podemos pedir el informe:

```
coverage report
```

![report](https://github.com/Enrique-Manzo/prog_data_sci_uoc/assets/30445121/44fd176c-8845-4aa0-a574-826d44114082)
