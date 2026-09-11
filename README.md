\# Intelligent Phishing Detection System using Machine Learning Techniques



\## 📌 Project Overview



The \*\*Intelligent Phishing Detection System\*\* is a Machine Learning based application developed to detect whether an email is \*\*Safe\*\* or \*\*Phishing\*\*.



The project uses Natural Language Processing (NLP) techniques to convert email text into numerical features using \*\*TF-IDF (Term Frequency-Inverse Document Frequency)\*\* and evaluates multiple Machine Learning algorithms.



The final system also includes a \*\*Streamlit web application\*\* where users can paste email content and receive a prediction.



\---



\## 🎯 Objectives



\- Detect phishing emails using Machine Learning.

\- Apply NLP techniques to email text.

\- Convert text into numerical features using TF-IDF.

\- Compare multiple Machine Learning algorithms.

\- Evaluate models using Accuracy, Precision, Recall, F1-score and ROC-AUC.

\- Develop a user-friendly Streamlit application.

\- Select a suitable final model for deployment.



\---



\## ✨ Key Features



\- 📧 Phishing and Safe email classification

\- 🧹 Text preprocessing

\- 🔤 TF-IDF feature extraction

\- ⚖️ Class balancing using undersampling

\- 🤖 Comparison of 7 Machine Learning algorithms

\- 🔍 GridSearchCV hyperparameter tuning

\- 📊 Multiple evaluation metrics

\- 📈 ROC curve comparison

\- 🔲 Confusion matrix visualization

\- 🔎 Feature importance analysis

\- 🧠 SHAP-based model explainability

\- 🌐 Interactive Streamlit application



\---



\## 📂 Dataset



The project uses the \*\*Phishing Email Dataset\*\* containing email text and corresponding labels.



\### Dataset Columns



| Column | Description |

|---|---|

| `Unnamed: 0` | Dataset index |

| `Email Text` | Email content |

| `Email Type` | Safe Email / Phishing Email |



\### Original Dataset Distribution



| Email Type | Count |

|---|---:|

| Safe Email | 11,322 |

| Phishing Email | 7,328 |

| Total | 18,650 |



The dataset contains a small number of missing values in the `Email Text` column, which are removed during preprocessing.



\---



\## ⚖️ Class Balancing



The original dataset contains more Safe Emails than Phishing Emails.



To create a balanced dataset for the ML experiment, \*\*undersampling\*\* was applied to the Safe Email class.



After balancing:



\- Safe Emails: 7,328

\- Phishing Emails: 7,328

\- Total: 14,656 emails



This balanced dataset was used for the comparative Machine Learning experiment.



\---



\# 🏗️ Project Architecture



```text

Email Dataset

&#x20;    │

&#x20;    ▼

Data Preprocessing

&#x20;    │

&#x20;    ├── Remove missing values

&#x20;    ├── Remove unnecessary column

&#x20;    └── Clean email text

&#x20;    │

&#x20;    ▼

Class Balancing

&#x20;    │

&#x20;    ▼

Train-Test Split

&#x20;    │

&#x20;    ▼

TF-IDF Vectorization

&#x20;    │

&#x20;    ▼

Machine Learning Models

&#x20;    │

&#x20;    ├── Logistic Regression

&#x20;    ├── SVM

&#x20;    ├── KNN

&#x20;    ├── Decision Tree

&#x20;    ├── Random Forest

&#x20;    ├── MLP

&#x20;    └── XGBoost

&#x20;    │

&#x20;    ▼

Model Evaluation

&#x20;    │

&#x20;    ├── Accuracy

&#x20;    ├── Precision

&#x20;    ├── Recall

&#x20;    ├── F1-score

&#x20;    └── ROC-AUC

&#x20;    │

&#x20;    ▼

Final Model Selection

&#x20;    │

&#x20;    ▼

Streamlit Application

&#x20;    │

&#x20;    ▼

Safe / Phishing Prediction

