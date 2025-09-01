from openai import AzureOpenAI
import utils
import azure_openai.model as model
import requests


client = AzureOpenAI(
    api_key=utils.DALLE_API_KEY,
    azure_endpoint=utils.DALLE_ENDPOINT,
    api_version=utils.AZURE_API_VERSION,
)

prompt="A futuristic cat dwelling in the sunset, highly detailed, digital art"

response = client.images.generate(
        model=model.DEPLOYMENT_MODEL_DALLE_NAME,
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard",
)


image_url=response.data[0].url

image_data = requests.get(image_url).content
with open("img2.png","wb") as handler:
        handler.write(image_data)

print("Finished generating the image")
