# PandasAI Explorer

## Overview

PandasAI Explorer is a Streamlit-based web application that leverages the power of PandasAI to provide intuitive, AI-driven data analysis. This tool allows users to explore, visualize, and analyze data using natural language queries, making data science more accessible to both technical and non-technical users.

## Features

- **Natural Language Querying**: Ask questions about your data in plain English.
- **Data Visualization**: Generate charts and graphs using natural language descriptions.
- **Data Cleansing**: Perform automated or custom data cleaning operations.
- **Feature Generation**: Use AI to create new features based on existing data.
- **User-friendly Interface**: Built with Streamlit for an intuitive user experience.

## Project Structure

For a detailed explanation of the project structure, components, and how they work together, please refer to the [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) file. This document provides in-depth information about:

- Key components of the application
- How each feature is implemented
- The data flow within the application
- Technical details and dependencies

I recommend reading the PROJECT_OVERVIEW.md file to get a comprehensive understanding of the project before diving into the code.

## Setup

To set up the PandasAI Explorer project, follow these steps:

1. **Prerequisites**:
   - Ensure you have Python 3.11 or later installed on your system.
   - Install [Poetry](https://python-poetry.org/docs/#installation) for dependency management.
   - Install [Task](https://taskfile.dev/installation/) for task management.

2. **Clone the repository**:
   ```
   git clone https://github.com/your-username/pandas-ai-101.git
   cd pandas-ai-101
   ```

3. **Install dependencies**:
   Run the following command to install all required dependencies:
   ```
   poetry install
   ```

4. **Run the application**:
   To start the Streamlit application, use the following command:
   ```
   task run
   ```
   Or, for development mode with auto-reload:
   ```
   task dev
   ```

5. **Additional commands**:
   - To run linter: `task lint`
   - To format code: `task format`
   - To run tests: `task test`
   - To update dependencies: `task update-deps`
   - To spawn a shell within the virtual environment: `task shell`

For a full list of available commands, run:
```
task list
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.