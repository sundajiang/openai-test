import openai
print("Hello, World!")
openai.api_key = "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"

# 提问
issue = '解释一下：一切圣贤，皆以无为法而有差别'

# 访问OpenAI接口
response = openai.Completion.create(
  #model='text-ada-001',
  model='text-davinci-003',
  #model='ChatGpt',
  prompt=issue,
  temperature=0.9,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6
)

# 返回信息
resText = response.choices[0].text

print(resText)


