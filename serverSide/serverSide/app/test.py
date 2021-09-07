




import random
import json
import pickle
import torch
from sklearn.preprocessing import LabelEncoder
import numpy as np
import mysql.connector
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

countdepression=0
countanxiety=0
ListDtage=["dQ1","dQ2","dQ3.1","dQ3.2","dQ4","dQ5.1","dQ5.2","dQ6","dQ7","dQ8","dQ9"]
ListAtage=["AQ1,6","AQ2,3","AQ4,5","AQ7"]
Listres=[]
Listresnum=[]
W="During the past two weeks, how many times have you been concerned about the following problems? :"
resdep="less than one week OR not ones OR mostly every day OR more than one week"
resanx="some days OR More than half of the days OR Never OR almost everyday"

ListQdep=["Lack of interest or listening in doing daily chores, such as household chores or watching TV.",
          "Feeling sad, distressed, or hopeless","Difficulty sleeping, interrupted sleep, or sleeping more than usual.",
          "Feeling tired or exhausted, even with the slightest effort.",
          "Lack of appetite or an increase in food intake than usual.",
          "Feeling after complacency or a feeling of failure or frustration.",
          "Difficulty concentrating, lack of absorption, or excessive forgetfulness.",
          "The slowdown in movement or less talkative than usual to a noticeable degree from others, or on the contrary, talking quickly and excessively.",
          "Have you ever felt so sad that you preferred death to life, or had thoughts of self-harm?"]

ListQAnx=["Feeling angry, anxious, or very emotional.","Inability to control or eliminate anxiety.","Excessive anxiety over various things.",
          "Difficulty relaxing.","The severity of the disturbance makes it difficult to remain calm.","Being easily irritated or Emotional."
          ,"Feeling frightened as if something terrible might happen."]

bot_name = "Sarah"
print("Let's chat! (type 'quit' to exit)")
def inputprocess(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    return tag,prob


startSurvey = 0

questionNum = 0

reply = 0

def serverReply(msg):
    
    global reply
    global countanxiety
    global countdepression
    global startSurvey
    global questionNum

    prob = 0.95

    if reply == 1:
        reply = 0
        Listres.append(msg)
        

    sentence = msg
    
    tag,prob=inputprocess(sentence)

    if(tag in ListDtage):
        countdepression+=1
    elif(tag in ListAtage):
        countanxiety+=1


    if(countdepression>3):
        if (startSurvey == 0):
            startSurvey =1
            return "depression"

       
        tag,prob=inputprocess(sentence)
        filename_one1 = 'knn_model.sav'
        loaded_model1 = pickle.load(open(filename_one1, 'rb'))

        if (sentence == 0 and startSurvey == 1 and questionNum == 0):
            return "endofsurvey"

        
        if prob.item() > 0.75:
            if questionNum >= len(ListQdep) - 1:
                countdepression = 0
                startSurvey = 0
                questionNum = 0
                Listres.clear()
                return "endofsurvey"

            reply = 1
            questionNum += 1
            return ListQdep[questionNum]

        else:
            return "I do not understand ..."

    else:
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        else:
            return "I do not understand ..."






