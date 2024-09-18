import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.helpers.openai_info import get_openai_callback


class PandasAIHandler:
    def __init__(self, api_key_manager):
        self.api_key_manager = api_key_manager
        self.df = None
        self.smart_df = None
        self.openai_llm = None

    def load_data(self, file):
        self.df = pd.read_csv(file)
        self._initialize_smart_df()
        return self.df

    def _initialize_smart_df(self):
        if self.df is not None and self.smart_df is None:
            pandasai_api_key = self.api_key_manager.get_api_key("PANDASAI_API_KEY")
            self.smart_df = SmartDataframe(
                self.df,
                config={
                    "api_key": pandasai_api_key,
                    "save_charts": True,
                    "conversational": False,
                    "enable_cache": True,
                    "use_error_correction_framework": True,
                }
            )

    def _get_openai_llm(self):
        if self.openai_llm is None:
            openai_api_key = self.api_key_manager.get_api_key("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set")
            self.openai_llm = OpenAI(api_token=openai_api_key)
        return self.openai_llm

    def natural_language_query(self, query):
        self._initialize_smart_df()
        return self.smart_df.chat(query)

    def visualize_data(self, query):
        self._initialize_smart_df()
        response = self.smart_df.chat(query)

        if "exports/charts" in response:
            chart_path = response.split("check out ")[-1].strip()
            return chart_path
        else:
            return response

    def cleanse_data(self, query=None):
        if self.df is None:
            raise ValueError("Dataframe is not initialized. Please load data first.")

        original_shape = self.df.shape
        original_columns = set(self.df.columns)
        original_dtypes = self.df.dtypes.to_dict()

        if query:
            response = self.smart_df.chat(query)

            if isinstance(response, pd.DataFrame):
                self.df = response
            else:
                return {"error": "Query did not return a DataFrame. Original data unchanged.",
                        "response": str(response)}
        else:
            self.df = self.df.dropna()

        # Calculate changes
        changes = {
            "rows_removed": original_shape[0] - self.df.shape[0],
            "columns_added": list(set(self.df.columns) - original_columns),
            "columns_removed": list(original_columns - set(self.df.columns)),
            "dtype_changes": {col: f"{original_dtypes[col]} -> {self.df[col].dtype}"
                              for col in self.df.columns
                              if col in original_dtypes and self.df[col].dtype != original_dtypes[col]}
        }

        return changes

    def generate_features(self, query):
        # Create a temporary SmartDataframe with OpenAI LLM for feature generation
        temp_smart_df = SmartDataframe(
            self.df,
            config={
                "api_key": self.api_key_manager.get_api_key("PANDASAI_API_KEY"),
                "llm": self._get_openai_llm(),
                "save_charts": True,
                "conversational": False,
                "enable_cache": True,
                "use_error_correction_framework": True,
            }
        )

        with get_openai_callback() as cb:
            response = temp_smart_df.chat(query)
            print(f"OpenAI API Usage for Feature Generation: {cb}")

        if isinstance(response, pd.DataFrame):
            self.df = response
            # Reset smart_df to None so it will be reinitialized with new data
            self.smart_df = None

        return response