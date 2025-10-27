import streamlit as st
st.write("Secret loaded:", "OPENAI_API_KEY" in st.secrets)
from openai import OpenAI

st.title("AI Job Description Analyzer 💼")

openai_api_key = st.text_input("Enter your OpenAI API key", type="password")
job_description = st.text_area("Paste the job description here:")

if st.button("Analyze"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        client = OpenAI(api_key=openai_api_key)
        with st.spinner("Analyzing job description..."):
            prompt = f"""
            You are an expert career advisor.
            Analyze the following job description and extract:
            1. Required skills (hard and soft)
            2. Experience level
            3. Industry keywords
            4. Key responsibilities
            5. Resume tailoring tips

            Job Description:
            {job_description}
            """
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response.choices[0].message.content)
