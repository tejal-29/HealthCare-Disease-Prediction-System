
# Healthcare — Multi-Disease Prediction System

Healthcare is a machine learning-based web application that demonstrates predictions for four health-related classification tasks: diabetes, heart disease, stroke, and thyroid conditions. Built with Python and Streamlit, the application provides a simple interface for entering health-related measurements and viewing the output of trained machine learning models.

## Features

- Diabetes prediction using a trained machine learning model.
- Heart disease prediction based on cardiovascular features.
- Stroke prediction using demographic and health-related inputs.
- Thyroid classification using laboratory measurements.
- Interactive dashboard with separate assessment pages.
- Form-based data entry and prediction results.
- Streamlit interface for running the application locally or deploying it online.

## Technologies Used

- **Programming Language:** Python
- **Frontend and Web Framework:** Streamlit
- **Data Handling:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model Storage:** Pickle
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git and GitHub

## Project Structure

```text
Multi-Disease-Detection-System/
├── app.py
├── requirements.txt
├── README.md
└── saved_models/
    ├── diabetes_model.sav
    ├── heart_disease_model.sav
    ├── stroke_model.sav
    └── thyroid_model.sav
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tejal-29/Multi-Disease-Detection-System.git
cd MediScope
```

Replace `tejal-29` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## How to Use

1. Open the application dashboard.
2. Select a prediction module from the sidebar.
3. Enter the requested input values.
4. Submit the form to run the corresponding trained model.
5. Review the prediction result.

## Machine Learning Models

The application loads four pre-trained classification models:

| Model | Purpose |
|---|---|
| Diabetes Model | Diabetes-related classification |
| Heart Disease Model | Heart disease-related classification |
| Stroke Model | Stroke-related classification |
| Thyroid Model | Thyroid-related classification |

The models are stored in the `saved_models/` directory and loaded by the Streamlit application.

## Deployment

Healthcare can be deployed using Streamlit Community Cloud.

1. Push the project to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the repository and branch.
5. Set `app.py` as the application entry point.
6. Deploy the application.

Ensure that `requirements.txt` contains the required dependencies and that the trained model files are accessible to the deployed application.

## Limitations

- Prediction quality depends on the training datasets, model performance, feature engineering, and input preprocessing.
- Input values and category encodings must match those expected by the trained models.
- Saved models may require compatible versions of Python and Scikit-learn.
- The application does not replace professional medical evaluation.

## Disclaimer

Healthcare is an educational machine learning project developed for learning and demonstration purposes. Its outputs are not medical diagnoses or validated clinical recommendations. Consult a qualified healthcare professional for medical advice.

## Future Improvements

- Add model performance metrics and evaluation reports.
- Improve input validation and preprocessing consistency.
- Add visual summaries of model predictions.
- Include dataset documentation and model training methodology.
- Improve automated testing and deployment workflows.

## Author

**Tejal Komb**

B.Tech in Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning
