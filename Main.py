from google import genai

client = genai.Client(api_key="AIzaSyBqPdUTaQmydVUcqlCxF-_TmjGNjcrzYXY")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain array in cpp",
)

print(response.text)