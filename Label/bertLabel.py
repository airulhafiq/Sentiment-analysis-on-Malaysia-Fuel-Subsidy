import os
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Check for CUDA availability and move model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Initialize the tokenizer and model, using a pre-trained sentiment analysis model
tokenizer = AutoTokenizer.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')
model.to(device)  # Move model to GPU if available
model.eval()  # Set the model to evaluation mode

# Function to predict sentiment using the fine-tuned model
def predict_sentiment(Content):
    inputs = tokenizer(Content, return_tensors="pt", padding=True, truncation=True, max_length=128)
    inputs = {key: value.to(device) for key, value in inputs.items()}  # Move inputs to GPU

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = F.softmax(logits, dim=-1)
        predicted_class = torch.argmax(probabilities, dim=-1).item()

    # Map the prediction to sentiment labels
    sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
    return sentiment_map[predicted_class]

# Folder paths
data_folder = 'DataPreprocessing\Labelling'  # Input folder with CSV files
output_folder = 'DataPreprocessing\Labelling\Labeled'  # Output folder for labeled CSV files
os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists

# Process each CSV file in the data folder
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(data_folder, file_name)

        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Apply the sentiment prediction to the 'comment' column
        df['sentiment'] = df['Content'].apply(predict_sentiment)

        # Define output file path in 'Labeled' folder
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_Labeled.csv")

        # Save the labeled DataFrame to a new CSV file
        df.to_csv(output_file_path, index=False)

        print(f"Labeled file saved as {output_file_path}")

print("Sentiment analysis completed!")
