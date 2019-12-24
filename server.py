from flask import render_template
import connexion

#create the application instance
app = connexion.App(__name__, specification_dir="./")

#read swagger.ym,l file to configure the endpoits
app.add_api("swagger.yml")

#create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)