from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beerjson = r.json()
    beer = {
        'name': beerjson[0]['name'],
        'desc': beerjson[0]['description'],
        'foodpair': beerjson[0]['food_pairing'],
        'brewerstips': beerjson[0]['brewers_tips']
    }

    return render_template('index.html', beer=beer)


if __name__ == '__main__':
    app.run(debug=True)
