import os
import sys
import time
from dotenv import load_dotenv

# Add the parent directory to the path since we work with notebooks
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper_functions import *

load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv('API_KEY')


class SimpleRAG:
    """
    A class to handle the Simple RAG process for document chunking and query retrieval.
    """

    def __init__(self, path, chunk_size=1000, chunk_overlap=200, n_retrieved=2):
        """
        Initializes the SimpleRAGRetriever by encoding the PDF document and creating the retriever.

        Args:
            path (str): Path to the PDF file to encode.
            chunk_size (int): Size of each text chunk (default: 1000).
            chunk_overlap (int): Overlap between consecutive chunks (default: 200).
            n_retrieved (int): Number of chunks to retrieve for each query (default: 2).
        """
        print("\n--- Initializing Simple RAG Retriever ---")

        # Encode the PDF document into a vector store using OpenAI embeddings
        start_time = time.time()
        self.vector_store = encode_pdf(path, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.time_records = {'Chunking': time.time() - start_time}
        print(f"Chunking Time: {self.time_records['Chunking']:.2f} seconds")

        # Create a retriever from the vector store
        self.chunks_query_retriever = self.vector_store.as_retriever(search_kwargs={"k": n_retrieved})

    def run(self, query):
        """
        Retrieves and displays the context for the given query.

        Args:
            query (str): The query to retrieve context for.

        Returns:
            tuple: The retrieval time.
        """
        # Measure time for retrieval
        start_time = time.time()
        context = retrieve_context_per_question(query, self.chunks_query_retriever)
        self.time_records['Retrieval'] = time.time() - start_time
        print(f"Retrieval Time: {self.time_records['Retrieval']:.2f} seconds")

        # Display the retrieved context
        return context


# Function to validate command line inputs
def validate_args(args: dict) -> dict:
    if args.get('chunk_size') <= 0:
        raise ValueError("chunk_size must be a positive integer.")
    if args.get('chunk_overlap') < 0:
        raise ValueError("chunk_overlap must be a non-negative integer.")
    if args.get('n_retrieved') <= 0:
        raise ValueError("n_retrieved must be a positive integer.")
    return args


# Function to parse command line arguments
def get_args():
    args = {}
    # Path to the PDF file to encode.
    args['path'] = os.getenv("DOCUMENTS_PATH", "data/Understanding_Climate_Change.pdf")
    # Size of each text chunk (default: 1000).
    args['chunk_size'] = int(os.getenv("CHUNK_SIZE", 1000))
    # Overlap between consecutive chunks (default: 200).
    args['chunk_overlap'] = int(os.getenv("CHUNK_OVERLAP", 200))
    # Number of chunks to retrieve for each query (default: 2).
    args['n_retrieved'] = int(os.getenv("N_RETRIEVED", 2))

    # Parse and validate arguments
    return validate_args(args)


# Main function to handle argument parsing and call the SimpleRAGRetriever class
def retrieve_context(query: str) -> str:
    args = get_args()

    simple_rag = SimpleRAG(
        path=args['path'],
        chunk_size=args['chunk_size'],
        chunk_overlap=args['chunk_overlap'],
        n_retrieved=args['n_retrieved']
    )

    # Retrieve context based on the query
    retrieved_chunks = simple_rag.run(query)

    context = "\n\n".join([f"Doc {i+1}:\n{chunk}" for i, chunk in enumerate(retrieved_chunks)])

    return context

