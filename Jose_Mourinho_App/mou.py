import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle
import nltk
import random

#with open('logistic_model_app.sav', 'rb') as f:
 #   final_model = pickle.load(f)

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

with open('word_dist.pkl', 'rb') as f:
    words_freq = pickle.load(f)
with open('word_model.pkl', 'rb') as f:
    words = pickle.load(f)
with open('word_params.pkl', 'rb') as f:
    params = pickle.load(f)
test = nltk.pos_tag(words)

def make_doc(topic_num):
    #raise NotImplementedError
    sentence = []
    sentence.append('Mourinho')
    sent_ord = ['RB','RB','VB','JJ','NN']
    
    for i in range(5):
        #topic_num = np.random.choice(np.arange(0,3),p=topic_probs)
        topic = params[topic_num]
        stop=0
        while stop ==0:
            word_num = np.random.choice(np.arange(0,500),p=topic)
            #print((sent_ord[i],test[word_num][1]))
            if sent_ord[i] in test[word_num][1]:
                sentence.append(test[word_num][0])
                stop=1

    common_words = ['the','a']
    sentence.insert(4,random.choice(common_words))
    sentence.append('.')
    quote = str(sentence).replace(',',' ').replace('[','').replace(']','').replace("'",'')
    return quote

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("index.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    test = flask.request.json
    x = list(test)
    pos_tops = [0,1,6]
    neg_tops = [2,4,5]
    neut_tops = [3,7]
    if x[0] > x[1]:
        topp = random.choice(pos_tops)
    elif x[0]==x[1]:
        topp = random.choice(neut_tops)
    else:
        topp = random.choice(neg_tops)
    message = make_doc(topp)

    results = {"score": message}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)