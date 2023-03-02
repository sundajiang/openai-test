import openai
print("Hello, World!")
openai.api_key = "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"


response = openai.Image.create_edit(
  image=open("xiaoyu.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="在可爱的小孩旁边，有一只可爱的大狗，狗狗嘴里叼着一个绿色皮球",
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)