from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(compound_score):
    if compound_score >= 0.05:
        return "Positive 😊"
    elif compound_score <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

@app.route('/', methods=["GET", "POST"])
def home():
    sentiment_result = None

    if request.method == "POST":
        user_text = request.form.get("text", "").strip()
        if user_text:
            scores = analyzer.polarity_scores(user_text)
            label = get_sentiment_label(scores['compound'])
            sentiment_result = {
                'positive': scores['pos'],
                'neutral': scores['neu'],
                'negative': scores['neg'],
                'compound': scores['compound'],
                'label': label,
                'text': user_text
            }
        else:
            sentiment_result = {'error': "Please enter some text to analyze."}

    return render_template('index.html', result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)
