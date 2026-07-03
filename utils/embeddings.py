from sentence_transformers import SentenceTransformer

# Loads only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text):
    """
    Convert text into an embedding vector.
    """
    embedding = model.encode(text)

    return embedding.tolist()