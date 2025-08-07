from fastapi import FastAPI, HTTPException , Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Initialize FastAPI app
app = FastAPI()

# Load the model and tokenizer
model_path = "C:/Users/airul hafiq/Desktop/DataPreprocessing/DataPreprocessing/Model/bert_sentiment_model_adam44"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

# Define the input structure
class SentimentRequest(BaseModel):
    comment: str

# Define the sentiment mapping
sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the sentiment analysis API!"}

@app.post("/predict")
def predict_sentiment(request: SentimentRequest):
    # Preprocess the input text
    inputs = tokenizer(request.comment, return_tensors="pt", truncation=True, padding=True, max_length=128)
    
    # Perform inference
    try:
        outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        sentiment = torch.argmax(probabilities).item()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

    sentiment_result = {"comment": request.comment, "sentiment": sentiment_map[sentiment]}
    print(f"API Response: {sentiment_result}")  # Debug log
    return sentiment_result

@app.get("/", response_class=HTMLResponse)
async def root():
    """ public model testing """
    return """
    <html>
        <head>
            <title>Sentiment Analysis Testing</title>
            <script>
                async function analyzeSentiment(event) {
                    event.preventDefault();  // Prevent form submission

                    let comment = document.getElementById("comment").value;
                    let response = await fetch("/predict_test", {
                        method: "POST",
                        headers: {"Content-Type": "application/x-www-form-urlencoded"},
                        body: "comment=" + encodeURIComponent(comment)
                    });

                    let result = await response.json();
                    document.getElementById("result").innerHTML = 
                        "<h3>Sentiment: " + result.sentiment + "</h3>";
                }
            </script>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Test My Sentiment Analysis Model Bert </h2>
            <p>Enter a comment to analyze its sentiment(English Only):</p>
            <form onsubmit="analyzeSentiment(event)">
                <input type="text" id="comment" name="comment" 
                       placeholder="Enter a comment..." required 
                       style="padding: 8px; width: 300px;">
                <button type="submit" style="padding: 8px 15px; cursor: pointer;">Analyze</button>
            </form>
            <div id="result" style="margin-top: 20px; font-size: 20px; font-weight: bold;"></div>
        </body>
    </html>
    """

@app.post("/predict_test")  # Separate endpoint for public testing (Ngrok)
def predict_sentiment_test(comment: str = Form(...)):
    """ Model inference for public testing via Ngrok """
    try:
        # Tokenize input
        inputs = tokenizer(comment, return_tensors="pt", truncation=True, padding=True, max_length=128)
        # Perform inference
        outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        sentiment = torch.argmax(probabilities).item()
        return {"comment": comment, "sentiment": sentiment_map[sentiment]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")