from typing import List
from collections import Counter


class CountVectorizer:
    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter
        self._frequency = Counter()
        self._feature_names = []
        self._text_arrays = []
        self.__names_mapping = {}

    def fit(self, texts: List[str], save_text=False):
        self._text_arrays = []
        names_frequency = Counter()
        for text in texts:
            words_list = text.lower().split(self.delimiter)
            names_frequency.update(words_list)
            if save_text:
                self._text_arrays.append(words_list)
        self._frequency = names_frequency
        self._feature_names = list(names_frequency.keys())
        self.__names_mapping = {name: index for index, name in enumerate(names_frequency.keys())}

    def transform(self, texts: List[str] = [], load_text=False) -> List[List[int]]:
        vectors = []
        if not load_text:
            for text in texts:
                words_list = text.lower().split(self.delimiter)
                self._text_arrays.append(words_list)
        for arr in self._text_arrays:
            word_counter = Counter(arr)
            string_vector = [0] * len(self._feature_names)
            for word in word_counter:
                try:
                    string_vector[self.__names_mapping[word]] = word_counter[word]
                except KeyError:
                    continue
            vectors.append(string_vector)
        return vectors

    def fit_transform(self, texts: List[str]) -> List[List[int]]:
        self.fit(texts, save_text=True)
        return self.transform(load_text=True)

    def get_feature_names(self) -> List[str]:
        return self.__str__()

    def get_feature_index(self, name: str) -> int:
        return self.__names_mapping[name]

    def __str__(self):
        return self._feature_names

    def __len__(self):
        return len(self._feature_names)

    def __iter__(self):
        return iter(self._frequency)

    def __getitem__(self, item):
        return self._frequency[item]

    def __contains__(self, item):
        return item in self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()

    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)

    vectorizer.fit(corpus)
    print(vectorizer.transform(['This is pasta Pomodoro with fresh ingredients', 'Pasta Carbonara with Parmesan']))

    print(vectorizer.get_feature_names())

    print(len(vectorizer))

    for el in vectorizer:
        print(f'{el}: {vectorizer[el]}')

    print(vectorizer.get_feature_index('pasta'))

    print('pasta' in vectorizer)
