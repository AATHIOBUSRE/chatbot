# HR Resource Query Chatbot

Hi there 👋

This is a chatbot I built as part of the GeekyAnts AI/ML Engineer assessment. The idea is to help HR teams quickly find employees based on natural language queries — for example:

- “Find a Python developer with 3+ years of experience”
- “Who has worked on healthcare projects?”
- “Suggest someone for a React Native app”

The bot understands these queries, searches an employee database, and responds with natural-sounding recommendations — kind of like what you'd expect from a smart assistant.

## What I Used

- **FastAPI** to build the backend APIs
- **SentenceTransformers + FAISS** for semantic search (retrieval)
- **LLaMA 3 (via Ollama)** for generating humanlike recommendations (generation)
- **Streamlit** to make a simple interface to interact with the bot

Everything runs locally — no OpenAI key needed!

##  How to Run It Locally

**Step 1** – Make sure you have Python 3.8+ and [Ollama](https://ollama.com/download) installed.

**Step 2** – Pull the LLaMA 3 model (if you haven’t already):
ollama pull llama3

**Step 3** – Start LLaMa in one terminal
ollama run llama3

**Step 4** – In another terminal, run the backend
uvicorn main:app --reload

**Step 5** – Finally launch the UI
streamlit run app.py

## Example Query

**You can ask something like**

      Who has worked on healthcare projects?
      
**And the bot might reply with**

      Based on your request for candidates who have worked on healthcare projects, I'd like to recommend the following individuals:

      Claire Lee has a strong background in developing applications with a focus on user experience. Their skills include React Native and Firebase, which would be valuable assets in building scalable and efficient solutions. Notably, they have experience working on a Healthcare App project. They are currently available and could bring their expertise to our team.

      Alice Johnson has an impressive track record of delivering high-quality projects across various domains, including healthcare. With skills in Python and React, they can tackle complex tasks with ease. Their experience working on a Healthcare App project demonstrates their ability to understand and address the specific needs of the industry. They are also available for new opportunities.

      Kevin Garcia's diverse skill set spans multiple areas, including AI-powered attendance systems and image-based search engines. While their expertise may not be as directly aligned with healthcare, they have worked on a healthcare-focused project in the past. Their innovative approach to problem-solving could bring a fresh perspective to our team. They are currently available.

      All three candidates possess relevant skills and experience working on healthcare projects. However, if you're looking for someone with a more direct focus on healthcare software development, Claire Lee's experience might be the most closely aligned with your needs.

## How It Works

I load a sample JSON file with employee data.

When a query comes in, I embed it using a SentenceTransformer.

I use FAISS to search for the most relevant employees.

I format the results into a prompt and send it to LLaMA 3 (running locally).

LLaMA generates a nice response based on the data + query.

It’s simple, fast, and doesn’t rely on any cloud APIs.

## API Endpoints

POST /chat – Takes a query and returns a recommendation.

{
  "question": "Find AWS developers with Docker experience"
}

GET /employees/search – Filter employees by skill and experience.

/employees/search?skill=Python&min_exp=3


## AI Development Notes

I used LLaMA 3 locally via Ollama for generation.

For retrieval, I used the all-MiniLM-L6-v2 model from sentence-transformers.

I wrote all the logic myself, but occasionally used ChatGPT to brainstorm and debug.

Prompt tuning was important — I had to tweak it to make LLaMA give cleaner, HR-style answers.

## Why I Chose This Stack

FastAPI is clean and async-friendly.

Streamlit is fast to prototype and good for a chatbot UI.

FAISS + Sentence Transformers gave me fast, decent semantic search.

Ollama + LLaMA meant I didn’t need an API key or rely on cloud inference — everything runs locally.

## Things I'd to Improve If I Had More Time

Add authentication and user roles (e.g. only HR can access)

Use a real database instead of JSON

Make the UI cleaner and more interactive

Allow filtering by availability, domain expertise, etc.

Containerize the whole thing with Docker




