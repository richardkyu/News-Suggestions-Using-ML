from tqdm import tqdm
from split_into_sentences import split_into_sentences
import numpy as np
import codecs, jieba, re, random, math
from scipy.special import psi


# wordCount : the number of total words (not terms)
# itemIdList : the list of distinct terms in the document
# itemCountList : the list of number of the existence of corresponding terms

class Document:
    def __init__(self, itemIdList, itemCountList, wordCount):
        self.itemIdList = itemIdList
        self.itemCountList = itemCountList
        self.wordCount = wordCount
        

# Preprocessing - filter out stopwords, handle segmentation, and use the class Document to represent all documents in the text sample.
def preprocessing():
    
    # read in all stopwords to be filtered out.
    file = codecs.open('stopwords.dic','r','utf-8')
    stopwords = [line.strip() for line in file]
    #print(stopwords)
    file.close()
    
    # the document to read and produce topics from
    with open('sample.txt','r') as fh:
        all_lines = fh.readlines()
        str_all_lines = ' '.join(all_lines).replace('\n','')
    raw_documents = split_into_sentences(str_all_lines)
    
    # Check that sentence splitting has worked.
    # print(raw_documents)

    # Group 4 sentences as a document.
    documents = []
    i=0
    while i < len(raw_documents)-4:
        documents.append(raw_documents[i]+'\n'+raw_documents[i+1]+raw_documents[i+2]+'\n'+raw_documents[i+3]+'\n')
        i+=4
    
    
    docs = []
    word2id = {}
    id2word = {}
    
    currentWordId = 0
    for document in documents:
        #word2Count is a dictionary, essentially a hashmap with the number of occurrences of each word in a sentence.
        word2Count = {}

        # Create generator objects for each word in the string, cuts on whole words and punctuation.
        segList = jieba.cut(document)
        
        for word in segList: 
            word = word.lower().strip()
            
            # Get rid of items that are punctuation, numbers, or stopwords.
            if len(word) > 1 and not re.search('[0-9]', word) and word not in stopwords:
                if word not in word2id:
                    word2id[word] = currentWordId
                    id2word[currentWordId] = word
                    currentWordId += 1
                if word in word2Count:
                    word2Count[word] += 1
                else:
                    word2Count[word] = 1
        itemIdList = []
        itemCountList = []
        wordCount = 0

        for word in word2Count.keys():
            itemIdList.append(word2id[word])
            itemCountList.append(word2Count[word])
            wordCount += word2Count[word]
            
        docs.append(Document(itemIdList, itemCountList, wordCount))

    return docs, word2id, id2word


def maxItemNum(N, docs):
    num = 0
    for d in range(0, N):
        if len(docs[d].itemIdList) > num:
            num = len(docs[d].itemIdList)
    return num