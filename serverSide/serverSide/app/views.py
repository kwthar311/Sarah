from app import app

from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta, datetime
import mysql.connector
import os

##################### ML Model ####################
import random
import json
import pickle
import torch
from sklearn.preprocessing import LabelEncoder
import numpy as np

from .model import NeuralNet
#from ./nltk_utils import bag_of_words, tokenize
from .nltk_utils import bag_of_words, tokenize
from datetime import datetime

#===============================
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('C:\\Users\\kwtha\\PycharmProjects\\serverSide\\app\\intents.json', 'r') as json_data:
    intents = json.load(json_data)

#F0ILE = .data
data = torch.load("C:\\Users\\kwtha\\PycharmProjects\\serverSide\\app\\data.pth")

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

todat_date=""
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

questionNum_d= 0
questionNum_a= 0
reply = 0

def serverReply(msg):
    
    global reply
    global countanxiety
    global countdepression
    global startSurvey
    global questionNum_d
    global questionNum_a

    #prob = 0.95

    if reply == 1:
        reply = 0
        Listres.append(msg)
        print("The list res : ")
        print(Listres)
        

    sentence = msg

    tag, prob = inputprocess(sentence)
    if tag in ListDtage:
        countdepression+=1
    elif tag in ListAtage:
        countanxiety+=1
    elif tag.__eq__("date"):
        todat_date = datetime.today().strftime('%Y-%m-%d')
        print(todat_date)

    #if msg == "startDepression":
    #    countdepression = 4


    if(countdepression>3 and countanxiety<3):
        countanxiety =0
        if (startSurvey == 0):
            startSurvey =1
            return "depression"

       
        

        if (sentence == '0' and startSurvey == 1 and questionNum_d == 0):
            countdepression = 0
            startSurvey = 0
            return "endofsurvey"

        filename_one1 = 'C:\\Users\\kwtha\\PycharmProjects\\serverSide\\app\\knn_model.sav'
        loaded_model1 = pickle.load(open(filename_one1, 'rb'))

        tag, prob = inputprocess(sentence)

        print(questionNum_d)
        if questionNum_d >= len(ListQdep):
                countdepression = 0
                startSurvey = 0
                questionNum_d = 0
                test_list = [int(i) for i in Listres]
                print(test_list)
                print(np.array(test_list).reshape(1,-1))
                result_rf = loaded_model1.predict(np.array(test_list).reshape(1,-1))
                return "endofsurvey : {0}".format(result_rf)
        else:
                reply = 1
                questionNum_d += 1
                return ListQdep[questionNum_d-1]



    elif(countanxiety>3 and countdepression<3):
        print("int in counters\n")
        print(countanxiety)
        print(countdepression)
        countdepression =0
        if (startSurvey == 0):
            startSurvey =1
            return "anxity"
 

        if (sentence == '0' and startSurvey == 1 and questionNum_a == 0):
            countanxiety = 0
            startSurvey = 0
            return "endofsurvey"

        filename_one1 = 'C:\\Users\\kwtha\\PycharmProjects\\serverSide\\app\\knn_model1.sav'
        loaded_model1 = pickle.load(open(filename_one1, 'rb'))

        tag, prob = inputprocess(sentence)

        print(questionNum_a)

        if questionNum_a >= len(ListQAnx):
                countanxiety = 0
                startSurvey = 0
                questionNum_a = 0
                test_list = [int(i) for i in Listres]
                print(test_list)
                print(np.array(test_list).reshape(1,-1))
                result_rf = loaded_model1.predict(np.array(test_list).reshape(1,-1))
                return "endofsurvey : {0}".format(result_rf)
        else:
            reply = 1
            questionNum_a += 1
            return ListQAnx[questionNum_a-1]


    else:
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    if tag.__eq__("date"):
                        return random.choice(intent['responses']) + todat_date
                    else:
                        return random.choice(intent['responses'])
        else:
            return "I do not understand ..."



#===============================

################# End Of The Model ################
userID=0
sessionID=0
conn = mysql.connector.connect(
    host="localhost",
    user="kwt1",
    password="kwt1",
    database="test"
)

cursor = conn.cursor()


@app.route('/')
def home():
    #return render_template('test.html')       
    return render_template('test.html')

@app.route('/user')
def user():
    if 'user_id' in session:
        return render_template('UserHome.html')
    else:
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute(""" INSERT INTO `users` (`name`, `email`, `password`, `gender`, `user_name`, `age`, `role`) VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}', '{}') """.format(name, email, password, gender, username, age, 1))

    conn.commit()

    cursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    user = cursor.fetchall()
    session['user_id'] = user[0][0]
    global userID
    userID = user[0][0]
    return redirect('/user')


@app.route('/login', methods=['POST'])
def login_validation():
    session.permanent = True
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
        .format(email, password))

    data = cursor.fetchall()
    print(data)
    if len(data) > 0:
        session['user_id'] = data[0][0]
        global userID
        userID = data[0][0]
        return redirect('/user')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


@app.route('/profile')
def profile():
    if 'user_id' in session:
        print("In The Profilllllllllllle")
        cursor.execute(""" SELECT * FROM `users` WHERE `user_id`='{}'"""
            .format(userID))

        data = cursor.fetchall()
        userInfo = {
            'name' : data[0][1],
            'email' : data[0][2],
            'password' : data[0][3],
            'user_name' : data[0][5],
            'age' : data[0][6],
            'progress' : data[0][8]
        }

        return render_template('profile.html', user=userInfo)
    else:
        return redirect('/')

@app.route('/session', methods=['POST'])
def sessions():
    if request.form.get('type') == 'trial':
        print("The trial : {}".format(request.form.get('type')))
        return render_template('session.html')

    if 'user_id' in session:

        cursor.execute(""" SELECT COUNT(*) FROM `sessions` WHERE 1""")
        data = cursor.fetchall()
        print("The count : {}".format(data))
        global sessionID
        sessionID = data[0][0] + 1

        print("the session ID : {}".format(sessionID))
        x = datetime.now()
        date = str(x.day) + "/" + str(x.month) + "/" + str(x.year) + ", " + str(x.hour) + ":" + str(
            x.minute) + ":" + str(x.second)
        print("The date : {}".format(date))

        cursor.execute(""" INSERT INTO `sessions` (`date`, `user_id`, `result`) VALUES
        ('{0}', '{1}', '{2}') """.format(date, userID, "Not Defined"))

        conn.commit()

        return render_template('session.html')
    else:
        return redirect('/')
startq=0

@app.route('/sendMessage', methods=['POST', 'GET'])
def sendMessage():
    if request.method == 'POST':
        print("The message : {}".format(request.form['message']))

        x = datetime.now()
        date = str(x.day) + "/" + str(x.month) + "/" + str(x.year) + ", " + str(x.hour) + ":" + str(
            x.minute) + ":" + str(x.second)
        reply = serverReply(request.form['message'])  # <========== response
        if(request.form['message'] is int):
            startq=1
        else:
            startq=0
        if(startq==0):
            temp =request.form['message']
            res =temp.find('\'')
            if(res!=-1):
                print(temp)
                temp =temp.replace('\'',' ')
                print(temp)

            cursor.execute(""" INSERT INTO `messages` (`date`, `text`, `session_id`, `sender`) VALUES
            ('{0}', '{1}', '{2}', '{3}') """.format(date, temp, sessionID, "user"))
            conn.commit()
            temp1 = reply
            res1 = temp1.find('\'')
            if (res1 != -1):
                print(temp1)
                temp1= temp1.replace('\'', ' ')
                print(temp1)

            cursor.execute(""" INSERT INTO `messages` (`date`, `text`, `session_id`, `sender`) VALUES
            ('{0}', '{1}', '{2}', '{3}') """.format(date, temp1, sessionID, "server"))
            conn.commit()
        print("User : {}".format(temp))
        print("Server: {}".format(reply))
        return reply
    return "The request should be POST"

@app.route('/loadMessages', methods=['POST', 'GET'])
def loadMessages():
    cursor.execute(""" SELECT `text`, `sender` FROM `messages` WHERE `session_id` IN
        (
            SELECT `session_id` FROM `sessions` WHERE `user_id` = '{}'
            ORDER BY `session_id` 
        );""".format(userID))
    data = cursor.fetchall()
    ret = str()
    for msg in data:
        ret += str(msg[0])
        ret += ">"
        ret += str(msg[1])
        ret += '|'

    print("The messages {}".format(ret))

    return ret

@app.route('/saveChanges', methods=['POST', 'GET'])
def saveChanges():
    if request.method == 'POST':
        name = request.form['name']
        userName = request.form['userName']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']

        cursor.execute(""" UPDATE `users` SET  `name`='{}', `email`='{}', `password`='{}', `user_name`='{}', `age`='{}' WHERE `user_id`='{}'"""
            .format(name, email, password, userName, age, userID))

        conn.commit()

        return redirect('/profile')
