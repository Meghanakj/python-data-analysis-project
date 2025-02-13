import zipfile
from elasticsearch import Elasticsearch
import pdfplumber
from datetime import datetime

# Elasticsearch connection details
ELASTIC_URL = "https://f350d84aeb164cfd90be94f49ee12835.us-central1.gcp.cloud.es.io:443"
USERNAME = "hemanth"
PASSWORD = "Submarine87!"

# Connect to Elasticsearch
es = Elasticsearch(w
    [ELASTIC_URL],
    basic_auth=(USERNAME, PASSWORD)
)

# Path to the zip file
zip_file_path = "ziped pdf_files.zip"

# Elasticsearch index name
index_name = "zipped_pdf"

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract and iterate through all PDF files in the zip archive
    for file_name in zip_ref.namelist():
        if file_name.endswith(".pdf"):
            print(f"Processing file: {file_name}")

            # Extract the file to a temporary location
            with zip_ref.open(file_name) as file:
                # pdfplumber to read the content of the PDF
                with pdfplumber.open(file) as pdf:
                    combined_content = ""
                    for page in pdf.pages:
                        page_content = page.extract_text()
                        if page_content:
                            combined_content += page_content.strip() + "\n\n"

                    # document for indexing
                    document = {
                        "file_name": file_name,
                        "content": combined_content.strip(),
                        "timestamp": datetime.now().isoformat()  # Current timestamp
                    }

                    # Index the document in Elasticsearch
                    response = es.index(index=index_name, document=document)
                    print(f"Document indexed for {file_name}: {response}")
