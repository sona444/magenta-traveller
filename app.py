from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from openpyxl import load_workbook
from dotenv import load_dotenv
 
load_dotenv()

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
