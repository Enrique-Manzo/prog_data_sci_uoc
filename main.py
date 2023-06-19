from preprocessing import *
from text_analysis.word_cloud import generate_word_cloud, plot_word_counts
import pandas as pd
import sys


def ejercicio_1():
    # Ejercicio 1.2
    print(read_csv_to_dictionary("twitter_reduced/twitter_reduced.csv", limit=5, remove_noise=False))


def ejercicio_2():
    # Ejercicio 2 | Preprocesado usando expresiones regulares y eliminación de stopwords
    twits = read_csv_to_dictionary("twitter_reduced/twitter_reduced.csv", limit="None")
    print(twits[:3])


def ejercicio_3():
    # Ejercicio 3 - Almacenar dictionarios de frecuencias en una lista
    twits = read_csv_to_dictionary("twitter_reduced/twitter_reduced.csv", limit="None")
    frequency_list = [bag_of_words(twit["text"]) for twit in twits]

    # Ejericio 3 Obtener palabras únicas de todo el dataset y guardarlas en una lista
    unique_words = list_unique_words(twits)

    # Ejercicio 3 Mostrar en pantalla los primeros cinco diccionarios
    print(frequency_list[0:5])

    # Ordenar alfabéticamente el vocabulario y mostrar los 10 primeros resultados
    print(sorted(unique_words)[0:10])


def ejercicio_4():
    # Guardar el dataset procesado en formato CSV en cada row el diccionario de frecuencias
    twits = read_csv_to_dictionary("twitter_reduced/twitter_reduced.csv", limit="None")
    frequency_list = [bag_of_words(twit["text"]) for twit in twits]
    data = save_frequencies(path="data/twitter_processed.csv", data=twits, frequencies=frequency_list, save=True)

    print(data[20])

    return data


def ejercicio_5():
    # 1. ¿Cuántos clusters tenemos en nuestro dataset?
    data = ejercicio_4()
    df = pd.DataFrame(data)
    print(f"La cantidad de clusters es:  {len(df['sentiment'].unique())}")

    # 2. ¿Tenemos elementos vacíos en las columnas text? Si es así,¿Qué porcentaje? Eliminar los elementos nulos
    empty_texts = df[df['text'].str.len() == 0]

    print(
        f"Sí, tenemos elementos vacíos. En total hay {len(empty_texts)} filas vacías. "
        f"El procentaje de textos vacíos es {round((len(empty_texts)/df.shape[0])*100, 2)}%"
    )

    # Eliminamos los elementos nulos
    clean_df = df.drop(empty_texts.index)

    # Generar un word cloud para cada cluster
    cluster_0_counts = generate_word_cloud(clean_df.to_dict("records"), "sentiment", "0")
    cluster_4_counts = generate_word_cloud(clean_df.to_dict("records"), "sentiment", "4")

    return cluster_0_counts, cluster_4_counts


def ejercicio_6():
    data = ejercicio_4()
    df = pd.DataFrame(data)
    empty_texts = df[df['text'].str.len() == 0]
    clean_df = df.drop(empty_texts.index)
    cluster_0_counts = generate_word_cloud(clean_df.to_dict("records"), "sentiment", "0", show=False)
    cluster_4_counts = generate_word_cloud(clean_df.to_dict("records"), "sentiment", "4", show=False)

    plot_word_counts(dict(cluster_0_counts.most_common(10)))
    plot_word_counts(dict(cluster_4_counts.most_common(10)))


def run_all():
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()


if __name__ == '__main__':
    globals()[sys.argv[1]]()
