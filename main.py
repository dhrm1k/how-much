import flask
#from flask import Flask, request, url_for, redirect, render_template
from replit import db, web
import datetime

today = datetime.datetime.now()
stryear = int(today.strftime('%j')) 

# -- Create & configure Flask application.
app = flask.Flask(__name__)
app.static_url_path = "/static"

users = web.UserStore()

lightbar = '░' 
darkbar = '▓'


@app.route("/")
def index():
  varstring = int(today.strftime('%j')) #Converting today.strftime in integer 

  stryear = varstring/365*100

  format_stryear = "{:.2f}".format(stryear)

  onlynumberdate = "{:.0f}".format(stryear)
  onlynumberdateint = int(onlynumberdate)

  ten = (10)
  forbar = onlynumberdateint/ten

  forbarwodec = "{:.0f}".format(forbar)
  forbarwodecint = int(forbarwodec)

  graphd = darkbar * forbarwodecint
  graphw = lightbar * (10 - forbarwodecint)


  return flask.render_template("index.html", format_stryear =format_stryear, graphd = graphd, graphw = graphw )

web.run(app)