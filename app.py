#coding: utf-8
from flask import Flask
from flask import render_template

app = Flask(__name__)

RESTAURANTS = [
	{
		'name': u'Ślepy Zaułek',
		'menu': u'Lunch od 12 do 15. 20 zł za zestaw'
	}
]

@app.route('/')
def index():
	return render_template('index.html', restaurants=RESTAURANTS)


if __name__ == '__main__':
	app.run(debug=True)