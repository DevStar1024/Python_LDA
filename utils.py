

from dataPrep import AccessData
from sklearn.preprocessing import OneHotEncoder

def processText(rt:AccessData):
    sentences = rt.contentData
    stopwords = rt.stopWordsData
    processedText = []
    for sentence in sentences:
        sentence = sentence.lower()
        temp = []
        wordlist = sentence.split(" ")
        for word in wordlist:
            if word.isalpha() != True:
                continue
            if word  not in stopwords:
                temp.append(word)
        processedText.append(temp)
    return processedText



def ProcessAnswers(rt:AccessData):
    answers = rt.answerData

    # Reshape the array to a column vector
    temp = answers.reshape(-1, 1)

    # Create an instance of the OneHotEncoder
    encoder = OneHotEncoder()

    # Fit and transform the array
    one_hot_encoded = encoder.fit_transform(temp)

    # Convert the sparse matrix to a dense array
    one_hot_encoded = one_hot_encoded.toarray()

    print(one_hot_encoded.shape)

    print(one_hot_encoded)




