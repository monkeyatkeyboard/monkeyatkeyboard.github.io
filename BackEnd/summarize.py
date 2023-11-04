#!/usr/bin/env python
# coding: utf-8




import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

#Input text for summarizing below:

text = """The theory of evolution by natural selection was conceived independently by Charles Darwin
 and Alfred Russel Wallace in the mid-19th century as an explanation for why organisms are adapted
 to their physical and biological environments. The theory was first set out in detail in Darwin's
 book On the Origin of Species. Evolution by natural selection is established by observable facts
 about living organisms: (1) more offspring are often produced than can possibly survive; (2) traits
 vary among individuals with respect to their morphology, physiology, and behaviour; (3) different traits
 confer different rates of survival and reproduction (differential fitness); and (4) traits can be passed
 from generation to generation (heritability of fitness). In successive generations, members of a
 population are therefore more likely to be replaced by the offspring of parents with favourable characteristics
 for that environment."""

print(text)

def Summarize(text):
    #pip install nltk
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    nltk.download('punkt')
    
    #tokenizing the text by word
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    #record how frequently each word appears
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    #tokenize the text by sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()


    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():            
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

Summarize(text)