# BMI Prediction

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

> A BMI calculator and prediction tool with basic, advanced, and notebook-based implementations — including Asian/South Asian BMI thresholds.

## About

BMI Prediction is an internship project that calculates Body Mass Index from user inputs and classifies health categories. It includes three implementations: a basic CLI calculator with Asian-specific BMI thresholds, an advanced version with additional features, and a Jupyter notebook for data-driven BMI analysis using a dataset. Demonstrates health informatics concepts with culturally-aware BMI classification standards.

## Tech Stack

- **Language:** Python 3
- **Notebook:** Jupyter
- **Data:** Pandas (for notebook analysis)

## Features

- **Basic BMI calculator** — input weight (kg) and height (cm), get BMI and health category
- **Asian/South Asian thresholds** — uses WHO Asia-Pacific BMI cutoffs (overweight at 23, obese at 25)
- **Standard WHO classification** — 7-tier classification from severely underweight to obesity class III
- **Advanced version** — extended BMI analysis with additional health insights
- **Jupyter notebook** — data-driven BMI analysis using a CSV dataset
- **Input validation** — handles invalid inputs and edge cases
- **Dataset included** — `bmi.csv` for notebook-based exploration

## Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook (for `.ipynb` file)

### Installation

```bash
git clone https://github.com/iampreetdave/BMI-prediction.git
cd BMI-prediction
pip install pandas jupyter
```

### Run

**Basic calculator:**

```bash
python BMI-basic.py
```

**Advanced calculator:**

```bash
python BMI-adv.py
```

**Jupyter notebook:**

```bash
jupyter notebook BMI.ipynb
```

## How It Works

1. User inputs weight (kg) and height (cm)
2. BMI is calculated: `BMI = weight / (height_in_meters²)`
3. User is asked if they are Asian/South Asian
4. BMI is classified using the appropriate threshold scale:
   - **Asian:** Underweight (<18.5), Normal (18.5–23), Overweight (23–25), Obese (>25)
   - **Standard:** Severely Underweight (<16.5), Underweight (<18.5), Normal (<25), Overweight (<30), Obesity I/II/III
5. The Jupyter notebook performs batch analysis on `bmi.csv` with visualizations

## Project Structure

```
BMI-prediction/
├── BMI-basic.py    # Basic CLI calculator with Asian thresholds
├── BMI-adv.py      # Advanced BMI calculator
├── BMI.ipynb       # Jupyter notebook analysis
├── bmi.csv         # Dataset for notebook
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).
