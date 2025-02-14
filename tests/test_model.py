from pydantic import ValidationError
import sys
import os
import json
import pathlib

import pytest

# Add the parent directory to the sys.path to import model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jane_api.model import GrowLog


def check_growlog(file_path: str):
  try:
    with open(file_path, "r") as file:
      data = json.load(file)
    GrowLog.model_validate_json(json.dumps(data))
    print(f"The JSON data in {file_path} fits the model.")
  except ValidationError as e:
    print(f"The JSON data in {file_path} does not fit the model.")
    print(e)
  except Exception as e:
    print(f"An error occurred: {e}")


mock_path = str(pathlib.Path(__file__).parent.resolve())


def test_log1():
  try:
    check_growlog(mock_path + "/mocks/log1.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log2():
  try:
    check_growlog(mock_path + "/mocks/log2.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log3():
  try:
    check_growlog(mock_path + "/mocks/log3.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log4():
  try:
    check_growlog(mock_path + "/mocks/log4.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log5():
  try:
    check_growlog(mock_path + "/mocks/log5.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log6():
  try:
    check_growlog(mock_path + "/mocks/log6.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log7():
  try:
    check_growlog(mock_path + "/mocks/log7.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log8():
  try:
    check_growlog(mock_path + "/mocks/log8.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log9():
  try:
    check_growlog(mock_path + "/mocks/log9.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log10():
  try:
    check_growlog(mock_path + "/mocks/log10.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log11():
  try:
    check_growlog(mock_path + "/mocks/log11.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")


def test_log12():
  try:
    check_growlog(mock_path + "/mocks/log12.json")
  except ValidationError as e:
    pytest.fail(f"Validation error: {e}")
