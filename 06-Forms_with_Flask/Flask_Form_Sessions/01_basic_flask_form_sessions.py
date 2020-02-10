from flask import Flask, render_template, session, redirect_url, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField, RadioField, 
                    SelectField, TextField, TextAreaField, SubmitField)
# Validate the input
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    # List the validators to use
    breed = StringField("What breed are you?", validators=[DataRequired])
   
    neutered = BooleanField("Have you been neutered?")
   
    mood = RadioField("Please choose your mood:", 
                    choices=[('mood_one','Happy'),('mood_two','Excited')])
   
    food_choices = SelectField(u'Pick your favourite food:',
                    choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    
    feedback = TextAreaField()
    
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    
    form = InfoForm()
    
    if form.validate_on_submit():
        # Session data is stored temporarily on the webserver when the user is active
            # Removed once the user has left
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choices'] = form.food_choices.data
        session['feedback'] = form.feedback.data
    
    # If the inputs are validated then go to the thankyou html template  
    return redirect(url_for('01-thankyou'))

return render_template('01-home.html', form=form) 

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
        