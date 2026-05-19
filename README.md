# Medical Insurance Cost Predictor

This Streamlit application predicts estimated medical insurance costs based on user inputs such as age, sex, BMI, number of children, smoking habits, and region.

## Features

- **Machine Learning Model**: Built using a Linear Regression model trained on a medical insurance dataset.
- **Interactive UI**: Simple and easy-to-use web interface powered by Streamlit.
- **Instant Predictions**: Get real-time cost estimates based on your profile.

## Setup Instructions

1. **Clone the repository** (if applicable) or download the files.
2. **Create and activate a Conda environment**:
   ```bash
   conda create -n tf python=3.12
   conda activate tf
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

## Files in the Repository

- `app.py`: The main Streamlit application script.
- `medical_insurance_model.pkl`: The pre-trained machine learning model.
- `requirements.txt`: List of required Python packages to run the app.
- `medical_insurance.ipynb`: The Jupyter Notebook used for exploratory data analysis and model training.
- `insurance.csv`: The dataset used to train the model.

## Usage

1. Open the application in your browser (typically `http://localhost:8501`).
2. Enter your **Age**, **Sex**, **BMI**, **Number of Children**, whether you are a **Smoker**, and your **Region**.
3. Click the **"Predict Insurance Cost"** button.
4. The estimated medical insurance cost will be displayed instantly on the screen.
