# Inference using the SambaNova Cloud

[SambaNova Cloud](https://cloud.sambanova.ai/) is available for developers to easily use the best open source models at record-breaking inference speeds. These models are powered by our state-of-the-art AI chip, the SN40L. 

## Quick Start Guide

Get started using the SambaNova Cloud API in just a few minutes!

### Get your API key

1. Create an account on the [SambaNova Cloud Developer Portal](https://cloud.sambanova.ai/) to get an API key.
2. Once logged in, navigate to the [API Keys section](https://cloud.sambanova.ai/apis) of the portal and generate a new key. 
3. Save the API key securely. For example, you can set it as an environment variable:
   ```shell
   export SAMBANOVA_API_KEY="your-api-key-here"
   ```

### Pick a model

The SambaNova Cloud is frequently updated with latest open source models, running at the fastest tokens per second.

To make an inference request from a model, you’ll need the model’s corresponding model-id. The full list of models and corresponding model-id’s are [listed here](https://docs.sambanova.ai/cloud/docs/get-started/supported-models).

### Make an API request

You can make an inference request to our models in Python using several approaches, two of which are described below:
1. Open AI client library 
2. LangChain connectors

#### OpenAI client library

Install the OpenAI Python library, as shown below. Make sure you have Python3 and pip installed:
```shell  
pip install openai
```

Next, copy the code below into a python file called, `hello_world.py`.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key="your-api-key-here"
)

completion = client.chat.completions.create(
  model="Meta-Llama-3.1-405B-Instruct",
  messages = [
      {"role": "system", "content": "Answer the question in a couple sentences."},
      {"role": "user", "content": "Share a happy story with me"}
    ]
)

print(completion.choices[0].message.content)
```

Once copied into the file, replace the string field in "your-api-key-here" with your API Key value. Then run the file with the command below:
```shell  
python hello_word.py
```

#### LangChain connectors
See [here](https://docs.sambanova.ai/cloud/docs/integrations/langchain) to learn how to use LangChain with SambaNova models.

## Function Calling Examples

[SambaNova AI Starter Kits](https://github.com/sambanova/ai-starter-kit/) are a collection of open-source examples and guides to facilitate the deployment of AI-driven use cases, designed to support both enterprises and developers in their AI adoption journeys.

Start by cloning the starter kit repo:
```
git clone https://github.com/sambanova/ai-starter-kit.git
```

Then, update the API information by configuring the environment variables in the `ai-starter-kit/.env` file:
- Create the `.env` file at `ai-starter-kit/.env` if the file does not exist.
- Enter the SambaNova Cloud API key in the `.env` file, for example:
  
```bash
SAMBANOVA_API_KEY = "your-api-key-here"
```

**Note**: If you've already set your API key as an environment variable (for example, in your `.bashrc` or `.zshrc`), there's no need to create the `.env` file.

Below are three examples you can try. **We recommend using Python >= 3.10 and < 3.12**. 

### Example 1: Function Calling Basics 

After cloning the repository, go to `ai-starter-kit/quickstart`. Then, run the [function_calling_get_started.ipynb](https://github.com/sambanova/ai-starter-kit/blob/main/quickstart/function_calling_get_started.ipynb) notebook. 

### Example 2: Complete Function Calling App

This function calling kit is an example of tools calling implementation and a generic function calling module that can be used inside your application workflows. To build a complete function calling app, [click on this AI Starter Kit](https://github.com/sambanova/ai-starter-kit/blob/main/function_calling). 

## Additional Resources
- [SambaNova Cloud documentation](https://docs.sambanova.ai/cloud/docs/get-started/overview)
- [Integrations](https://docs.sambanova.ai/cloud/docs/integrations/overview)
- [AI Starter Kits](https://github.com/sambanova/ai-starter-kit)
- [SambaNova Agents Demo](https://aiskagents.cloud.snova.ai/)




