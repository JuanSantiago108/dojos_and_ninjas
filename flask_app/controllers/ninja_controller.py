
from flask_app import app
from flask import redirect,render_template,request
from flask_app import DATABASE
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route("/ninjas/create")
def ninja_form():
    all_dojos = Dojo.get_all_dojos()
    return render_template("create_ninja.html", all_dojos =all_dojos )



@app.route('/ninjas/create', methods=['POST'])
def submit_ninja_form():
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    print("=====================================")
    Ninja.create_one_ninja(data)
    print(data)
    print("===================================")
    return redirect ('/all_dojos')