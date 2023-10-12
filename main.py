from dataPrep import AccessData
from utils import processText, ProcessAnswers
from gensim import corpora
from gensim.models import LdaModel
import gensim

if __name__ == "__main__":
    rt = AccessData(contentPath="./content.csv", answerPath='./answer.csv',hashtagsPath="hashtags.csv",stopwordsPath="./stopwords.csv")
    rt.loadAllData()
    txts = processText(rt)
    dictionary = corpora.Dictionary(txts)
    corpus = [dictionary.doc2bow(text) for text in txts]
    #ProcessAnswers(rt)
    
    
    lda_model = LdaModel(corpus=corpus,
                     id2word=dictionary,
                     num_topics=100,  # specify the number of topics
                     random_state=42,
                     passes=10)  # specify the number of passes/iterations

    # Print the topics as words
    topics = lda_model.print_topics(num_topics=100, num_words=10)  # Adjust the number of words to display per topic

    for topic_id, topic in topics:
        words = [word for word, _ in lda_model.show_topic(topic_id)]
        print(f"Topic {topic_id}: {words}")
    #doc_topics = lda_model.get_document_topics(corpus[0])
   