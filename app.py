from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

RESEND_API_KEY = os.environ.get("RESEND_API_KEY")


@app.route('/')
def home():
    success = request.args.get('success')
    return render_template('index.html', success=success)


@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "from": "onboarding@resend.dev",
            "to": ["rajathshet.005@gmail.com"],
            "subject": f"Portfolio Message from {name}",
            "html": f"""
                <h3>New Portfolio Message</h3>

                <p><strong>Name:</strong> {name}</p>

                <p><strong>Email:</strong> {email}</p>

                <p><strong>Message:</strong></p>

                <p>{message}</p>
            """
        }
    )

    print(response.status_code)
    print(response.text)

    return redirect(url_for('home', success='1'))


if __name__ == '__main__':
    app.run(debug=True)