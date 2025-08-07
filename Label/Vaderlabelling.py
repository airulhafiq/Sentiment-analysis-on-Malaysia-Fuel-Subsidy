import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')
# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to label sentiment
def label_sentiment(df, text_column='Content'):
    # Create a new column 'Sentiment' based on the comment of the text
    df['Sentiment'] = df[text_column].apply(lambda text: classify_sentiment(text))
    return df

# Helper function to classify sentiment
def classify_sentiment(text):
    scores = sid.polarity_scores(str(text))  # Convert text to string to avoid issues
    if scores['compound'] > 0.05:
        return 'Positive'
    elif scores['compound'] < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Directory with Excel files
data_folder = 'Labelling'
output_folder = 'Labelling\Labeled'
os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists

for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(data_folder, file_name)

        # Load the Excel file into a DataFrame
        df = pd.read_csv(file_path)

        # Apply sentiment labeling
        labeled_df = label_sentiment(df, text_column='Content')

        # Define output file path in 'Labeled' folder
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_Labeled.csv")

        # Save the labeled DataFrame to a new Excel file with sentiment column in column C
        labeled_df.to_csv(output_file_path, index=False)

        print(f"Labeled file saved as {output_file_path}")
