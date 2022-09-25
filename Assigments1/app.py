from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/signin", methods=['POST', 'GET'])
def signin():
    return render_template('signin.html')




@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')
   # if request.method == 'POST':
    #    username = request.form['username']
     #   password = request.form['password']
      #  repassword = request.form['repassword']
       # if password == repassword:
        #    return render_template('signin.html')
        #else:
         #   return redirect(url_for('signup'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
