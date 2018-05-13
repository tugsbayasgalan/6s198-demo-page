import markovify
import re
import spacy

nlp = spacy.load("en")

class CustomText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

    def sentence_split(self, text):
        return re.split(r"\s*\n\s*", text)
# Get raw text as string.
with open("country_lyrics_all.txt") as f:
    text = f.read().decode('utf8')

# Build the model.
text_model = CustomText(text, state_size=6)


# Print three randomly-generated sentences of no more than 140 characters
for i in range(20):
    print(text_model.make_short_sentence(100))
