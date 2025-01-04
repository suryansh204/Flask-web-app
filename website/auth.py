from flask import Blueprint, render_template, request, flash
# blueprint means it has a bunch of urls inside

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean = True)
    
    
@auth.route('/logout')
def logout():
    return render_template("logout.html")
    
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
     email = request.form.get('email')
     firstName = request.form.get('firstName')
     password1 = request.form.get('password1')
     password2 = request.form.get('password2')
    
     if len(email) <4:
        flash('Email must be greater than 3 characters', category='error')
        pass
     elif len(firstName) <2:
         flash('First name must be greater than 1 character', category='error')
         pass
     elif len(password1) != password2:
         flash('Your passwords dont match', category='error')
         pass
     elif len(password1) < 7:
         flash('Password must be at greater than 7 characters', category='error')
         
     else:
         flash('Account created', category='success')
        #add the user
    
    return render_template("sign_up.html")
    