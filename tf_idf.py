

documents = ['the the universe has very many stars',
             'the galaxy contains many stars',
             'the cold breeze of winter made it very cold outside']

#first: tonkenized Words

dictOfWords = {}

for indx, sentence in enumerate(documents):
    tonkenizedWords = sentence.split(' ')
    dictOfWords[indx] = [(word, tonkenizedWords.count(word)) for word in tonkenizedWords]

#print(dictOfWords)

#second: remove duplicates
termFrequency = {}

for i in range(0,len(documents)):
    listOfNoDuplicates = []
    for wordFreq in dictOfWords[i]:
        if wordFreq not in listOfNoDuplicates:
            listOfNoDuplicates.append(wordFreq)
        termFrequency[i] = listOfNoDuplicates
# print("Removed Duplicates :")
# print(termFrequency)
# print("\n")

#Third: Nomalized term frequency
normalizedTermFrequency = {}
for i in range(0, len(documents)):
    #used dictOfWords to get full lenth of words
    sentence = dictOfWords[i]
    lenOfSentence = len(sentence)
    listOfNormalized = []
    for wordFreq in termFrequency[i]:
        normalizedFreq = wordFreq[1]/lenOfSentence
        listOfNormalized.append((wordFreq[0],normalizedFreq))
    normalizedTermFrequency[i] = listOfNormalized

# print("Calcalated MormalizedFreq : ")
# print(normalizedTermFrequency)
# print("\n")

#----Calcalate IDF
#First pull sentence together and tonkenize words
alldocuments = ''
for sentence in documents:
    alldocuments += sentence + ' '
alldocumentsTokenized = alldocuments.split(' ')
print("AlldocumentsTokenized :")
print(alldocumentsTokenized )
print("\n")




#Remove duplicates from tonkenizedWords
alldocumentsNodups = []
for word in alldocumentsTokenized:
    if word not in alldocumentsNodups:
        print(word)
        alldocumentsNodups.append(word)


#Calculate the number of documents where the term t appears
dictOfNumberOfDocumentsWithTermInside = {}
for index, voc in enumerate(alldocumentsNodups):
    count = 0
    for sentence in documents:
        if voc in sentence:
            count+=1
    dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)
print(dictOfNumberOfDocumentsWithTermInside)
