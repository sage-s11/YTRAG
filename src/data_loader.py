from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported documents from the data directory and
    convert to LangChain document structure
    """
    # Use project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    #PDF files
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(pdf_file)
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    #Text files
    text_files = list(data_path.glob('**/*.txt'))
    print(f"Found {len(text_files)} Text files: {[str(f) for f in pdf_files]}")
    for text_file in text_files:
        print(f"[DEBUG] Loading text: {text_file}")
        try:
            textloader = TextLoader(text_file)
            textloaded = textloader.load()
            print(f"[DEBUG] Loaded {len(textloaded)} Text files from {text_file}")
            documents.extend(textloaded)
        except Exception as e:
            print(f"[ERROR] Failed to load text file: {text_file}")

    # CSV Files
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"Found {len(csv_files)} CSV files: {[str(csv_files) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV file: {csv_file}")
        try:
            csv_loader = CSVLoader(csv_file)
            loadedcsv = csv_loader.load()
            print(f"[DEBUG] Loaded {len(loadedcsv)} CSV files from {csv_file}")
            documents.extend(loadedcsv)
        except Exception as e:
            print(f"[ERROR] Failed to load CSV file: {csv_file}")

    return documents

