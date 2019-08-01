# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:11:38 2019

@author: KUS
"""

from flask import Flask,request,url_for,render_template
from flask_bootstrap import Bootstrap

# for NLP
from textblob import TextBlob,Word
import random
import time

app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse',methods = ['POST'])
def analyse():
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        
        # NLP STUFF STARTS HERE
        blob = TextBlob(rawtext)
        received_text2 = blob
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        num_tokens = len(list(blob.words))
        nouns =list()
        for word,tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())
                len_of_words = len(nouns)
                rand_words = random.sample(nouns,len(nouns))
                final_word = list()
                for item in rand_words:
                    word = Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    final_time = end - start
        
    return render_template('index.html',received_text = received_text2, num_tokens = num_tokens, 
                           blob_sentiment = blob_sentiment, blob_subjectivity = blob_subjectivity,
                           summary = summary, final_time = final_time)







if(__name__ == '__main__'):
    app.run(debug=True)