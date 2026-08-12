import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT") or 8000)
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in {"1", "true", "yes", "on"}
    app.run(host="0.0.0.0", port=port, debug=debug)
