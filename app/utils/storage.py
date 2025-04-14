from app.utils.supabase_client import supabase
import os

def get_supabase_public_url(path: str) -> str:
    bucket = os.getenv("SUPABASE_BUCKET")
    return supabase.storage.from_(bucket).get_public_url(path)

# def get_supabase_public_url(filename):
#     base_url = getenv("SUPABASE_URL")
#     bucket = getenv("SUPABASE_BUCKET")
#     return f"{base_url}/storage/v1/object/public/{bucket}/uploads/{filename}"