# DocuBot 📄 - Chat with Your Documents

This Streamlit application allows you to chat with the content of your PDF documents using the power of Large Language Models (LLMs) from Groq. You can upload a PDF file and ask questions related to its content, receiving insightful answers powered by retrieval-augmented generation.

## ✨ Features

* **Effortless PDF Upload:** Easily upload your PDF documents directly within the application.
* **Intelligent Chat:** Ask questions about the content of your uploaded PDF and receive relevant answers.
* **Powered by Groq:** Utilizes fast and efficient LLMs from Groq (gemma2-9b-it and llama-3.1-8b-instant).
* **Conversation History:** Maintains a chat history, allowing for follow-up questions and contextual understanding.
* **Model Selection:** Choose between different Groq models to experiment with their performance.

## 🚀 Deployed on Streamlit Cloud

You can try out the live application on Streamlit Cloud here:

👉 [Try DocuBot Now](https://your-streamlit-app-url.streamlit.app)


## ⚙️ Setup and Installation (for local development)

1.  **Clone the repository (if you have one):**
    ```bash
    git clone [your_repository_url]
    cd [your_repository_name]
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file with the following dependencies if it doesn't exist)*
    ```
    python-dotenv
    streamlit
    langchain-community
    langchain-text-splitters
    langchain
    huggingface-hub
    groq
    ```

3.  **Obtain a Groq API Key:**
    * Sign up for a Groq account at [https://console.groq.com/](https://console.groq.com/).
    * Generate an API key from your account settings.

4.  **Set up Environment Variables:**
    * Create a `.env` file in the root directory of your project.
    * Add your Groq API key to the `.env` file:
        ```
        GROQ_API_KEY="YOUR_GROQ_API_KEY"
        ```
        *(Replace `"YOUR_GROQ_API_KEY"` with your actual API key)*

5.  **Run the Streamlit application:**
    ```bash
    streamlit run your_script_name.py
    ```
    *(Replace `your_script_name.py` with the name of your Python script, e.g., `app.py`)*

6.  **Open your browser:** The application should automatically open in your web browser (usually at `http://localhost:8501`).

## 🛠️ How to Use

1.  **Upload a PDF File:** Click on the "Browse files" button under "Upload your pdf file" and select the PDF document you want to chat with.
2.  **Select a Model:** Choose your preferred Groq model from the "Select Your model" dropdown.
3.  **Start Chatting:** Once the PDF is uploaded, enter your questions in the chat input box at the bottom and press Enter or click the send button.
4.  **View Responses:** The assistant's responses based on the content of your PDF will appear in the chat window.
5.  **Continue the Conversation:** You can ask follow-up questions to delve deeper into the information within the document.
6.  **Upload a New File:** To chat with a different PDF, simply upload a new file. This will reset the chat history and the vector database.

## 💡 Under the Hood

This application leverages the following technologies:

* **Streamlit:** For creating the interactive web interface.
* **Langchain:** A framework for building applications powered by LLMs.
* **PyPDFLoader:** To load and extract text from PDF documents.
* **CharacterTextSplitter:** To break down the document text into smaller chunks.
* **HuggingFaceEmbeddings:** To generate vector embeddings for the text chunks.
* **FAISS:** For creating and storing the vector embeddings, enabling efficient similarity search.
* **Groq:** To access powerful and fast LLMs (gemma2-9b-it and llama-3.1-8b-instant) for generating responses.
* **ConversationBufferMemory:** To maintain the context of the conversation.
* **ConversationalRetrievalChain:** To combine document retrieval with conversational capabilities.
* **dotenv:** To securely manage environment variables (like the Groq API key).

## 🙏 Acknowledgements

* The Langchain and Streamlit communities for their excellent libraries and documentation.
* Groq for providing access to their high-performance LLMs.
* The creators of the Hugging Face Transformers library.
