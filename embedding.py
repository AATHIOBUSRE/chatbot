import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_data(path="employees.json"):
    with open(path, "r") as f:
        return json.load(f)["employees"]

def build_index(data, model):
    texts = [
        f"{e['name']} {' '.join(e['skills'])} {' '.join(e['projects'])} {e['experience_years']}"
        for e in data
    ]
    embeddings = model.encode(texts, convert_to_tensor=False)
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, texts