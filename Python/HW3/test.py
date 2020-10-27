from transformers import CountVectorizer

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
print('tomato' in vectorizer)

