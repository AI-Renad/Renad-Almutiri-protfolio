from flask import Flask,render_template

app = Flask(__name__)
project=[
  {'id':1,
  'project':'web scrapping',
  'skills':'urllib python,Python,Requests,Selenium'},
  {'id':2,
   'project':'AI model for flare mointoring',
  'skills':'python padas, skilitlib , matblotlib , microsoft azur,pychatgbt'}
]

@app.route("/")
def hello_world():
  return render_template("home.html",myskills=project,
                        myname='Renad')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=True)  #run flack server
