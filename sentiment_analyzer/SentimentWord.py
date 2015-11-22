class SentimentWord:
    def __init__(self):
        self.words = []
        with open("SentiWordNet.txt", "r") as sentimentFile:
            for line in sentimentFile:
                content = line.split()
                if content[2] != '0' and content[3] != '0':
                    self.words.append((content[4].split('#')[0], float(content[2]), float(content[3])))
        sentimentFile.close()

    def get_words(self):
        return self.words
