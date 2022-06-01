from flask import Flask, render_template, redirect, flash,request
import os

##############################################################################

app = Flask("Satyammishra")

# setting up secret key
app.secret_key = os.urandom(12)



@app.route('/')
def home():
    return render_template("home.html")
