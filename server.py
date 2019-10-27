from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

from transliterate import transliterate_kn_iast


class TransliterationForm(FlaskForm):
    name = "test"
    text = TextAreaField("text")


app = Flask(__name__)
app.logger.setLevel('INFO')

@app.route("/", methods=("GET",))
def submit():
    form = TransliterationForm(csrf_enabled=False)
    original_text = request.args.get("text")
    app.logger.info(f"Now processing: {original_text}")
    if original_text:
        transliterated_text = transliterate_kn_iast(original_text)
        app.logger.info(f"Returning transliterated text: {transliterated_text}")
    else:
        transliterated_text = None
    return render_template("index.html", form=form, transliterated_text=transliterated_text, existing_text=original_text)
