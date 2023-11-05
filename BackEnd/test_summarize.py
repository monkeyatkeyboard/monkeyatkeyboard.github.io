## Will not be used 
## Can be deeleted 

def Summarize2(input_text): 
    #from __future__ import absolute_import
    #from __future__ import division, print_function, unicode_literals

    # import sumy
    from sumy.parsers.html import HtmlParser
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words


    LANGUAGE = "english"
    SENTENCES_COUNT = 10

    #url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = summarizer(parser.document, SENTENCES_COUNT)
    
    # Turn struct sentence into str, joining them by a space
    return ' '.join([str(sentence) for sentence in summary])
