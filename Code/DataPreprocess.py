import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import os

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


# Function to clean a single DataFrame
def clean_excel_file(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Check if 'comment' column exists
    if 'Content' in df.columns:
        # Fill missing values in 'comment' column with an empty string
        df['Content'] = df['Content'].fillna('')

        # Ensure all data in 'comment' column are strings
        df['Content'] = df['Content'].astype(str)

        # Convert to lowercase
        df['Content'] = df['Content'].str.lower()

        # Remove special characters (keep only letters, numbers, and spaces)
        df['Content'] = df['Content'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

        # Remove emojis
        df['Content'] = df['Content'].apply(remove_emojis)

        # Remove stop words
        df['Content'] = df['Content'].apply(
            lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))

    else:
        print("No 'Content' column found in the DataFrame.")

    # # Remove rows with missing values
    # df = df.dropna()

    return df


# Function to remove emojis using regular expressions
def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


# Ensure the "Cleaned" directory exists
os.makedirs('tnbCleaned', exist_ok=True)

# Process all files in the "Data" directory
data_folder = 'tnb'
for file_name in os.listdir(data_folder):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(data_folder, file_name)

        try:
            # Load the Excel file into a DataFrame
            df = pd.read_excel(file_path)

            # Clean the DataFrame
            cleaned_df = clean_excel_file(df)

            # Create the output file name and path
            base_name = os.path.splitext(file_name)[0]
            cleaned_file_name = f"{base_name}_Cleaned.xlsx"
            output_file_path = os.path.join('tnbCleaned', cleaned_file_name)

            # Save the cleaned DataFrame to a new Excel file
            cleaned_df.to_excel(output_file_path, index=False)

            print(f"Cleaned file saved as {output_file_path}")
        
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
