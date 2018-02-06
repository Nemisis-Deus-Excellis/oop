from flask import Flask, render_template, request ,flash, redirect, url_for, session
from wtforms import Form, StringField, PasswordField, TextAreaField, RadioField, SelectField, SubmitField, validators, DateField, FloatField
from wtforms.fields.html5 import DateField
import firebase_admin
from firebase_admin import credentials, db
from targets2 import Target
from bmi2 import Bmi
from User import *
from UserUp import *
from datetime import datetime
from RegisterProgram import Registerform
import pygal
from pygal.style import LightSolarizedStyle
from program import Program
from Contact import *


app = Flask(__name__)

cred = credentials.Certificate('cred/oopp-267d4-firebase-adminsdk-4rnbe-e23e0168e7.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

user_ref = db.reference('userbase')
now = datetime.now().date()

program = db.reference('program')
registerform = db.reference('registerform')

@app.route('/')
def home():
    return render_template('index.html')


class RegisterForm(Form):
    name = StringField('Please enter your full name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('What is your Gender?',[validators.DataRequired()], choices = [('', 'Select'), ('MALE', 'Male'), ('FEMALE', 'Female')],default='')
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    contact = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    weight = FloatField('Weight (KG)', [validators.DataRequired()])
    height = FloatField('Height (CM)', [validators.DataRequired()])
    program = SelectField('Which Program are you registering for?',[validators.DataRequired()], choices = [('', 'Select'), ('TAIJI', 'Complimentary Taiji & QiGong Classes'), ('MARINARUN', 'Marina Run 2018'), ('RUNFORLIGHT', 'Run For Light')],default='')


@app.route('/registerprogram', methods=['GET','POST'])
def registerform():
    userkey = session['key']
    root = user_ref.child(userkey)
    registerprog = RegisterForm(request.form)
    if request.method == 'POST' and registerprog.validate():
        name = registerprog.name.data
        gender = registerprog.gender.data
        email = registerprog.email.data
        contact = registerprog.contact.data
        weight = registerprog.weight.data
        height = registerprog.height.data
        program = registerprog.program.data

        registerform = Registerform(name, gender, email, contact, weight, height, program)
        registerform_db = root.child('registerprogram')

        registerform_db.push({
            'name': registerform.get_name(),
            'gender': registerform.get_gender(),
            'email': registerform.get_email(),
            'contact': registerform.get_contact(),
            'weight': registerform.get_weight(),
            'height': registerform.get_height(),
            'program': registerform.get_program()
            })

        flash('You have been registered for the program! Thank you!.', 'success')

    return render_template('registerform.html',registerform=registerprog)


@app.route('/fitnessprograms')
def fitnessprograms():
    #prog = Program('Program 1')
    #if request.method == 'GET':
        #registerform_db = root.child('registerform')
        #registerform_db.push({
            #'program': prog.get_program()
        #})
    return render_template('fitnessprograms.html')

class Plannerform(Form):
    age = SelectField('What is your age group?',[validators.DataRequired()], choices = [('', 'Select'), ('TEENAGER/ADULT', 'Teenager/Adult (Below 50)'), ('ELDERLY', 'Elderly (above 50)')],default='')
    type = SelectField('What type of exercise would you like to do?',[validators.DataRequired()], choices = [('', 'Select'), ('AEROBICS', 'Aerobics'), ('STRENGTH', 'Strength'), ('FLEXIBILITY', 'Flexibility')], default ='')
    time = SelectField('Choose the duration of exercise',[validators.DataRequired()], choices = [('', 'Select'), ('15min', '15 Min'), ('30min', '30 Min'), ('45min', '45 Min')], default='')


@app.route('/planner', methods=['GET','POST'])
def plannerform():
    plannerform = Plannerform(request.form)
    if request.method == 'POST' and plannerform.validate():
        age = plannerform.age.data
        type = plannerform.type.data
        time = plannerform.time.data

        routine  = ''

        if age == 'TEENAGER/ADULT':
            if type == 'AEROBICS':
                if time == '15min' :
                    routine = 'routine_1'
                elif time == '30min':
                    routine = 'routine_2'
                elif time == '45min':
                    routine = 'routine_3'

            elif type == 'STRENGTH':
                if time == '15min' :
                    routine = 'routine_4'
                elif time == '30min':
                    routine = 'routine_5'
                elif time == '45min':
                    routine = 'routine_6'

            elif type == 'FLEXIBILITY':
                if time == '15min' :
                    routine = 'routine_7'
                elif time == '30min':
                    routine = 'routine_8'
                elif time == '45min':
                    routine = 'routine_9'

        elif age == 'ELDERLY':
            if type == 'AEROBICS':
                if time == '15min':
                    routine = 'routine_10'
                elif time == '30min':
                    routine = 'routine_11'
                elif time == '45min':
                    routine = 'routine_12'

            elif type == 'STRENGTH':
                if time == '15min':
                    routine = 'routine_13'
                elif time == '30min':
                    routine = 'routine_14'
                elif time == '45min':
                    routine = 'routine_15'

            elif type == 'FLEXIBILITY':
                if time == '15min':
                    routine = 'routine_16'
                elif time == '30min':
                    routine = 'routine_17'
                elif time == '45min':
                    routine = 'routine_18'


        return redirect(url_for(routine))

    return render_template('plannerform.html',plannerform=plannerform)


@app.route('/routine_1')
def routine_1():
    return render_template('routine_1.html')

@app.route('/routine_2')
def routine_2():
    return render_template('routine_2.html')

@app.route('/routine_3')
def routine_3():
    return render_template('routine_3.html')

@app.route('/routine_4')
def routine_4():
    return render_template('routine_4.html')

@app.route('/routine_5')
def routine_5():
    return render_template('routine_5.html')

@app.route('/routine_6')
def routine_6():
    return render_template('routine_6.html')

@app.route('/routine_7')
def routine_7():
    return render_template('routine_7.html')

@app.route('/routine_8')
def routine_8():
    return render_template('routine_8.html')

@app.route('/routine_9')
def routine_9():
    return render_template('routine_9.html')

@app.route('/routine_10')
def routine_10():
    return render_template('routine_10.html')

@app.route('/routine_11')
def routine_11():
    return render_template('routine_11.html')

@app.route('/routine_12')
def routine_12():
    return render_template('routine_12.html')

@app.route('/routine_13')
def routine_13():
    return render_template('routine_13.html')

@app.route('/routine_14')
def routine_14():
    return render_template('routine_14.html')

@app.route('/routine_15')
def routine_15():
    return render_template('routine_15.html')

@app.route('/routine_16')
def routine_16():
    return render_template('routine_16.html')

@app.route('/routine_17')
def routine_17():
    return render_template('routine_17.html')

@app.route('/routine_18')
def routine_18():
    return render_template('routine_18.html')


@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

class bmiform(Form):
    weight = StringField('Weight(kg):', [validators.DataRequired()])
    height = StringField('Height(m):', [validators.DataRequired()])

@app.route('/bmi', methods=['GET','POST'])
def bmi1():
    userkey = session['key']
    root = user_ref.child(userkey)
    form = bmiform(request.form)
    if request.method =='POST' and form.validate():
        height = float(form.height.data)
        weight = float(form.weight.data)
        Bmi1 = Bmi(height, weight)
        bmi_data = root.child('BMI')
        bmi_data.push({
            "BMI":float(Bmi1.get_bmi()),
            "Date":str(now)
            })
        flash('You have successfully post your BMI','success')
        return redirect('/bmiresults')

    return render_template('bmi.html', form=form)
#@login_manager.unauthorized_handler
#def unauthorized_handler():
#    return render_template('<html>Please <a href="/login">Login</a>to access.</html>')

@app.route('/bmiresults')
def bmiresults():
    userkey = session['key']
    root = user_ref.child(userkey)
    bmirels = []
    bmidate = []
    ref3 = root.child('BMI').get()
    #bmirels = []  # create a list to store all the objects
    for ref5 in ref3:
        ref4 = ref3[ref5]
        refval = ref4['BMI']
        # retrieve date here
        refdate = ref4['Date']
        refval2 = float("{0:.2f}".format(refval))
        bmirels.append(refval2)
        bmidate.append(refdate)
    bmilast = bmirels[-1]
    if len(bmirels) > 5:
        bmirelt = bmirels[-5:]
        bmidate1 = bmidate[-5:]
        graph = pygal.Line(style=LightSolarizedStyle)
        graph.title = 'BMI history'
        graph.x_labels = bmidate1
        graph.add('BMI', bmirelt)
        graph_data = graph.render_data_uri()
        return render_template('bmiresults.html', bmilist2=bmirelt, bmilast=bmilast, graph_data=graph_data)
    else:
        graph = pygal.Line(style=LightSolarizedStyle)
        graph.title = 'BMI history'
        graph.x_labels = bmidate
        graph.add('BMI', bmirels)
        graph_data = graph.render_data_uri()
        return render_template('bmiresults.html' , bmilist2=bmirels, bmilast=bmilast, graph_data= graph_data)

root = db.reference()
#targets_ref = root.child('targets')

@app.route('/viewtarget')
def viewtarget():
    try:
        userkey = session['key']
        root = user_ref.child(userkey)
        #print(root.get())
        targets = root.child('targets').get()
        list1 = []  # create a list to store all the objects
        for target6 in targets:
            targetpost = targets[target6]
            target2 = Target(targetpost['goals'], targetpost['category'], targetpost['status'], targetpost['number'],
                             targetpost['date'])
            target2.set_target3(target6)
            target2.get_target3()
            list1.append(target2)
            #return render_template('view_target.html', targets=list1)
        return render_template('view_target.html', targets=list1)

    except TypeError:
        return render_template('error.html')

class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)


class Target1(Form):
    goals = StringField('Goals', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = RadioField('Type Of Goals', choices=[('physical', 'Physical'), ('diet', 'Diet'), ('habits', 'Habits')])
    status = RadioField('Status', choices=[('active', 'Active'),('onhold', 'On Hold'), ('notstarted', 'Not Started'), ('completed', 'Completed')])
    number = StringField('Number of times daily',[validators.Length(min=1, max=100), validators.DataRequired()])
    submit = SubmitField('Update')

@app.route('/newtarget', methods=['GET','POST'])
def new():
    userkey = session['key']
    root = user_ref.child(userkey)
    targetform = Target1(request.form)
    if request.method == 'POST' and targetform.validate():
        goals = targetform.goals.data
        category = targetform.category.data
        status = targetform.status.data
        number = targetform.number.data
        date = now
        tar = Target(goals, category, status, number, date)
        tar_db = root.child('targets')
        tar_db.push({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
            'date':str(now)
        })
        flash('Target added successfully.', 'success')
        return redirect(url_for('viewtarget'))

    return render_template('create_target.html', form=targetform)

@app.route('/update/<string:id>', methods=['GET','POST'])
def update_target(id):
    userkey = session['key']
    root = user_ref.child(userkey)
    targetform = Target1(request.form)
    if request.method == 'POST' and targetform.validate():
        goals = targetform.goals.data
        category = targetform.category.data
        status = targetform.status.data
        number = targetform.number.data
        date = now
        tar = Target(goals, category, status, number, date)
        tar_db = root.child('targets/' + id)
        tar_db.set({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
            'date': str(now)
        })
        flash('Goal Updated Successfully.', 'success')
        return redirect(url_for('viewtarget'))
    else:
        url = 'targets/' + id
        target_s = root.child(url).get()
        target2 = Target(target_s['goals'], target_s['category'], target_s['status'], target_s['number'], target_s['date'])
        target2.set_target3(id)
        targetform.goals.data = target2.get_goals()
        targetform.category.data = target2.get_category()
        targetform.status.data = target2.get_status()
        targetform.number.data = target2.get_number()

        return render_template('update_target.html', form=targetform)

    #return render_template('update_target.html', form=targetform)

@app.route('/delete_targets/<string:id>', methods=['POST'])
def delete_targets(id):
    userkey = session['key']
    root = user_ref.child(userkey)
    tar_db = root.child('targets/' + id)
    tar_db.delete()
    flash('Goal Deleted Successfully.', 'success')

    return redirect(url_for('viewtarget'))

__all__ = ['Target' , 'Bmi' ]

#profile
class UpdateForm(Form):
    name = StringField('Name', [validators.Length(min=1, max =50),validators.optional()])
    username = StringField('Username',[validators.Length(min=4,max=25),validators.optional()])
    email = StringField('Email', [validators.Length(min=6,max=50),validators.optional()])
    region = SelectField('Area of Residence', choices=[('Central', 'Central'), ('East', 'East'), ('North', 'North'), ('South', 'South')])
    password = PasswordField('Password', [validators.EqualTo('confirm',message='Passwords do not match'),validators.optional()])
    confirm = PasswordField('Confirm Password')

#@app.route('/<un>')
#def profile(un):
 #   return render_template('profile.html')




@app.route('/<un>/edit', methods=['GET','POST'])
def editprofile(un):
    userkey = session['key']
    root = user_ref.child(userkey)
    form = UpdateForm(request.form)
    userbase = user_ref.get()
    if request.method == 'POST' and form.validate():
            name = form.name.data.title()
            username = form.username.data
            email = form.email.data
            region = form.region.data
            password = str(form.password.data)
            user = UserUp(name,username,email,password,region)
            user_db = root.child('userbase/' + un)
            user_db.set = ({
                'name': user.get_name(),
                'username': user.get_username(),
                'email': user.get_email(),
                'password': user.get_password(),
                'region': user.get_region(),

            })
            flash('Profile Updated Sucessfully.', 'success')
            return render_template('editprofile.html', form=form)
    return render_template('editprofile.html',form=form)




#signup
class SignUpForm(Form):
    name = StringField('Name', [validators.Length(min=1, max =50), validators.DataRequired()])
    username = StringField('Username',[validators.Length(min=4,max=25),validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6,max=50),validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    gender = SelectField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    region = SelectField('Area of Residence',
                         choices=[('Central', 'Central'), ('East', 'East'), ('North', 'North'), ('South', 'South')])
    password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm',message='Passwords do not match')
])
    confirm = PasswordField('Confirm Password')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data.title()
        username = form.username.data
        email = form.email.data
        birthday = str(form.birthday.data)
        gender = form.gender.data
        region = form.region.data
        password = str(form.password.data)
        user_db = root.child('userbase')
        user = User(name, username, email, password,region,birthday,gender)
        user_db.push({
            'name': user.get_name(),
            'username': user.get_username(),
            'email': user.get_email(),
            'birthday': user.get_birthday(),
            'password': user.get_password(),
            'gender': user.get_gender(),
            'region': user.get_region()
        })
        flash('You have registered successfully', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

#login
class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
     form = LoginForm(request.form)
     if request.method == 'POST' and form.validate() == True:
         username = form.username.data
         password = form.password.data
         userbase = user_ref.get()
         for user in userbase.items():
             if user[1]['username'] == username and user[1]['password'] == password:
                 session['user_data'] = user[1]
                 session['logged_in'] = True
                 session['logged_out'] = True
                 session['un'] = username
                 session['key'] = user[0]
                 return redirect(url_for('home'))
             elif form.validate() == False:
                 flash('Please enter your credentials', 'danger')
                 return render_template('login.html', form=form)
     return render_template('login.html', form=form)
#

#logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

#contact
class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=1, max =50), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max =50), validators.DataRequired()])
    subject = StringField('Subject', [validators.Length(min=1, max =50), validators.DataRequired()])
    message = TextAreaField('Message',[validators.Length(min=20), validators.DataRequired()])

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate() == True:
        name = form.name.data.title()
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        contact_db = root.child('contact_message')
        contacts = Contact(name, email, subject,message)
        contact_db.push({
            'name': contacts.get_name(),
            'email': contacts.get_email(),
            'subject': contacts.get_subject(),
            'message': contacts.get_message()
        })
        flash('You have submitted a message successfully', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)




#requiredif
class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)



if __name__ == '__main__':
    app.secret_key = 'secret12'
    app.run()
