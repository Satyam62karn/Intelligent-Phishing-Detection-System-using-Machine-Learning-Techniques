# 🛡️ Intelligent Phishing Detection System Using Machine Learning

A machine learning-based web application that analyzes email text and classifies it as **Safe** or **Phishing** using TF-IDF feature extraction and Logistic Regression.

<p align="center">
  <a href="https://satyam-phishing-detector.streamlit.app/">
    <img src="https://img.shields.io/badge/Live_Demo-Launch_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/Satyam62karn/Intelligent-Phishing-Detection-System-using-Machine-Learning-Techniques">
    <img src="https://img.shields.io/badge/GitHub-View_Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
</p>

---

## 📌 Project Overview

Phishing emails are a common cybersecurity threat used to deceive users into revealing sensitive information, clicking suspicious links, or interacting with fraudulent messages.

The **Intelligent Phishing Detection System** applies Natural Language Processing (NLP) and machine learning techniques to classify email content into Safe Email or Phishing Email categories.

The application provides a simple, interactive interface where users can paste email text and receive a prediction from a trained Logistic Regression model.

## ✨ Key Features

- **Email Classification:** Predicts whether an email is likely to be safe or phishing.
- **TF-IDF Feature Extraction:** Converts text into numerical features for machine learning.
- **Logistic Regression:** Uses a supervised learning algorithm for classification.
- **Data Preprocessing:** Handles missing text and label values in the dataset.
- **Interactive Web Interface:** Built using Streamlit for easy access and testing.
- **Live Deployment:** Available online through Streamlit Community Cloud.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset loading and preprocessing |
| Scikit-learn | Machine learning and feature extraction |
| TF-IDF Vectorizer | Text feature representation |
| Logistic Regression | Email classification |
| Streamlit | Interactive web application |
| CSV | Dataset format |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

## ⚙️ Project Workflow

1. **Dataset Loading:** Load labeled email data from the CSV file.
2. **Data Preprocessing:** Select relevant columns and remove records with missing text or labels.
3. **Text Vectorization:** Transform email text into numerical features using TF-IDF.
4. **Model Training:** Train the Logistic Regression classifier using labeled examples.
5. **User Input:** Accept email content through the Streamlit interface.
6. **Prediction:** Transform the input using the fitted vectorizer and classify it.
7. **Result Display:** Show the predicted category in the application.

## 📂 Project Structure

```text
Intelligent-Phishing-Detection-System/
├── app.py
├── train_model_github.py
├── Phishing_Email.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Dataset

The project uses `Phishing_Email.csv`, a dataset containing email text and associated classification labels.

| Column | Description |
|---|---|
| `Email Text` | Email content used for classification |
| `Email Type` | Target label: Safe Email or Phishing Email |
| `Unnamed: 0` | Additional index column in the original dataset |

During preprocessing, the application selects the required text and label columns and removes rows with missing values.

## 🚀 Getting Started

Follow the instructions below to run the project locally.

### Prerequisites

- Python 3.12 or another compatible Python version
- Git
- Visual Studio Code or another Python editor

### 1. Clone the Repository

```bash
git clone https://github.com/Satyam62karn/Intelligent-Phishing-Detection-System-using-Machine-Learning-Techniques.git
```

### 2. Navigate to the Project Directory

```bash
cd Intelligent-Phishing-Detection-System-using-Machine-Learning-Techniques
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

To activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser. Paste an email into the text area and click **Check Email** to receive a prediction.

## 🧪 Example

**Sample email input:**

```text
Your account has been suspended.
Click here immediately to verify your password.
```

The model analyzes the email text and returns a predicted category.

*Note: The actual prediction depends on the trained model and may not always be correct.*

## 🔮 Future Improvements

- Evaluate model performance using accuracy, precision, recall, F1-score, and a confusion matrix.
- Introduce a separate test dataset for more reliable evaluation.
- Compare Logistic Regression with other classification algorithms.
- Explore additional text preprocessing and feature engineering techniques.
- Investigate suspicious URL and sender-related features.
- Improve model efficiency and deployment performance.

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes. Machine learning predictions are not guaranteed to be accurate. Do not rely solely on this application to determine whether an email is safe or malicious.

## 👨‍💻 Author

**Satyam Kumar Karn**

Aspiring Data Analyst | Machine Learning & Data Analytics

- **GitHub:** [Satyam62karn](https://github.com/Satyam62karn)
- **Project Repository:** [Intelligent Phishing Detection System](https://github.com/Satyam62karn/Intelligent-Phishing-Detection-System-using-Machine-Learning-Techniques)
- **Live Demo:** [Email Phishing Detector](https://satyam-phishing-detector.streamlit.app/)

---

<p align="center">
  <i>Built with Python, NLP, Machine Learning, and Streamlit.</i>
</p>
