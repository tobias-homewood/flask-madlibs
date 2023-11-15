from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)


# Define a route for the homepage
@app.route("/")
def homepage():
    prompts = story.prompts  # Get the prompts from the story
    return render_template("homepage.html", prompts=prompts)


# Define a route for generating and displaying the story
@app.route("/story", methods=["POST"])
def generate_story():
    answers = {}  # Initialize an empty dictionary to store user answers
    for prompt in story.prompts:
        answers[prompt] = request.form[prompt]  # Get user answers from the form

    generated_story = story.generate(answers)  # Generate the story
    return render_template("story.html", generated_story=generated_story)


if __name__ == "__main__":
    app.run(debug=True)
