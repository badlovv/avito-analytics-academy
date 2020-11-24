from typing import List
from collections import Counter
from math import log


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


def tf_transform(c_mat):
    return [[round(f / sum(text), 3) for f in text] for text in c_mat]


def idf_transform(c_mat):
    def idf(all_docs, docs_with_word):
        return round(log((all_docs + 1) / (docs_with_word + 1)) + 1, 1)

    docs_cnt = len(c_mat)
    docs_with_words = [0] * len(c_mat[0])
    idf_index = []
    for i, word_cnts in enumerate(c_mat):
        docs_with_words = [docs_with_words[i] + 1 * (word_cnts[i] > 0) for i in range(len(c_mat[0]))]
    idf_index = [idf(docs_cnt, docs_with_word) for docs_with_word in docs_with_words ]
    return idf_index


class TfidfTransformer:

    @staticmethod
    def tf_transform(c_mat):
        return [[round(f / sum(text), 3) for f in text] for text in c_mat]

    @staticmethod
    def idf_transform(c_mat):
        def idf(all_docs, docs_with_word):
            return round(log((all_docs + 1) / (docs_with_word + 1)) + 1, 1)

        docs_cnt = len(c_mat)
        docs_with_words = [0] * len(c_mat[0])
        idf_index = []
        for i, word_cnts in enumerate(c_mat):
            docs_with_words = [docs_with_words[i] + 1 * (word_cnts[i] > 0) for i in range(len(c_mat[0]))]
        idf_index = [idf(docs_cnt, docs_with_word) for docs_with_word in docs_with_words]
        return idf_index

    def fit_transform(self, c_mat):
        tf = self.tf_transform(c_mat)
        idf = self.idf_transform(c_mat)
        return [[round(tf_[i] * idf[i], 3) for i in range(len(tf_))] for tf_ in tf]


class TfidfVectorizer(CountVectorizer):

    def fit_transform(self, corpus):
        c_mat = CountVectorizer().fit_transform(corpus)
        return TfidfTransformer().fit_transform(c_mat)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()

    count_matrix = vectorizer.fit_transform(corpus)

    tf = tf_transform(count_matrix)
    print(tf)

    idf = idf_transform(count_matrix)
    print(idf)

    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)

    transformer = TfidfVectorizer()
    tfidf_matrix = transformer.fit_transform(corpus)
    print(tfidf_matrix)
