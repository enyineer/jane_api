# Example usage
import sys
import os
import json

# Add the parent directory to the sys.path to import model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jane_api.functions import get_grow_log_by_slug

slug = "white-widow-auto-evxme"
grow_log = get_grow_log_by_slug(slug)
print(json.dumps(grow_log.model_dump(mode="json"), indent=4))