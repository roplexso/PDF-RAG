import streamlit as st

from utils.loader import extract_text
from utils.chunker import chunk_text
from utils.embeddings import embed_text
from utils.vectorstore import VectorStore
from utils.llm import ask_llm


st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Chat with Your PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

question = st.text_input(
    "Ask a question"
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("PDF Loaded Successfully!")

    chunks = chunk_text(text)

    st.write(f"Chunks Created: {len(chunks)}")

    embeddings = []

    with st.spinner("Generating embeddings..."):

        for chunk in chunks:
            embeddings.append(embed_text(chunk))

    st.success("Embeddings Generated!")

    dimension = len(embeddings[0])

    vector_store = VectorStore(dimension)

    vector_store.add(
        embeddings,
        chunks
    )

    st.success("Vector Database Ready!")

    if question:

        query_embedding = embed_text(question)

        relevant_chunks = vector_store.search(
            query_embedding,
            k=4
        )

        context = "\n\n".join(relevant_chunks)

        answer = ask_llm(
            context,
            question
        )

        st.subheader("Answer")

        st.write(answer)

        with st.expander("Retrieved Context"):

            for i, chunk in enumerate(relevant_chunks):

                st.markdown(f"### Chunk {i+1}")

                st.write(chunk)