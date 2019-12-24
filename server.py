from flask import (
    Flask,
    render_template
)

#create the application instance
app = Flask(__name__, template_folder="templates")

#create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)