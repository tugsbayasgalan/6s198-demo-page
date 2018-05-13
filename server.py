from flask import Flask, render_template, request
from utils import generate_lyrics
import random
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():



    submitted = "false"
    if request.method == "POST":
        form = request.form
        seedtext = form['seedtext']
        genre = form['selectedOption']
        submitted = "true"
        if seedtext == "":
            generated_lyrics = generate_lyrics(seedtext, genre, random=True)

        else:
            sample = "Almost heaven, West Virginia\nBlue ridge mountains, Shenandoah river\nLife is old there, older than me".lower()
            generated_lyrics = generate_lyrics(sample, genre)


    return render_template("index.html", **locals())



if __name__ == '__main__':
    app.run()
