# Reference

> [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)<br>
> [My Blog](https://zacks.one/udacity-data-engineering/)

---

# Index

## Stage 1: Text Processing

### [Cleaning Practice](./cleaning_practice.ipynb)

---

### [Normalization Practice](./normalization_practice.ipynb)

---

### [Tokenization Practice](./tokenization_practice.ipynb)

---

### [Stop Words Practice](./stop_words_practice.ipynb)

---

### [Pos Ner Practice](./pos_ner_practice.ipynb)

---

### [Stem Lemmatize Practice](./stem_lemmatize_practice.ipynb)

---

### Sample Pipeline for Text Processing

```py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words("english")
stemmer = PorterStemmer()


def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)
    
    # lemmatize and remove stop words
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]

    return tokens

# initialize count vectorizer object
countVectorizer = CountVectorizer(tokenizer=tokenize)
```

[View more](./bow_tfidf_lesson.ipynb)

---

## Stage 2: Feature Extraction

---

### [Bow Tfidf Lesson](./bow_tfidf_lesson.ipynb)

---

### [Bow Tfidf Practice](./bow_tfidf_practice.ipynb)
