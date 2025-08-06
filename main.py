from fastapi import FastAPI
from pydantic import BaseModel
from embedding import load_data, build_index
from llama_api import generate_response
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

class Query(BaseModel):
    question: str

# Load data and embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
data = load_data()
index, texts = build_index(data, model)

@app.post("/chat")
def chat(query: Query):
    query_vec = model.encode([query.question])
    _, I = index.search(np.array(query_vec), k=3)
    results = [data[i] for i in I[0]]

    profile_text = "\n".join([
        f"{e['name']} - Skills: {', '.join(e['skills'])}, Experience: {e['experience_years']} yrs, Projects: {', '.join(e['projects'])}, Availability: {e['availability']}"
        for e in results
    ])

    prompt = f"""
    You are a smart and professional HR assistant at a tech company.

    The user asked: "{query.question}"

    Below are some candidate profiles from our internal database. Your task is to analyze them and write a recommendation in a warm, helpful tone.

    Highlight:
    - Relevant skills
    - Past projects
    - Domain match (e.g. healthcare)
    - Their current availability

    Avoid using gender-specific pronouns like 'he' or 'she'. Use their name or 'they/them'.
    Avoid using closing phrases like “Best wishes” or “Sincerely.” Just end after the recommendations.

    Candidate Profiles:
    {profile_text}
    """

    answer = generate_response(prompt)
    return {"response": answer.strip()}

@app.get("/employees/search")
def search(skill: str = None, min_exp: int = 0):
    matches = []
    for emp in data:
        if skill and skill not in emp['skills']:
            continue
        if emp['experience_years'] < min_exp:
            continue
        matches.append(emp)
    return {"results": matches}