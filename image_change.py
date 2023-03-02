import openai
print("Hello, World! ttt")
openai.api_key = "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"


response = openai.Image.create_variation(
  image=open("xiaoyu.png", "rb"),
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

#https://platform.openai.com/docs/guides/images/usage
#http://www.aqwu.net/wp/?p=1315