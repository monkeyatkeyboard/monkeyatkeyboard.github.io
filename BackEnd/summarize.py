#!/usr/bin/env python
# coding: utf-8

def Summarize(text, percent):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    #nltk.download('punkt')
    from heapq import nlargest
    from string import punctuation
    
    stopWords = set(stopwords.words("english"))
    
    words = word_tokenize(text)
    
    sentences = sent_tokenize(text)


    if(percent >= 1):
        select_length = int(percent)
    elif(percent > 0):
        select_length = int(len(sentences) * percent)
    else:
        return "ERROR: Percent must be Positive!"


    freqTable = dict()
    
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in punctuation:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


    sentenceValue = dict()
    
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    summary = nlargest(select_length, sentenceValue, key=sentenceValue.get)
    final_summary = [word for word in summary]

    summary = ''.join(final_summary)
    
    return summary