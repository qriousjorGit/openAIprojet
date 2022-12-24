import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="3 short beginner examples with 'call off",
  temperature=0.5,
  max_tokens=80,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0,
  stop=["You:"]
)
#
# target_language = input("I'm looking for examples of: ")
#
# response2 = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=f"3 short beginner sentences using '{target_language}'",
#   temperature=0.5,
#   max_tokens=80,
#   top_p=1,
#   frequency_penalty=0.5,
#   presence_penalty=0,
#   stop=["You:"]
# )
#
# print(response2['choices'])
# print(response2['choices'][0])
#
# rlist = response2['choices'][0]['text'].replace('\n', '<br>')
# print(rlist)

def get_sentences(tl):
    data = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"3 beginner sentences (past, present, and future) and 1 intermediate sentence using '{tl}'",
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["You:"]
    )
    return (data['choices'][0]['text'].replace('\n', '<br><br>'))

# print(get_sentences('pass the buck'))
