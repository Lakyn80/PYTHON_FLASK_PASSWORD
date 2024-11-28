from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'tajný klíč' # potřebné pro flash zprávy

# uživatelské údaje
USER_NAME = 'Lukas'
USER_PASSWORD = 'heslo'

# domovská stránka s formulářem
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # získání dat z formuláře
        user_name_input = request.form['username']
        user_password_input = request.form['password']

        # kontrola přihlašovacích údajů
        if user_name_input == USER_NAME and user_password_input == USER_PASSWORD:
            return 'Loged in!'
        else:
            flash('Zadal jsi špatné údaje, zkus to znovu!')
            return redirect(url_for('login'))
        
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)