from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("fine-tuning-data/TEDTalks.csv", "rb"),
  purpose="fine-tune"
)

client.fine_tuning.jobs.create(
  training_file="fine-tuning-data/TEDTalks.csv",
  model="gpt-3.5-turbo"
)


completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
  messages=[
    {"role": "system", "content": "You are a professional programming tutor. You write attractive technical tutorial for posting"},
    {"role": "user", "content": "Give me a technical tutorial to post today"}
  ]
)
print(completion.choices[0].message)