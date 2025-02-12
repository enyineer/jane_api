from pydantic import ValidationError
from jane_api.model import GrowLog
import requests

def get_grow_log_by_slug(slug: str) -> GrowLog:
    url = f"https://api.growithjane.com/public/growlogs/get?slug={slug}"
    print(f"Fetching data from {url}")
    response = requests.get(
        url=url,
        headers={
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "api.growithjane.com",
            "Origin": "https://growithjane.com",
            "Pragma": "no-cache",
            "Referer": "https://growithjane.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "TE": "trailers",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0"
        }
    )

    if response.status_code == 200:
        try:
            growlog = GrowLog.model_validate_json(
                json_data=response.text,
                strict=True
            )
            return growlog
        except ValidationError as e:
            print("The JSON data does not fit the model.")
            raise ValueError(e)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise Exception(e)
    else:
        raise ValueError(f"Failed to fetch data. Status code: {response.status_code}")