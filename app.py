from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Gmail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'nnm23cs146@nmamit.in'
app.config['MAIL_PASSWORD'] = 'eins hsai zshe tgaq'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        subject=f'Portfolio Message from {name}',
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']]
    )

    msg.body = f'''
Name: {name}

Email: {email}

Message:
{message}
'''

    mail.send(msg)

    return '''
    <h2>Message Sent Successfully!</h2>
    <a href="/">Go Back</a>
    '''


if __name__ == '__main__':
    app.run(debug=True)