# ❤️ Heart Disease Detection

This is a machine learning-powered Django web application that predicts the likelihood of a person having heart disease based on various medical attributes. It provides a clean, interactive frontend and uses a trained model to generate predictions.

---

## 🧠 Project Objective

To build an intelligent system that assists users (patients or doctors) in predicting heart disease risks using relevant clinical features. It leverages supervised learning and integrates seamlessly with a Django-based web interface.

---

## 🚀 Features

🔍 Input form for medical data:
- Age
- Gender
- Chest pain type
- Resting blood pressure
- Cholesterol
- Fasting blood sugar
- ECG results
- Max heart rate
- Exercise-induced angina
- ST depression
- Slope, etc.

🤖 Uses pre-trained ML model (`heart_disease_model.pkl`)

📈 Displays clear output: **Likely or Not Likely to Have Heart Disease**

🖥️ Simple, responsive user interface (HTML templates)

📊 Real-world heart disease dataset (`dataset.csv`)

---

## 🛠️ Tech Stack

| Layer     | Technology                |
|-----------|---------------------------|
| Frontend  | HTML5, CSS3               |
| Backend   | Python, Django            |
| ML Model  | Scikit-learn              |
| Data      | Pandas, NumPy             |
| Storage   | SQLite3, Pickle           |
| Tools     | Git, GitHub, VS Code      |

---

## 📂 Folder Structure

HeartDisease/
│
├── webapp/
│ ├── predictor/ # Django app
│ │ ├── templates/ # HTML templates
│ │ ├── static/ # Static files (if any)
│ │ ├── views.py # Logic and model integration
│ │ ├── models.py # (optional) DB models
│ │ └── ...
│ ├── webapp/ # Django project settings
│ │ └── settings.py
│ └── manage.py # Django CLI
│
├── dataset.csv # Heart disease dataset
├── heart_disease_model.pkl # Trained ML model
├── scaler.pkl # Preprocessing scaler
├── requirements.txt # Python dependencies
└── .gitignore # Files to ignore

yaml
Copy
Edit

---

## ⚙️ How to Run the Project Locally

**Clone the repository:**
```bash
git clone https://github.com/Nitu143-nks/HeartDiseaseDetection.git
cd HeartDiseaseDetection
Create and activate a virtual environment (Windows):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py migrate
Start the development server:

bash
Copy
Edit
python manage.py runserver
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:8000/
📦 Dataset Used
The dataset (dataset.csv) contains real patient medical data and heart disease labels. It was used to train a classification model using Scikit-learn.

📈 Machine Learning Model
Trained using Scikit-learn

Preprocessed with StandardScaler

Saved as heart_disease_model.pkl using pickle

Integrated in Django view for real-time predictions

🙌 Contributing
Contributions are welcome! Open an issue or submit a pull request with improvements or ideas.

✨ Author
Nitesh Kumar Sahoo
📧 Email: sahoonitesh78@gmail.com
🎓 MCA Student | Full Stack Developer | ML Enthusiast
🌐 GitHub Profile
