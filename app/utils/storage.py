from app.utils.supabase_client import supabase
import os

def get_supabase_public_url(path: str) -> str:
    bucket = os.getenv("SUPABASE_BUCKET")
    return supabase.storage.from_(bucket).get_public_url(path)
