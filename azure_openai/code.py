import os
import json
from openai import AzureOpenAI
import utils
import azure_openai.model as model


client = AzureOpenAI(
    api_key=utils.AZURE_API_KEY,
    azure_endpoint=utils.AZURE_ENPOINT,
    api_version=utils.AZURE_API_VERSION,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are specialized in LLMs.",
        },
        {
            "role": "user",
            "content": "What is a temperature setting?",
        }
    ],
    max_completion_tokens=model.MAX_COMPLETION_TOKENS,
    temperature=model.TEMPERATURE,
    top_p=model.TOP_P,
    frequency_penalty=model.FREQUENCY_PENALTY,
    presence_penalty=model.PRESENCE_PENALTY,
    model=model.DEPLOYMENT_MODEL_NAME
)

print(response.choices[0].message.content)

# ENTIRE RESPONSE

# dumped_response=response.model_dump()

# print(json.dumps(dumped_response, indent=2))
