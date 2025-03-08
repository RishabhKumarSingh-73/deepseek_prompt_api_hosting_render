from ai_codes.deepseek_r1_call import deepseek_call
from fastapi import FastAPI
from supabase import create_client, Client

url: str = "https://ctubglnwnmddsicyyvsn.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0dWJnbG53bm1kZHNpY3l5dnNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDEzNjE5MDcsImV4cCI6MjA1NjkzNzkwN30.8pCOURuF02IgSUHjUJlx3EVoAjsWe0JwGVRPskp1cIQ"
            
supabase: Client = create_client(url, key)

async def insert(message:str):
    
    response = (
    supabase.table("response")
    .insert({"message": message})
    .execute()
    )
    return response

app = FastAPI()

@app.post("/prompt/{prompt}")
async def prompt_and_store(prompt:str):

    prompt_answer : str = await deepseek_call(prompt)

    ans = remove_boxed_formatting(prompt_answer)

    insert_response = await insert(ans)

    return {"prompt_answer": prompt_answer, "insert_response": insert_response}


def remove_boxed_formatting(response: str) -> str:
    if response.startswith(r"\boxed{") and response.endswith("}"):
        return response[len(r"\boxed{"):-1]  
    return response
    
