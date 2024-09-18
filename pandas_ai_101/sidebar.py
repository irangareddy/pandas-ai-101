"""Feature Sidebar"""
import streamlit as st

def features_sidebar(pandasai_manager):
    st.sidebar.header("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        pandasai_manager.load_data(uploaded_file)
        st.sidebar.success("Dataset uploaded successfully!")
    elif pandasai_manager.df is not None:
        st.sidebar.info("Using previously loaded dataset")
    else:
        st.sidebar.warning("Please upload a CSV file")
        return None

    st.sidebar.header('PandasAI Features')
    feature = st.sidebar.selectbox(
        'Choose a PandasAI feature',
        ('Natural Language Querying', 'Data Visualization', 'Data Cleansing', 'Feature Generation with LLM')
    )

    return feature

