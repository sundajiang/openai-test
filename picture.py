import openai
print("Hello, World!")
openai.api_key = "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"

response = openai.Image.create(
  prompt="模仿莫奈的风格，画一个女骑士，她的摩托车很有科技感，车轮冒出火焰，车尾飞翔着一群白鸽",
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)