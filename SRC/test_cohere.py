import cohere
import os

co = cohere.Client(os.getenv("COHERE_API_KEY"))

response = co.chat(
    model="command-r-plus",
    message="C'est quoi une lettre de candidature ?"
)

print(response.text)