#from flask import Flask, render_template
#import connexion

#app = Flask(__name__, template_folder='templates')
#app.add_api("swagger.yml")

# app.py

#from flask import Flask, render_template

#app = Flask(__name__, template_folder='template')

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    