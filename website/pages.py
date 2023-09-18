from flask import Blueprint, render_template, redirect, url_for, request, flash #From the flask application, import Blueprint
from . import db
from .models import User
from flask_login import current_user
import sqlite3
from random import randint



pages = Blueprint("pages", __name__) #The blueprint name is now pages

#def get_db_connection():
    #swimJournal = sqlite3.connect('swimJournal.db')
    #swimJournal.row_factory = sqlite3.Row
    #return swimJournal
@pages.route("/conversionTool") 
def conversionTool():
    return render_template("conversionTool.html") #renders conversion tool template


@pages.route("/coachDashboard")
def coachDashboard():
    #swimJournal = get_db_connection()
    #coachID = current_user.get_id()
    #name = swimJournal.execute('SELECT CForename FROM coach WHERE id="coachID"').fetchall()
    #swimJournal.close()
    return render_template("coachDashboard.html") #, name = name
    #To pass in a variable from the backend to the frontend, do this:
    #return render_template("home.html", name = 1). If you then place this {{name}} into the specified html page, it will return
    #the value of that variable.
    #return render_template("coachDashboard.html")

@pages.route("/swimmerDashboard") 
def swimmerDashboard():
    #swimJournal = get_db_connection()
    #swimmerID = current_user.get_id()
    #name = swimJournal.execute('SELECT SForename FROM swimmer WHERE id=swimmerID').fetchall()
    #swimJournal.close()
    return render_template("swimmerDashboard.html", name = "me!") #, name = name
    #To pass in a variable from the backend to the frontend, do this:
    #return render_template("home.html", name = 1). If you then place this {{name}} into the specified html page, it will return
    #the value of that variable.


### Pages for the swimmers ###
@pages.route("/swimmerSession") 
def swimmerSession():
    return render_template("swimmerSession.html")

@pages.route("/swimmerJournal") 
def swimmerJournal():
    return render_template("swimmerJournal.html")

@pages.route("/swimmerAttendance") 
def swimmerAttendance():
    return render_template("swimmerAttendance.html")

@pages.route("/swimmerGoals") 
def swimmerGoals():
    return render_template("swimmerGoals.html")

@pages.route("/swimmerPBs") 
def swimmerPBs():
    return render_template("swimmerPBs.html")

### Pages for the Coaches ###

@pages.route("/coachSession") 
def coachSession():
    return render_template("coachSession.html")

@pages.route("/coachSwimmers", methods = {'GET', 'POST'}) 
def coachSwimmers():
    if request.method == 'POST':
        squadName = request.form.get('squadName')
        squadName_exists = Squads.query.filter_by(squadName=squadName).first()
        
        if squadName_exists:
            flash("Squad name already in use.", category="error")
        elif squadName < 2:
            flash("Squad name too short.", category="error")
        else:
            squadCode = randint(1000,9999)
            new_squad = Squads(squadName=squadName, squadCode=squadCode)
            db.session.add(new_squad)
            db.session.commit()
    return render_template("coachSwimmers.html")
            
            
@pages.route("/coachJournal") 
def coachJournal():
    return render_template("coachJournal.html")

@pages.route("/coachAttendance") 
def coachAttendance():
    return render_template("coachAttendance.html")