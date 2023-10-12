import pandas as pd



class AccessData():
    def __init__(self,contentPath, answerPath, hashtagsPath, stopwordsPath) -> None:
        self.contentPath = contentPath
        self.answerPath = answerPath
        self.hashtagsPath = hashtagsPath
        self.stopWordsPath = stopwordsPath

    def setContentPath(self, path):
        self.contentPath = path
    def setAnswerPath(self,path):
        self.answerPath = path;

    def loadAllData(self):
        self.contentData = pd.read_excel(self.contentPath).values.flatten()
        self.answerData = pd.read_excel(self.answerPath).values.flatten()
        self.hashtagsData = pd.read_excel(self.hashtagsPath).values.flatten()
        self.stopWordsData = pd.read_excel(self.stopWordsPath).values.flatten()

    
    def loadContent(self):
        self.contentData = pd.read_excel(self.contentPath).values.flatten()
    def loadAnswer(self):
        self.answerData = pd.read_excel(self.answerPath).values.flatten()
    
    

    
    




