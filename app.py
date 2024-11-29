import streamlit as st
import google.generativeai as genai

genai.configure(api_key="")

sys_prompt = """ You are a helpful AI Python Code Reviewer. 
When students provide Python code, you will:
1. Provide a detailed **Code Review** of the code.
2. Highlight any issues or errors in a section labeled **Bug Report**.
3. Provide a corrected version of the code in a section labeled **Fixed Code**.

Always format your response exactly like this:
- Code Review:(make it bold as title)
  [Your review here]

- Bug Report:(make it bold as title)
  [List of bugs here]

- Fixed Code:(make it bold as title)
  [Corrected Python code here]

If there are no bugs, clearly state that in the Bug Report section and still provide a reviewed version of the code in Fixed Code.

Do not respond to anything unrelated to Python code. """

llm = genai.GenerativeModel("models/gemini-1.5-flash",
                            system_instruction= sys_prompt)

st.title('GenAI App - AI Code Reviewer')

human_prompt = st.text_area("Enter your Python code here ...")

if st.button("Generate"):
    if human_prompt:
        response = llm.generate_content(human_prompt)
        response_text = response.text

        st.subheader("Code Review")
        st.write(response_text)

    else:
        st.warning("Please enter Python code before clicking Generate.")