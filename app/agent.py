from langchain.chains import RetrievalQA
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

from app.config import CHROMA_DB_PATH, PHI2_MODEL_PATH, LLAMA3B_MODEL_PATH

# Load the LLM model (using LlamaCpp for GGUF)
# Ensure you have either phi-2.gguf or llama-3b.gguf in the models/ directory
try:
    # Choose the model you want to use
    model_path = PHI2_MODEL_PATH # Or LLAMA3B_MODEL_PATH
    
    llm = LlamaCpp(
        model_path=model_path,
        n_ctx=2048, # Context window size
        n_gpu_layers=-1, # Offload all layers to GPU if available
        verbose=False, # Suppress verbose output
    )
except Exception as e:
    print(f"Error loading LLM model for RAG: {e}")
    llm = None

# Load the embeddings model
try:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception as e:
    print(f"Error loading embeddings model for RAG: {e}")
    embeddings = None

# Load the Chroma vector store
try:
    vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
    retriever = vectorstore.as_retriever()
except Exception as e:
    print(f"Error loading Chroma vector store: {e}")
    vectorstore = None
    retriever = None

# Create the RAG chain
qa_chain = None
if llm and retriever:
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

def get_rag_response(query: str) -> str:
    """
    Generates a response using the RAG system based on the knowledge base.
    """
    if qa_chain is None:
        return "RAG system not initialized. Cannot generate context-aware reply."
    try:
        result = qa_chain.invoke({"query": query})
        return result["result"]
    except Exception as e:
        return f"Error generating RAG response: {e}"

if __name__ == "__main__":
    # Simple test for RAG system
    if qa_chain:
        print("RAG system loaded successfully. Testing get_rag_response...")
        test_query = "What is the core technology used for STT?"
        response = get_rag_response(test_query)
        print(f"Query: {test_query}")
        print(f"Response: {response}")
    else:
        print("RAG system failed to load. Cannot run test.")
