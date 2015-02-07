import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
sql = "SELECT * FROM stuffToPlot WHERE keyword =?"

wordUser = 'data'

def readData():
