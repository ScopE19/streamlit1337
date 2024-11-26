import streamlit as st
import pandas as pd

class Project1:
    def __int__(self):
        pass
    def app(self):
        st.title('Creation of DataFrame')
        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None
        upload = st.file_uploader('choose csv file')
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)
            column = st.selectbox('Choose column for filter', df.columns)
            if column:
                unique_values = df[column].unique()
                selected_values = st.multiselect(f"Select values for {column}", options=unique_values, default=unique_values)
                filtered_df = df[df[column].isin(selected_values)]
                st.dataframe(filtered_df, height=400, width=600)
            stress_levels = df['Stress_Level'].unique()
            selected_levels = st.multiselect('Select Stress Level(s)', options=stress_levels, default=stress_levels)
            filtered_df = df[df['Stress_Level'].isin(selected_levels)]
            st.dataframe(filtered_df, height=400, width=800)
        else:
            st.warning('Please upload a CSV file')
        st.title("Tekken EVO results 2005-2024 ")
        csv_path = "./src/Tekken EVO Results 2005-2024.csv"
        df = pd.read_csv(csv_path)
        st.write("Tekken EVO results 2005-2024 (preloaded DataFrame):")
        st.dataframe(df)
        column1 = st.selectbox('Choose column for filter', df.columns)
        if column1:
                unique_values = df[column1].unique()
                selected_values = st.multiselect(f"Select values for {column1}", options=unique_values, default=unique_values)
                filtered_df = df[df[column1].isin(selected_values)]
                st.dataframe(filtered_df, height=400, width=800)
      
        st.markdown("""<style>
                    h1 {
                    color: green;
                    font-size: 18px;
                    text-align: center;
                    }
                    </style>""", unsafe_allow_html=True)