import streamlit as st

from modules.pdf_extractor import extract_text
from modules.preprocessing import clean_text
from modules.summarizer import summarize
from modules.qa_engine import answer_question
from modules.plagiarism_checker import check_plagiarism
from modules.ppt_generator import generate_ppt


st.title("Intelligent Research Paper Analysis and Assistance Chatbot")


uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type=["pdf"])


if uploaded_file is not None:

    # extract text from pdf
    text = extract_text(uploaded_file)

    # preprocess text
    sentences, clean_sentences = clean_text(text)

    st.success("Paper Loaded Successfully")


    # ---------- SUMMARY SECTION ----------

    if st.button("Generate Summary"):

        summary = summarize(sentences, clean_sentences)

        st.subheader("Summary")

        st.write(summary)

        # generate ppt
        ppt_file = generate_ppt(summary)

        # download ppt
        with open(ppt_file, "rb") as file:

            st.download_button(
                label="Download PPT",
                data=file,
                file_name="summary_presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )


    # ---------- QUESTION ANSWERING ----------

    st.subheader("Ask Questions from Paper")

    question = st.text_input("Enter your question")

    if question:

        answer = answer_question(question, text)

        st.write("Answer:", answer)


    # ---------- PLAGIARISM CHECK ----------

    st.subheader("Plagiarism Check")

    sample_dataset = [
        "machine learning improves automation",
        "natural language processing helps machines understand language",
        "deep learning models are powerful",
        "artificial intelligence is transforming industries"
    ]

    score = check_plagiarism(text, sample_dataset)

    st.write("Similarity Score:", score, "%")