import openai
openai.api_key = "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"

prompt = "Hello, how are you?"
model = "text-davinci-003" # or any other model you want to use
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1000
)

print(response.choices[0].text)
