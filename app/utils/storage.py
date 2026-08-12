from flask import current_app
from app.utils.supabase_client import get_supabase_client

def get_supabase_public_url(path: str) -> str:
    bucket = current_app.config.get("SUPABASE_BUCKET")
    base_url = (current_app.config.get("SUPABASE_URL") or "").rstrip("/")

    if not bucket or not base_url:
        raise RuntimeError("SUPABASE_URL and SUPABASE_BUCKET must be configured")

    computed_url = f"{base_url}/storage/v1/object/public/{bucket}/{path.lstrip('/')}"
    if not current_app.config.get("SUPABASE_KEY"):
        return computed_url

    try:
        return get_supabase_client().storage.from_(bucket).get_public_url(path)
    except Exception as exc:
        current_app.logger.warning("Using computed Supabase public URL after client error: %s", exc)
        return computed_url
