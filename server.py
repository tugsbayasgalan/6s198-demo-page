from flask import Flask, render_template, request
from utils import generate_lyrics
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():

    submitted = "false"

    if request.method == "POST":
        form = request.form

        seedtext = form['seedtext']
        genre = form['selectedOption']
        submitted = "true"

        generated_lyrics = generate_lyrics(seedtext, genre)




    return render_template("index.html", **locals())



if __name__ == '__main__':
    app.run()
