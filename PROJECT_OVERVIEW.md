# PandasAI Explorer

## Introduction

PandasAI Explorer is a Streamlit-based web application that leverages the power of PandasAI and OpenAI to provide an intuitive, AI-driven data analysis experience. This tool allows users to explore, visualize, and analyze data using natural language queries, making data science more accessible to both technical and non-technical users.

## Key Components

1. **app.py**: The main Streamlit application file that orchestrates the user interface and functionality.

2. **sidebar.py**: Manages the sidebar functionality, including dataset upload and feature selection.

3. **welcome.py**: Displays the welcome page and data overview when a dataset is loaded.

4. **api_key_manager.py**: Handles API key management for PandasAI and OpenAI.

5. **pandas_ai_handler.py**: Core logic for interacting with PandasAI and processing data.

## Features

### 1. Natural Language Querying
Users can ask questions about their data in plain English. The application uses PandasAI to interpret these queries and return relevant results.

### 2. Data Visualization
Generate charts and graphs using natural language descriptions. The application leverages PandasAI's ability to create visualizations based on user prompts.

### 3. Data Cleansing
Perform automated or custom data cleaning operations. Users can provide instructions in natural language to clean and preprocess their data.

### 4. Feature Generation with LLM
Use AI to create new features based on existing data. This feature utilizes OpenAI's language models to generate new columns or transformations.

## How It Works

1. **Data Loading**: Users upload a CSV file through the sidebar.

2. **Feature Selection**: Users choose from four main features in the sidebar.

3. **Query Processing**: Depending on the selected feature, users can input queries or instructions in natural language.

4. **AI Processing**: The application uses PandasAI (and OpenAI for feature generation) to process the queries and manipulate the data.

5. **Result Display**: Results are displayed in the main panel, including text outputs, dataframes, and visualizations.

## Technical Details

- The project uses Poetry for dependency management.
- Streamlit is used for the web interface.
- PandasAI is the core library for AI-driven data analysis.
- OpenAI's API is used for advanced natural language processing in feature generation.
- The application supports dynamic API key configuration through environment variables or the UI.
- Task is used for task management.

# Conclusion

This project demonstrates the power of combining modern AI technologies with traditional data analysis tools, creating a user-friendly interface for data exploration and manipulation.
