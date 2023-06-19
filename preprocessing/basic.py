import csv
from typing import Union
import re


def read_csv_to_dictionary(file_path: str,
                           stopwords: Union[str, list] = "default",
                           limit: Union[str, int] = 5,
                           remove_noise: bool = True):
    """
        Read a CSV file and convert its contents to a dictionary.

        Args:
            file_path (str): The path to the CSV file.
            stopwords (Union[str, list], optional): A string or list of stopwords. Defaults to "default".
            limit (Union[str, int], optional): The maximum number of entries to read from the CSV file. Defaults to 5.
            remove_noise (bool, optional): A flag indicating whether to remove noise from the data (uses regex). Defaults to True.

        Returns:
            dict: A dictionary representation of the CSV file data.

    """
    result = []

    _stopwords = []
    if stopwords == "default":
        _stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                      'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
                      'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
                      'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
                      'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
                      'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
                      'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                      'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there',
                      'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
                      'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
                      'can', 'will', 'just', 'don', 'should', 'now']
    elif stopwords == "none":
        _stopwords = []
    else:
        _stopwords = stopwords

    with open(file_path, 'r', encoding='utf8') as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            dictionary = {
                "sentiment": row[0],
                "id": row[1],
                "date": row[2],
                "query": row[3],
                "user": row[4],
                "text": row[5],
            }

            if remove_noise:
                # Remove URLs
                dictionary["text"] = re.sub(r'http\S+|www\S+', '', dictionary["text"]).lower()

                # Remove non-ASCII characters
                dictionary["text"] = re.sub(r'[^\x00-\x7F]+', '', dictionary["text"])

                # Remove symbols
                dictionary["text"] = re.sub(r'[^\w\s]', '', dictionary["text"])

            filtered_out = [word for word in dictionary["text"].split() if word not in _stopwords]

            dictionary["text"] = " ".join(filtered_out)

            result.append(dictionary)

            if limit == "None":
                continue
            elif index == limit - 1:
                break

    return result[1:]


def bag_of_words(words: str):
    """
        Convert a string of words into a bag-of-words dictionary.

        Args:
            words (str): A string containing words.

        Returns:
            dict: A dictionary representing the bag-of-words, where the keys are unique words and the values are their frequencies.

    """
    string_list = words.split()

    dictionary = {}

    for word in string_list:
        count = string_list.count(word)

        dictionary[word] = count

    return dictionary


def list_unique_words(frequencies: list):
    """
        Extract unique words from a list of tweet frequencies.

        Args:
            frequencies (list): A list of dictionaries containing tweet frequencies.
                Each dictionary should have a "text" key representing the tweet text.

        Returns:
            list: A list of unique words extracted from the tweet texts.

    """
    unique_words = []

    for twit in frequencies:
        for word in twit["text"].split(" "):
            if word not in unique_words:
                unique_words.append(word)

    return unique_words


def save_frequencies(path: str, data, frequencies, save: bool=True):
    """
        Save tweet frequencies to a CSV file and update the input data with the corresponding dictionaries.

        Args:
            path (str): The path of the CSV file to save the data.
            data (list): A list of dictionaries representing tweet data.
            frequencies (list): A list of dictionaries containing tweet frequencies.
            save (bool, optional): Flag indicating whether to save the data to a file. Defaults to True.

        Returns:
            list: The updated list of dictionaries with the added "dictionary" key.

    """
    for index, twit in enumerate(data):
        twit["dictionary"] = frequencies[index]
    if save:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["sentiment", "id", "date", "query", "user", "text", "dictionary"])
            writer.writeheader()
            writer.writerows(data)

    return data
