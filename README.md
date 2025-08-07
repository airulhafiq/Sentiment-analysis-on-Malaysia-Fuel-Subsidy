# 🇲🇾 Sentiment Analysis on Malaysia Fuel Subsidy

This Final Year Project (FYP) explores public sentiment regarding Malaysia's fuel subsidy allocation by analyzing social media comments. It leverages both traditional Machine Learning (ML) and Deep Learning (BERT) models to classify sentiments into **positive**, **neutral**, and **negative** categories.

## 📁 Project Structure

```
Sentiment-analysis-on-Malaysia-Fuel-Subsidy/
├── API/                      # Temporary deployment using FastAPI
│   ├── api.ipynb             # Guide to run API locally
│   └── app.py                # FastAPI backend code
├── code/                     # Core code files
│   ├── dataPreprocess.py     # Full preprocessing pipeline
│   ├── translate.py          # Translate comments to English (if needed)
│   ├── model.ipynb           # Traditional ML model training (SVM, RF, NB)
│   └── modelbert.ipynb       # Deep Learning model using BERT
├── dataset/
│   └── data.csv              # Labeled dataset used in this project
├── Label/
│   ├──bertLabel.py           # Labelling code for Bert
│   └──Vaderlabelling.py      # Labelling code for Vader
└── README.md                 # Project documentation
```

---

## 🎯 Objective

To analyze and classify Malaysian public opinion on fuel subsidy allocation using sentiment analysis techniques.

---

## 🧠 Models Implemented

### ✅ Traditional Machine Learning:
- Support Vector Machine (SVM)
- Naive Bayes
- Random Forest

### ✅ Deep Learning:
- BERT (Bidirectional Encoder Representations from Transformers)

---

## 🛠️ Preprocessing Workflow

1. **Text Cleaning** – Removing links, emojis, hashtags, etc.  
2. **Translation** – Converting Malay comments to English (if necessary)  
3. **Tokenization & Vectorization** – Using `TF-IDF` for ML models and `Tokenizer` for BERT  
4. **Sentiment Labeling** – VADER and manual checking into `positive`, `neutral`, or `negative`  

> All steps are included in `code/dataPreprocess.py`.

---

## 📦 Dataset

- 8,852 social media comments scraped from public platforms.
- Manually labeled with one of three sentiment classes.

Location: `dataset/data.csv`

---

## 🚀 How to Run

### 🔹 Clone the Repository

```bash
git clone https://github.com/airulhafiq/Sentiment-analysis-on-Malaysia-Fuel-Subsidy.git
cd Sentiment-analysis-on-Malaysia-Fuel-Subsidy
```

### 🔹 Create a Virtual Environment (Recommended)

```bash
python -m venv env
# For Linux/macOS
source env/bin/activate
# For Windows
env\Scripts\activate
```

### 🔹 Install Dependencies

> Some dependencies might require manual installation if used within notebooks.

---

## 🌐 API Deployment (Local Only)

1. Navigate to the `API` folder.  
2. Run FastAPI:

```bash
uvicorn app:app --reload
```

3. Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the Swagger UI.

---

## 📊 Model Results & Visualizations

Results are documented in:
- `model.ipynb` (Traditional ML)
- `modelbert.ipynb` (BERT DL Model)

Includes:
- Confusion Matrix
- Accuracy Scores
- Classification Reports
- Word Clouds
- Bar & Pie Charts

---

## 🙏 Acknowledgements

- Final Year Project (UiTM 2025)
- Hugging Face (Transformers)
- scikit-learn, pandas, matplotlib, seaborn
- Public sources for social media data

---

## 📬 Contact

**Airul Hafiq**  
[LinkedIn](https://linkedin.com/in/airulhafiq)  
📧 hafiqairul02[at]gmail.com

> *This repository is part of a Final Year Project (FYP) at Universiti Teknologi MARA (UiTM), 2025.*