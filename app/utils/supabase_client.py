from functools import lru_cache
from flask import current_app
from supabase import create_client


@lru_cache(maxsize=1)
def get_supabase_client():
    """Create the Supabase client only when an API-backed operation needs it."""
    url = current_app.config.get("SUPABASE_URL")
    key = current_app.config.get("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be configured to use the Supabase client")

    return create_client(url, key)
