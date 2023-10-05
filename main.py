from flask import Flask, render_template, url_for

app = Flask(__name__)

posts= [
    {
        'author': 'pp',
        'title': "the big pp",
        'content': 'first ggogogogogogogo',
        'date': '22/06/2007'
        
    },
    {
        'author': 'AJ',
        'title': "the small aj",
        'content': 'second boboboboboboboobobobobobobo',
        'date': '23/06/2007'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return(render_template('home.html',postas=posts))

@app.route('/about')
def about():
    return(render_template('about.html',title='about'))


app.run(debug=True)