# 📁 Project Structure & Navigation Guide

## Overview
This document provides a comprehensive guide to the organization, architecture, and navigation of the Network Security Analytics Platform. It is designed for both hiring managers and developers to quickly understand the structure, purpose, and usage of each part of the project.

---

## High-Level Organization

```
cisco-data-science-journey/
├── config/                # Configuration files (settings, secrets, environment)
├── data/                  # Datasets (raw, processed)
│   ├── raw/               # Original datasets (e.g., KDD Cup 1999)
│   └── processed/         # Cleaned and feature-engineered data
├── deployment/            # Production and local deployment scripts/apps
│   └── dashboard/         # Streamlit app and dashboard components
├── docs/                  # Project documentation and technical reports
├── models/                # Trained ML models and encoders
│   └── trained/classifiers/ # Saved model artifacts (pkl, encoders)
├── notebooks/             # Jupyter notebooks for EDA, modeling, analysis
├── reports/               # Executive and technical reports, figures
├── src/                   # Source code (modular Python packages)
│   ├── data/              # Data ingestion, validation, and processing
│   ├── models/            # ML model training and evaluation
│   ├── visualization/     # Plotting and dashboard utilities
│   └── utils/             # Helper functions and utilities
├── tests/                 # Unit and integration tests
├── streamlit-cloud/       # (NEW) Streamlit Cloud deployment version
│   ├── app.py             # Cloud-ready Streamlit app (copy, not original)
│   ├── requirements.txt   # Minimal requirements for cloud
│   └── .streamlit/        # Streamlit config for cloud
├── README.md              # Project overview and navigation
├── PROJECT_STRUCTURE.md   # (This file)
├── requirements.txt       # Full project requirements
└── .gitignore             # Files/folders to exclude from version control
```

---

## Directory & File Explanations

### config/
- **Purpose:** Store configuration files, secrets, and environment variables.
- **Usage:** Centralize settings for reproducibility and security.

### data/
- **raw/**: Original datasets (e.g., KDD Cup 1999). **Do not modify.**
- **processed/**: Cleaned and feature-engineered data for modeling.

### deployment/
- **dashboard/**: Main Streamlit app for local/enterprise deployment.
- **assets/**, **components/**: App resources and modular UI components.

### docs/
- **Purpose:** Technical documentation, user guides, and architecture diagrams.

### models/
- **trained/classifiers/**: Saved ML models (Random Forest, encoders, scalers).
- **Purpose:** Store all model artifacts for reproducibility and deployment.

### notebooks/
- **Purpose:** Jupyter notebooks for exploratory data analysis (EDA), feature engineering, and model development.
- **archive/**, **experimental/**: Older or experimental notebooks.

### reports/
- **Purpose:** Executive and technical reports, business impact summaries, and visual figures.
- **dashboards/**: Screenshots and visualizations for presentations.

### src/
- **data/**: Data ingestion, validation, and ETL pipeline code.
- **models/**: ML model training, evaluation, and inference code.
- **visualization/**: Plotting utilities and dashboard helpers.
- **utils/**: General-purpose helper functions.
- **api/**: (If present) REST API endpoints for model serving.

### tests/
- **Purpose:** Unit and integration tests for all major modules.
- **Usage:** Run `pytest` to validate code integrity.

### streamlit-cloud/ (NEW)
- **Purpose:** Dedicated folder for Streamlit Cloud deployment.
- **app.py**: Copy of main Streamlit app, enhanced for cloud demo.
- **requirements.txt**: Minimal requirements for cloud.
- **.streamlit/config.toml**: Streamlit Cloud configuration.

### README.md
- **Purpose:** Project overview, setup instructions, and navigation links.

### PROJECT_STRUCTURE.md (This file)
- **Purpose:** Detailed guide to project organization and navigation.

### requirements.txt
- **Purpose:** Full list of Python dependencies for local/enterprise use.

### .gitignore
- **Purpose:** Exclude sensitive, large, or unnecessary files from version control.

---

## Usage Guide

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run deployment/dashboard/complete_app.py`
4. Explore notebooks in `notebooks/` for EDA and modeling
5. Review reports in `reports/` for business and technical insights

### Streamlit Cloud Demo
1. Navigate to `streamlit-cloud/`
2. Deploy `app.py` to Streamlit Cloud
3. Use `requirements.txt` and `.streamlit/config.toml` for cloud setup

### Model Artifacts
- All trained models and encoders are in `models/trained/classifiers/`
- Do not modify these files unless retraining

### Data
- All raw data is in `data/raw/`
- Processed data is in `data/processed/`
- **Never overwrite raw data**

### Testing
- Run `pytest` in the `tests/` directory to validate code

---

## Navigation Guide

- **For Hiring Managers:**
  - Start with `README.md` for executive summary and business impact
  - See `PROJECT_STRUCTURE.md` for technical organization
  - Explore `reports/` for business value and results
  - Try the live demo in `streamlit-cloud/`

- **For Developers:**
  - Review `src/` for modular codebase
  - Use `notebooks/` for EDA and model development
  - Check `deployment/` for app deployment scripts
  - Validate with `tests/`

---

## Contact
For questions, contact the project author via email or GitHub (see `README.md`). 