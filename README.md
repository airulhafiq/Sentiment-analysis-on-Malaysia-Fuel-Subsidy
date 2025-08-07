Great! Based on your folder structure and the focus of your FYP project, here’s a complete, clean, and professional `README.md` you can upload to your GitHub repo:



---



```md

\# 🇲🇾 Sentiment Analysis on Malaysia Fuel Subsidy



This Final Year Project (FYP) analyzes public sentiment regarding the Malaysian government's fuel subsidy policy using social media comments. The project combines both traditional Machine Learning (ML) and Deep Learning (BERT) approaches to classify sentiments into \*\*positive\*\*, \*\*neutral\*\*, and \*\*negative\*\* categories.



---



\## 📁 Project Structure



```



Sentiment-analysis-on-Malaysia-Fuel-Subsidy/

│

├── API/                      # Temporary deployment using FastAPI

│   ├── api.ipynb             # Guide to run API locally

│   └── app.py                # FastAPI backend code

│

├── code/                     # Core code files

│   ├── dataPreprocess.py     # Full preprocessing pipeline

│   ├── translate.py          # Translate comments to English (if needed)

│   ├── model.ipynb           # Traditional ML model training (SVM, RF, etc.)

│   └── modelbert.ipynb       # Deep Learning model using BERT

│

├── dataset/

│   └── data.csv              # Labeled dataset used in this project

│

└── README.md                 # Project documentation



````



---



\## 🎯 Project Objective



To analyze and classify Malaysian public opinion towards fuel subsidy allocations using sentiment analysis techniques.



---



\## 🧠 Models Used



\### ✅ Traditional Machine Learning:

\- Support Vector Machine (SVM)

\- Naive Bayes

\- Random Forest



\### ✅ Deep Learning:

\- BERT (Bidirectional Encoder Representations from Transformers)



---



\## 🛠️ Preprocessing Workflow



1\. \*\*Text Cleaning\*\* – remove links, emojis, hashtags, etc.

2\. \*\*Translation\*\* – convert Malay comments to English (if necessary)

3\. \*\*Tokenization \& Vectorization\*\* – using `TF-IDF` for traditional ML and `Tokenizer` for BERT

4\. \*\*Sentiment Labeling\*\* – manually labeled into `positive`, `neutral`, `negative`



> All preprocessing is handled in `code/dataPreprocess.py`.



---



\## 📦 Dataset



\- 8,852 social media comments scraped from public platforms.

\- Each comment is labeled manually into one of three sentiment classes.



Dataset located at: `dataset/data.csv`



---



\## 🚀 How to Run



\### 🔹 Clone the Repository



```bash

git clone https://github.com/airulhafiq/Sentiment-analysis-on-Malaysia-Fuel-Subsidy.git

cd Sentiment-analysis-on-Malaysia-Fuel-Subsidy

````



\### 🔹 Create a Virtual Environment (optional but recommended)



```bash

python -m venv env

source env/bin/activate      # Linux/macOS

env\\Scripts\\activate         # Windows

```



\### 🔹 Install Required Packages



```bash

pip install -r requirements.txt

```



> You may need to manually install packages used in Jupyter notebooks.



---



\## 🌐 API Deployment (Local Test Only)



1\. Navigate to `API` folder.

2\. Run the API with FastAPI:



```bash

uvicorn app:app --reload

```



3\. Open browser at: `http://127.0.0.1:8000/docs` for interactive Swagger UI.



---



\## 📊 Dashboard \& Results



The final model results and sentiment analysis visualizations are built into the `model.ipynb` and `modelbert.ipynb`.



Includes:



\* Confusion Matrix

\* Classification Report

\* Accuracy Score

\* Word Cloud

\* Pie/Bar Charts



---



\## 📌 Acknowledgements



\* UiTM FYP Supervision (2025)

\* Hugging Face (Transformers)

\* scikit-learn, pandas, matplotlib, seaborn

\* Publicly available social media comments



---



\## 📬 Contact



\*\*Airul Hafiq\*\*

💼 \[LinkedIn](https://linkedin.com/in/airulhafiq)

📧 airulhafiq\\\[at]gmail.com



---



> \*This repository is part of a Final Year Project (FYP) at Universiti Teknologi MARA (UiTM), 2025.\*



```



---



Would you like this turned into an actual `.md` file to download directly and upload to GitHub?

```



