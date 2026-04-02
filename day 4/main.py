from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("AI is", max_length=20)

print(result[0]['generated_text'])