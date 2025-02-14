# Example usage
import sys
import os
from pydantic import ValidationError
import pytest

# Add the parent directory to the sys.path to import model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jane_api.functions import get_grow_log_by_slug


def test_request():
  try:
    slug = "white-widow-auto-evxme"
    get_grow_log_by_slug(slug)
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")
  except Exception as e:
    pytest.fail(f"Unexpected error: {e}")
