from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template("test.html")

@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    return render_template("home.html")

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    return render_template("info.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)