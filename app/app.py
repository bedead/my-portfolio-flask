from flask import Flask, render_template, redirect, flash,request
import os
from flask_mail import Mail, Message

##############################################################################

app = Flask("Satyammishra")

# setting up secret key
app.secret_key = os.urandom(12)

# mail data
mail = Mail(app)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'satyammishra.site@gmail.com'
app.config['MAIL_PASSWORD'] = 'HW8@Q-6Bt9lExon'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)




@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        desc = request.form.get('msg')

        print('name')

        if name and email and desc:
            msg = Message(
                subject=name,
                sender='satyammishra.site@gmail.com',
                recipients=['satyam.work.only@gmail.com'],
                body = f'{desc} \nfrom - {email}'
            )
            
            mail.send(msg)
            
            flash(f'Hey, {name} I have got your mail.', 'success')
            return redirect('/')
        else:
            flash("Make sure to fill out all the fields.", 'error')
            return render_template('home.html')
    return render_template("home.html")
