from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
    
        user_text = request.form.get("text")
        analyze = TextBlob(user_text)
        polarity = analyze.sentiment.polarity
        
        print("Polarity score:", polarity)
        
    
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
