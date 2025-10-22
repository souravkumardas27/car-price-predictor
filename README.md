# 🚗 Car Price Predictor

A machine learning web application that predicts car prices based on various features like make, year, mileage, fuel type, and more. Built with Streamlit and powered by XGBoost regression.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Performance](#-model-performance)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Interactive Web Interface**: Clean and intuitive Streamlit-based UI
- **Real-time Predictions**: Get instant car price predictions
- **Comprehensive Input Fields**: 
  - Car make/brand selection
  - Year of manufacture (1990-2025)
  - Kilometers driven
  - Fuel type (Petrol, Diesel, CNG, Electric)
  - Transmission type (Manual, Automatic)
  - Engine capacity (CC)
  - Maximum power (bhp)
  - Seating capacity
- **Robust Error Handling**: Graceful handling of missing models and invalid inputs
- **Data Visualization**: Built-in charts and analysis tools
- **Model Persistence**: Pre-trained model ready for deployment


## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/souravkumardas27/car-price-predictor.git
cd car-price-predictor
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app/streamlit_app.py
```

The application will be available at `http://localhost:8501`

## 💻 Usage

1. **Launch the Application**: Run the Streamlit app using the command above
2. **Input Car Details**: Fill in the required fields:
   - Select or enter the car brand
   - Choose the year of manufacture
   - Enter kilometers driven
   - Select fuel type and transmission
   - Specify engine capacity and power
   - Set seating capacity
3. **Get Prediction**: Click the predict button to see the estimated car price
4. **View Results**: The predicted price will be displayed along with confidence metrics

## 📁 Project Structure

```
car-price-predictor/
├── app/
│   └── streamlit_app.py          # Main Streamlit application
├── data/
│   ├── raw/
│   │   └── car_data.csv          # Original dataset
│   └── processed/
│       └── car_data_clean.csv    # Cleaned and processed data
├── models/
│   └── car_price_model.pkl       # Trained XGBoost model
├── notebooks/
│   ├── 01_eda.ipynb              # Exploratory Data Analysis
│   └── 02_model_training.ipynb   # Model training and evaluation
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore file
├── LICENSE                       # MIT License
└── README.md                     # Project documentation
```

## 📊 Model Performance

The model uses XGBoost regression and has been trained on a comprehensive car dataset. Key performance metrics include:

- **R² Score**: Measures the proportion of variance explained by the model
- **RMSE**: Root Mean Square Error for prediction accuracy
- **Cross-validation**: Robust evaluation across different data splits

*Note: Specific performance metrics can be found in the model training notebook.*

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Machine Learning**: 
  - XGBoost
  - Scikit-learn
  - Pandas
  - NumPy
- **Data Visualization**: 
  - Matplotlib
  - Seaborn
- **Model Persistence**: Joblib
- **Development**: Jupyter Notebooks

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌐 Live Demo

🚀 **Try the app online**: [Streamlit App](https://your-app-name.streamlit.app) *(Coming Soon)*

## 📞 Contact

Sourav Kumar Das - [@souravkumardas27](https://github.com/souravkumardas27) 

Project Link: [https://github.com/souravkumardas27/car-price-predictor](https://github.com/souravkumardas27/car-price-predictor)

---

⭐ If you found this project helpful, please give it a star.
