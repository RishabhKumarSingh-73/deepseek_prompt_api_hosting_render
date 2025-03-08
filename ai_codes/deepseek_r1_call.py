from openai import OpenAI

async def deepseek_call(prompt:str):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
    )

    completion = client.chat.completions.create(
        extra_headers={},
        model="deepseek/deepseek-r1-zero:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content