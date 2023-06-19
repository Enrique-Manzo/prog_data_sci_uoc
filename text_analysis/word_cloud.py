import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Union
from collections import Counter


# Reference https://www.datacamp.com/tutorial/wordcloud-python
def generate_word_cloud(data: list, cluster_name: str, cluster_to_use: Union[str, int], show: bool=True):
    """
        Generate a word cloud from text data based on a specific cluster in the data.

        Args:
            data (list): A list of dictionaries representing the text data.
            cluster_name (str): The name of the cluster field in the dictionaries.
            cluster_to_use (Union[str, int]): The value of the cluster to use for generating the word cloud.
            show (bool, optional): Flag indicating whether to display the word cloud. Defaults to True.

        Returns:
            Counter: A Counter object containing the word counts for the selected cluster.

    """

    text = ""

    for item in data:
        if item[cluster_name] == cluster_to_use:
            text += item["text"]

    word_counts = Counter(text.split())

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    if show:
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    return word_counts


def plot_word_counts(counts: dict):
    """
        Plot the word counts using a bar chart.

        Args:
            counts (dict): A dictionary containing word counts, where the keys are words and the values are their frequencies.

        Returns:
            None

    """

    plt.bar(counts.keys(), counts.values())
    plt.show()
