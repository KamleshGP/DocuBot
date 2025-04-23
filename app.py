import os

from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


# load the environment variables
load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    def load_document(file_path):
        """This function load the pdf file and return the text from it."""
        loader = UnstructuredPDFLoader(file_path)
        documents = loader.load()
        return documents


    def setup_vectorstore(documents):
        """
        This function convert text into verctors and store into the vector database.
        Arguments:
                Documents: It takes text from the pdf.
        Returns : 
            Vectorstore
        """
        embeddings = HuggingFaceEmbeddings()
        text_splitter = CharacterTextSplitter(
            separator="/n",
            chunk_size=1000,
            chunk_overlap=200
        )
        doc_chunks = text_splitter.split_documents(documents)
        vectorstore = FAISS.from_documents(doc_chunks, embeddings)
        return vectorstore


    def create_chain(vectorstore,model_name):
        """
        This function creates chain to retrive the information from the documents and vectorstores.
        Arguments:
            vectorstore: text in the vector form.
            model_name: which llm model do you are using to give the response.
        Returns: 
            chain
        """
        llm = ChatGroq(
            model=model_name,
            temperature=0
        )
        retriever = vectorstore.as_retriever()
        memory = ConversationBufferMemory(
            llm=llm,
            output_key="answer",
            memory_key="chat_history",
            return_messages=True
        )
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            chain_type="map_reduce",
            memory=memory,
            verbose=True
        )
        return chain

    st.set_page_config(
        page_title="Chat with Doc",
        page_icon="📄",
        layout="centered"
    )

    st.title(" DocuBot 📄")

    model_name = st.selectbox("Select Your model: ", ["gemma2-9b-it", "llama-3.1-8b-instant"])


    # initialize the chat history in streamlit session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    #file upload option
    uploaded_file = st.file_uploader(label="Upload your pdf file", type=["pdf"])

    if uploaded_file:
        file_path = f"{working_dir}/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())


        if "vectorstore" not in st.session_state:
            st.session_state.vectorstore = setup_vectorstore(load_document(file_path))

        if "conversation_chain" not in st.session_state:
            st.session_state.conversation_chain = create_chain(st.session_state.vectorstore, model_name)

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #taking input from the user
    user_input = st.chat_input("Ask Your Question...")


    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)


        with st.chat_message("assistant"):
            response = st.session_state.conversation_chain({"question": user_input})
            assistant_response = response["answer"]
            st.markdown(assistant_response)
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    main()
