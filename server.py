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

        sample = "Almost heaven, West Virginia\nBlue ridge mountains, Shenandoah river\nLife is old there, older than the trees\nYounger than the mountains, blowing like a breeze\nCountry roads, take me home".lower()
        if len(sample) > 100:
            sample = sample[:100]

        generated_lyrics = generate_lyrics(sample, genre)




    return render_template("index.html", **locals())



if __name__ == '__main__':
    app.run()
