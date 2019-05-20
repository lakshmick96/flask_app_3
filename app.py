from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/', methods = ['POST', 'GET'])
def saved():
	if request.method == 'POST':
	    data = request.form['data']
	    d = sqlite3.connect('readings.db')
	    d.execute('CREATE TABLE IF NOT EXISTS Readings (Reading, date, time)')
	    d.execute('INSERT INTO Readings (Reading, date, time) values (?, date(), datetime())', [data] )
	    d.commit()
	    d.close()
	return render_template('home.html', data=data)

@app.route('/data', methods = ['POST', 'GET'])
def getreadings():
    return render_template('getdata.html')

@app.route('/display', methods = ['POST', 'GET'])
def display():
    if request.method == 'POST':
        to = request.form['to']
        frm = request.form['frm']
        d = sqlite3.connect('readings.db')
        cur = d.cursor()
        c = cur.execute('SELECT * FROM Readings')
        readings = c.fetchall()
        return render_template('display.html', to=to, frm=frm, readings=readings)



if __name__ == '__main__':
    app.run(debug = True)

