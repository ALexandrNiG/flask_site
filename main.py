from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    main_data = {
        'a' : 'A - apple',
        'b' : 'B - banana',
        'c' : 'C - cocoa'
    }
    return render_template('index.html', main_data= main_data)

#
@app.route("/run/", methods = ['GET', 'POST'])
def create_new_contact():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method =='POST':
        input_name = request.form['input_name']
        input_status = request.form['input_status']
        input_phone = request.form['input_phone']
        with open('main_base.csv', 'a+') as f:
            f.write(f'{input_name};{input_status};{input_phone};\n')
        return render_template('form.html')



# @app.route("/run/", methods = ['GET', 'POST'])
# def run():
#     if request.method == 'POST':
#         pass
#     else:
#         return render_template('form.html')

# @app.route('/run/', methods=['GET'])
# def run_get():
#     with open('main_base.csv', 'r') as f:
#         text = f.read()
#     return render_template('form.html', text=text)


#
# @app.route('/run/', methods=['POST'])
# def run_post():
#     # Как получть данные формы
#     text = request.form['input_text']
#     with open('main_base.csv', 'a') as f:
#         f.write(f'{text}\n')
#     return render_template('good.html')

import csv
@app.route("/contacts/")
def contacts():
    context = {"Имя":[], "Статус":[], "Номер":[]}
    with open('main_base.csv', 'r') as csvfile:
        text = csv.reader(csvfile, delimiter=';')
        for row in text:
            context["Имя"].append(row[0])
            context["Статус"].append(row[1])
            context["Номер"].append(row[2])
    return render_template('contacts.html', context_names = context["Имя"], context_status = context["Статус"], context_phone = context["Номер"], num = len(context["Имя"]))

if __name__ == "__main__":
    with open('main_base.csv', 'w') as f:
        f.write('')
    app.run(debug=True, port=5001)