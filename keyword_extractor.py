from tqdm import tqdm
import numpy as np
import random, math, time
from scipy.special import psi
from preprocessing import preprocessing, maxItemNum
from retrieve_articles import retrieve_articles

docs, word2id, id2word = preprocessing()
    
# The number of documents we'll be using to train the model. 
N = len(docs)
# number of distinct terms
M = len(word2id)
# number of topics
T = 10
# iteration times of variational inference, judgment of the convergence by calculating likelihood is omitted
iterInference = 35
# iteration times of variational EM algorithm, judgment of the convergence by calculating likelihood is omitted
iterEM = 50

# initial value of hyperparameter alpha
alpha = 5
# sufficient statistic of alpha
alphaSS = 0

# the topic-word distribution (beta in D. Blei's paper)
# Passing the list [T,M] in as an argument for np.zeros creates a matrix of T-by-M zeros.
varphi = np.zeros([T, M])

# topic-word count, this is a sufficient statistic to calculate varphi
nzw = np.zeros([T, M])

# topic count, sum of nzw with w ranging from [0, M-1], for calculating varphi
nz = np.zeros([T])

# inference parameter gamma
gamma = np.zeros([N, T])
# inference parameter phi
phi = np.zeros([maxItemNum(N, docs), T])



def initializeLdaModel():
    for z in range(0, T):
        for w in range(0, M):
            nzw[z, w] += 1.0/M + random.random()
            nz[z] += nzw[z, w]
    updateVarphi()    

# update model parameters : varphi (the update of alpha is ommited)
def updateVarphi():
    for z in range(0, T):
        for w in range(0, M):
            if(nzw[z, w] > 0):
                varphi[z, w] = math.log(nzw[z, w]) - math.log(nz[z])
            else:
                varphi[z, w] = -100

# update variational parameters : gamma and phi
def variationalInference(docs, d, gamma, phi):
    phisum = 0

    #Creates an numpy array containing a list of zeros with length equal to the number of topics.
    oldphi = np.zeros([T])
    digamma_gamma = np.zeros([T])
    
    for z in range(0, T):
        gamma[d][z] = alpha + docs[d].wordCount * 1.0 / T
        digamma_gamma[z] = psi(gamma[d][z])
        for w in range(0, len(docs[d].itemIdList)):
            phi[w, z] = 1.0 / T
    
    
    for iteration in tqdm(range(0, iterInference)):
        for w in range(0, len(docs[d].itemIdList)):
            phisum = 0
            for z in range(0, T):
                oldphi[z] = phi[w, z]
                phi[w, z] = digamma_gamma[z] + varphi[z, docs[d].itemIdList[w]]
                if z > 0:
                    phisum = math.log(math.exp(phisum) + math.exp(phi[w, z]))
                else:
                    phisum = phi[w, z]
            for z in range(0, T):
                phi[w, z] = math.exp(phi[w, z] - phisum)
                gamma[d][z] =  gamma[d][z] + docs[d].itemCountList[w] * (phi[w, z] - oldphi[z])
                digamma_gamma[z] = psi(gamma[d][z])

# initialization of the model parameter varphi, the update of alpha is ommited
initializeLdaModel()

print("Checkpoint") #Track Preprocessing Progress

# variational EM Algorithm
for iteration in tqdm(range(0, iterEM)): 
    nz = np.zeros([T])
    nzw = np.zeros([T, M])
    alphaSS = 0
    # EStep
    for d in tqdm(range(0, N)):
        variationalInference(docs, d, gamma, phi)
        gammaSum = 0
        for z in range(0, T):
            gammaSum += gamma[d, z]
            alphaSS += psi(gamma[d, z])
        alphaSS -= T * psi(gammaSum)

        for w in range(0, len(docs[d].itemIdList)):
            for z in range(0, T):
                nzw[z][docs[d].itemIdList[w]] += docs[d].itemCountList[w] * phi[w, z]
                nz[z] += docs[d].itemCountList[w] * phi[w, z]

    
    # MStep
    updateVarphi()

# calculate the top 10 terms of each topic
topicwords = []
maxTopicWordsNum = 10
for z in range(0, T):
	ids = varphi[z, :].argsort()
	topicword = []
	for j in ids:
		topicword.insert(0, id2word[j])
	topicwords.append([topicword[0 : min(10, len(topicword))],j])


counter = 1
for item in topicwords:
    print(f"Topic {counter}: {item[0]}")
    counter+=1

#print(phi)
print('Complete.')



#Write results to file.
with open("results.txt","w+") as file:
    for index, item in enumerate(topicwords):
        file.write(f"Topic {index+1}: {item[0]} \n")
    for item in topicwords:    
        file.write('\n'+' '.join(item[0])+'\n')
        query = ' '.join(item[0])
        file.write(retrieve_articles(query))
        time.sleep(5)