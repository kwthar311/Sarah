import random
import json
import pickle
import torch
from sklearn.preprocessing import LabelEncoder
import numpy as np

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

def mapdep(result):
    if result=="not ones":
        res=0
    elif result=="less than one week":
        res=1
    elif result=="more than one week"   :
        res=2
    elif result=="mostly every day":
        res=3
    return res


def mapanx(result):
    if result=="Never":
        res=0
    elif result=="some days":
        res=1
    elif result=="More than half of the days"   :
        res=2
    elif result=="almost everyday":
        res=3
    return res











while True:
    # sentence = "do you use credit cards?"

    sentence = input("You: ")
    if sentence == "quit":
        break
    tag,prob=inputprocess(sentence)

    if(tag in ListDtage):
        countdepression+=1
    elif(tag in ListAtage):
        countanxiety+=1






    if(countdepression>3):
        countdepression=0
        filename_one1 = 'knn_model.sav'
        loaded_model1 = pickle.load(open(filename_one1, 'rb'))

        print(f"{bot_name}:  Can i ask you some questions? To ensure you are fine.")
        sentence = input("You: ")
        tag, p = inputprocess(sentence)
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    print(f"{bot_name}: {W}")
                    print(f"{bot_name}:{resdep}")
                    for i in range(len(ListQdep)):
                        print(f"{bot_name}: {ListQdep[i]}")
                        Listres.append(input("You: "))
                    for l in range(len(Listres)):
                        Listresnum.append(mapdep(Listres[l]))
                    result_rf = loaded_model1.predict(np.array(Listresnum).reshape(1,-1))
                    print(f"{bot_name}:{str(result_rf)}")

        else:
            print(f"{bot_name}: I do not understand ...")

    elif(countanxiety>2):
        countanxiety=0
        filename_two2 = 'knn_model1.sav'
        loaded_model2 = pickle.load(open(filename_two2, 'rb'))

        print(f"{bot_name}:  Can i ask you some questions? To ensure you are fine.")
        sentence = input("You: ")
        tag, p = inputprocess(sentence)
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    print(f"{bot_name}: {W}")
                    print(f"{bot_name}:{resanx}")
                    for i in range(len(ListQAnx)):
                        print(f"{bot_name}: {ListQAnx[i]}")
                        Listres.append(input("You: "))
                    for l in range(len(Listres)):
                        Listresnum.append(mapanx(Listres[l]))
                    result_rf = loaded_model2.predict(np.array(Listresnum).reshape(1,-1))
                    print(f"{bot_name}:{result_rf}")

        else:
            print(f"{bot_name}: I do not understand ...")

    else:
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: I do not understand ...")



