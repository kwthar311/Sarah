from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
#import mysql.connector
import os

userID = 0
sessionID = 0

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(hours=2)



from app import views
