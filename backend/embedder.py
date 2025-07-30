from sentence_transformers import SentenceTransformer

# Load model only once globally
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    return model.encode(text)
