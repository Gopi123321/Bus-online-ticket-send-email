from flask import Flask, request, flash, render_template, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "gopi"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gopikannan3961@gmail.com'
app.config['MAIL_PASSWORD'] = 'whgvhdvdbfggwjmm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/", methods=["POST", "GET"])
def send_email():
    if request.method == "POST":
        name = request.form['name']
        from_location = request.form['from']
        to_location = request.form['to']
        date = request.form['date']
        email = request.form['email']

        message = f'''
        Happy  Day
        Passenger Name: {name}
        From: {from_location}
        To: {to_location}
        Date of Travel: {date}
        Email: {email}
        Thank you for your online booking
                '''

        msg = Message('Bus Ticket Booking', sender='gopikannan3961@gmail.com', recipients=[email])
        msg.body = message

        mail.send(msg)
        flash("Mail Sent Successfully", 'success')

        return redirect(url_for('send_email'))

    return render_template('bus.html')


if __name__ == '__main__':
    app.run(debug=True)
