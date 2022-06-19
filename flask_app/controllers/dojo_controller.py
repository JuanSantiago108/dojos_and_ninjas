
from flask_app import app
from flask import redirect ,render_template, request
from flask_app.models.dojo_model import Dojo 
from flask_app.models.ninja_model import Ninja

# ============================ FORM ROUTES =========================================




@app.route('/create/dojo', methods=['POST'])
def submit_dojo_form():
    data = {
        "name": request.form['name'],
    }

    Dojo.create_one_dojo(data)
    return redirect ('/all_dojos')


# ============================ FORM ROUTES =========================================
# ============================ DISPLAY ROUTES =======================================



@app.route('/')
@app.route('/all_dojos')
def display_all_dojos():

    all_dojos = Dojo.get_all_dojos()

    return render_template('all_dojos.html', all_dojos = all_dojos)


@app.route('/dojo_show/<int:id>')
def display_all_ninja_from_dojo_id(id):
    data = {
        'id' : id
    }
    
    one_dojo = Dojo.get_dojos_with_ninjas(data)
    print(one_dojo.ninjas) 
    return render_template('show_ninja.html',one_dojo=one_dojo)


# ============================ DISPLAY ROUTES =======================================



