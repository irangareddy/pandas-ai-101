import streamlit as st
import json
from api_key_manager import APIKeyManager
from welcome import display_welcome_page, display_data_overview
from pandas_ai_handler import PandasAIHandler
from sidebar import features_sidebar

st.set_page_config(layout="wide", page_title="PandasAI Explorer", page_icon='data/pokeball.png')


def load_queries():
    query_file_path = 'data/pokemon_queries.json'
    with open(query_file_path, 'r') as f:
        return json.load(f)


def app():
    """Streamlit app"""
    api_manager = APIKeyManager()
    api_manager.display_api_key_warning()
    api_manager.setup_api_key_inputs()

    pandasai_manager = PandasAIHandler(api_manager)

    feature = features_sidebar(pandasai_manager)

    if pandasai_manager.df is None:
        display_welcome_page()
    elif feature is None:
        st.title("Dataset Loaded")
        display_data_overview(pandasai_manager.df)
    else:
        queries = load_queries()
        st.write(pandasai_manager.df.head())

        if feature == 'Natural Language Querying':
            st.title("Natural Language Querying")
            query = st.selectbox("Select a query or enter your own:",
                                 [""] + queries["Natural Language Querying"] + ["Custom Query"])
            if query == "Custom Query":
                query = st.text_area("Enter your custom query:")
            if query:
                with st.spinner("Processing query..."):
                    result = pandasai_manager.natural_language_query(query)
                    st.success('Query Processed!')
                    st.write(result)

        elif feature == 'Data Visualization':
            st.title("Data Visualization")
            viz_query = st.selectbox("Select a visualization query or enter your own:",
                                     [""] + queries["Data Visualization"] + ["Custom Query"])
            if viz_query == "Custom Query":
                viz_query = st.text_area("Describe the visualization you want:")
            if viz_query:
                with st.spinner("Generating visualization..."):
                    chart_path = pandasai_manager.visualize_data(viz_query)
                    st.success('Visualization Generated!')
                    if isinstance(chart_path, str) and chart_path.endswith('.png'):
                        st.image(chart_path)
                    else:
                        st.write(chart_path)

        elif feature == 'Data Cleansing':
            st.title("Data Cleansing")
            cleanse_query = st.selectbox("Select a cleansing query or enter your own:",
                                         [""] + queries["Data Cleansing"] + ["Custom Query"])
            if cleanse_query == "Custom Query":
                cleanse_query = st.text_area("Enter cleansing instructions:")
            if st.button("Cleanse Data"):
                with st.spinner("Cleansing data..."):
                    changes = pandasai_manager.cleanse_data(cleanse_query)
                    if "error" in changes:
                        st.error(changes["error"])
                        st.write("Response:", changes["response"])
                    else:
                        st.success("Cleansing complete!")
                        st.write("Changes made:")
                        st.write(f"Rows removed: {changes['rows_removed']}")
                        if changes['columns_added']:
                            st.write(f"Columns added: {', '.join(changes['columns_added'])}")
                        if changes['columns_removed']:
                            st.write(f"Columns removed: {', '.join(changes['columns_removed'])}")
                        if changes['dtype_changes']:
                            st.write("Data type changes:")
                            for col, change in changes['dtype_changes'].items():
                                st.write(f"  {col}: {change}")
                        st.write("Updated first 5 rows:")
                        st.write(pandasai_manager.df.head())

        elif feature == 'Feature Generation with LLM':
            st.title("Feature Generation with LLM")
            instructions = st.selectbox("Select feature generation instructions or enter your own:",
                                        [""] + queries["Feature Generation with LLM"] + ["Custom Instructions"])
            if instructions == "Custom Instructions":
                instructions = st.text_area("Enter instructions for feature generation:")
            if st.button("Generate Features"):
                with st.spinner("Generating features..."):
                    updated_df = pandasai_manager.generate_features(instructions)
                    st.success("Features generated!")
                    st.write("First 5 rows of updated dataframe:")
                    st.write(updated_df.head())


if __name__ == "__main__":
    app()
