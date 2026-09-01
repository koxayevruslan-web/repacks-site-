from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/gta5')
def gta5():
    return render_template('GTA5.html')

@app.route('/game/rdr2')
def rdr2():
    return render_template('RDR2.html')

@app.route('/game/f12020')
def f12020():
    return render_template('F12020.html')

@app.route('/game/tlou1')
def tlou1():
    return render_template('TLOU1.html')

@app.route('/discord')
def discord_page():
    return render_template('discord.html')
if __name__ == '__main__':
    app.run(debug=True)