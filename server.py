from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:path>')
def page(path):
    return render_template(path)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'Email : {email}\n Subject : {subject}\n Message : {message}\n\n')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return 'done'
    else:
        return 'Problem'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')