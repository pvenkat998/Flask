from flask import Flask,request

app=Flask(__name__)
@app.route('/')
def index():
    return "Method used : %s" % request.method

@app.route("/bacon",methods=['GET','POST'])
def bacon():
   if request.method=="POST":
      return"YOU ARE USING POST"
   else:
      return "YOU ARE probably USING GET"

if __name__=="__main__":
    app.run(debug=True)
