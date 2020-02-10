from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    # Creating attributes for this class
    breed_input = StringField("What breed are you?")
    submit_input = SubmitField("Submit")
    
# Using GET and POST methods, it is possible to send and receive data for the form
@app.route ('/', methods=['GET','POST'])
def index():
    breed_ouput = False
    
    # Create instance of the form class above: InfoForm()
    form = InfoForm()
    
    if form.validate_on_submit():
        breed_ouput = form.breed_input.data
        form.breed_input.data = ''
    return render_template('00-home.html', form=form, breed_ouput=breed_ouput)
    
if __name__ == '__main__':
    app.run(debug=True)