#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import os
import openai

def init():
    # Set the API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # You can also set organization if needed
    # openai.organization = os.getenv("OPENAI_ORG_ID")

def run(raw_data):
    try:
        # Parse input JSON
        data = json.loads(raw_data)
        prompt = data.get("prompt", "")

        # Make request to OpenAI GPT-4 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo-2024-04-09",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )

        # Return the response content
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return json.dumps({"error": str(e)})

