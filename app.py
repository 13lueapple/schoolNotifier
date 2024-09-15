from flask import Flask, render_template, request
import os, json, datetime


app = Flask(__name__)

def fileDir(relativeDir: str):
    return os.path.join(__file__, relativeDir)

@app.route("/")
def mainPage():
    return render_template("mainPage.html")

@app.route("/schedule", methods = ["GET", "POST"])
def schedulePage():
    if request.method == "POST":
        with open(fileDir("../data/password.json")) as f:
            _passwordData = json.load(f)
        if request.form["password"] != _passwordData["password"]:
            pass
        else:
            temp_data = {
                "monday" : {1:request.form['monday1'],
                            2:request.form['monday2'],
                            3:request.form['monday3'],
                            4:request.form['monday4'],
                            5:request.form['monday5'],
                            6:request.form['monday6'],
                            7:request.form['monday7']
                            },
                "tuesday" : {1:request.form['tuesday1'],
                            2:request.form['tuesday2'],
                            3:request.form['tuesday3'],
                            4:request.form['tuesday4'],
                            5:request.form['tuesday5'],
                            6:request.form['tuesday6'],
                            7:request.form['tuesday7']
                            },
                "wednesday" : {1:request.form['wednesday1'],
                            2:request.form['wednesday2'],
                            3:request.form['wednesday3'],
                            4:request.form['wednesday4'],
                            5:request.form['wednesday5'],
                            6:request.form['wednesday6'],
                            7:request.form['wednesday7']
                            },
                "thursday" : {1:request.form['thursday1'],
                            2:request.form['thursday2'],
                            3:request.form['thursday3'],
                            4:request.form['thursday4'],
                            5:request.form['thursday5'],
                            6:request.form['thursday6'],
                            7:request.form['thursday7']
                            },
                "friday" : {1:request.form['friday1'],
                            2:request.form['friday2'],
                            3:request.form['friday3'],
                            4:request.form['friday4'],
                            5:request.form['friday5'],
                            6:request.form['friday6'],
                            7:request.form['friday7']
                            }
            }
            with open(fileDir("../data/schedule.json"), 'w') as f:
                json.dump(temp_data, f, indent=4)
    with open(fileDir("../data/schedule.json")) as f:
            scheduleData = json.load(f)
        
    return render_template("schedule.html", schedule=scheduleData, today=datetime.datetime.now().strftime("%A").lower())

if __name__ == "__main__":
    app.run()