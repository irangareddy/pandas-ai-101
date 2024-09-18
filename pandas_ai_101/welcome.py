import streamlit as st


def display_data_overview(df):
    st.subheader("Data Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Column Information")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes,
        'Non-Null Count': df.notnull().sum(),
        'Null Count': df.isnull().sum()
    })
    st.dataframe(col_info, use_container_width=True)

    st.subheader("Sample Data")
    st.dataframe(df.head(), use_container_width=True)


def display_welcome_page():
    st.title("Welcome to PandasAI Explorer")
    st.write("Explore and analyze your data using the power of AI and natural language processing.")

    st.header("How to use this app:")
    st.markdown("""
    1. **Load your data**: Use the sidebar to upload a CSV file or select a sample dataset.
    2. **Choose a feature**: Select one of the following features from the sidebar:
        - Natural Language Querying
        - Data Visualization
        - Data Cleansing
        - Feature Generation with LLM
    3. **Explore your data**: Use the selected feature to analyze and manipulate your data.
    4. **Interpret results**: View the results of your queries and analyses in the main panel.
    """)

    st.header("Tips:")
    st.markdown("""
    - Start with Natural Language Querying to get a feel for your data.
    - Use Data Visualization to create insightful charts and graphs.
    - Clean your data using the Data Cleansing feature before in-depth analysis.
    - Generate new features using AI with the Feature Generation feature.
    """)
