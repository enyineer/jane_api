from pydantic import ValidationError
import sys
import os
import json
import pathlib

# Add the parent directory to the sys.path to import model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jane_api.model import GrowLog

def check_growlog(file_path: str):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        growlog = GrowLog.model_validate_json(json.dumps(data))
        print(f"The JSON data in {file_path} fits the model.")
    except ValidationError as e:
        print(f"The JSON data in {file_path} does not fit the model.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    mock_path = str(pathlib.Path(__file__).parent.resolve())
    check_growlog(mock_path + "/mocks/log1_normal.json")
    check_growlog(mock_path + "/mocks/log2_normal.json")
    check_growlog(mock_path + "/mocks/log3_initial.json")
    check_growlog(mock_path + "/mocks/log4_big.json")
    check_growlog(mock_path + "/mocks/log5_most.json")
    check_growlog(mock_path + "/mocks/log6_old.json")
    check_growlog(mock_path + "/mocks/log7_outdoor.json")
    check_growlog(mock_path + "/mocks/log8.json")
    check_growlog(mock_path + "/mocks/log9_repetitions.json")