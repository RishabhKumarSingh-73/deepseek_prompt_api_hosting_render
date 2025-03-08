from supa.connection import supabase

async def insert(message:str):
    response = (
    supabase.table("response")
    .insert({"message": message})
    .execute()
    )

    return response

    
async def query_by_id(id:int):
    response = (
    supabase.table("response")
    .select("*")
    .eq("id", id)
    .execute()
    )
    return response

async def query_all():
    response = (
    supabase.table("response")
    .select("*")
    .execute()
    )
    return response