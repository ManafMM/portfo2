from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html') 

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        fullname = data["fullname"]
        phone = data["phone"]
        email = data["email"]
        subject = data["subject"]
        message = data["text"]
        file = database.write(f'\n{fullname}, {phone}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        fullname = data["fullname"]
        phone = data["phone"]
        email = data["email"]
        subject = data["subject"]
        Message = data["text"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname,phone,email,subject,Message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print (data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'

