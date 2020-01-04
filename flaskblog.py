from flask import Flask, render_template, url_for
app = Flask(__name__)


# Some dumb data
posts = [

    {
        'author': 'Corey Schafer',
        'title': 'Blog Post n 1',
        'content': 'April 20,2018'
    },
    {
        'author': 'Eduardo de Santana',
        'title': 'Blog Post n 2',
        'content': 'April 21,2017'
    },
    {
        'author': 'Julia Bandeira',
        'title': 'Blog Post n 5',
        'content': 'April 15,2017'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title="PASSING")
    
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
