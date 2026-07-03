import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add(self, embeddings, texts):

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.texts.extend(texts)

    def search(self, embedding, k=4):

        vector = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(vector, k)

        return [self.texts[i] for i in indices[0]]