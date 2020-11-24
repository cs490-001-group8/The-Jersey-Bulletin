"""
    Fetch New Jersey National Park Information
"""

import os
import json
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

KEY_API_KEY = "api_key"
KEY_STATE_CODE = "stateCode"
KEY_STATE_NJ = "nj"
KEY_PARK_NAME = "name"
KEY_DATA = "data"
KEY_FULLNAME = "fullName"
KEY_URL = "url"
KEY_DESCRIPTION = "description"
KEY_GEO_COORDINATES = "geocoding_coordinates"
KEY_LATITUDE = "latitude"
KEY_LONGITUDE = "longitude"
KEY_ACTIVITIES = "activities"
KEY_ACTIVITY_NAME = "name"
KEY_FEES = "fees"
KEY_COST = "cost"
KEY_ENTRANCEFEES = "entranceFees"
KEY_DIRECTIONS_INFO = "directionsInfo"
KEY_DIRECTIONS_URL = "directionsUrl"
KEY_OPERATING_HOURS = "operatingHours"
KEY_STANDHOURS = "standardHours"
KEY_IMAGES = "images"
KEY_IMAGE_ALT_TEXT = "altText"
KEY_IMAGE_CAPTION = "caption"
KEY_IMAGE_URL = "url"
KEY_TIMESTAMP = "timestamp"
KEY_ID = 'id'

NPS_BASE_URL = "https://developer.nps.gov/api/v1/parks?"
NPS_API_KEY = os.getenv("NPS_API_KEY")
NATIONAL_PARK_CACHE_FILE = "national_parks_cache.json"
CACHE_LIFE = 3600


def get_national_parks_from_cache():
    """
    check national_parks_cache and if data is recent
    then use that data to reduce number of API calls
    and the data doesn't get modify or change very often
    so doing caching make sense to save API calls and
    still have updated data
    """
    with open(NATIONAL_PARK_CACHE_FILE, "r", encoding="utf8") as cache_file:
        data = json.load(cache_file)
        current_timestamp = datetime.now().timestamp()
        if current_timestamp - data[KEY_TIMESTAMP] < CACHE_LIFE:
            return data
        return None


def national_parks():
    """
    Make API requests for NJ Nationa Parks
    """
    output = []
    cache_result = get_national_parks_from_cache()
    if cache_result:
        output = cache_result[KEY_DATA]
    else:
        payload = {KEY_API_KEY: NPS_API_KEY, KEY_STATE_CODE: KEY_STATE_NJ}

        response = requests.get(NPS_BASE_URL, params=payload)
        response = response.json()
        try:
            for each_park in response[KEY_DATA]:
                output.append(
                    {
                        KEY_ID: each_park[KEY_ID],
                        KEY_PARK_NAME: each_park[KEY_FULLNAME],
                        KEY_URL: each_park[KEY_URL],
                        KEY_DESCRIPTION: each_park[KEY_DESCRIPTION],
                        KEY_GEO_COORDINATES: {
                            KEY_LATITUDE: each_park[KEY_LATITUDE],
                            KEY_LONGITUDE: each_park[KEY_LONGITUDE],
                        },
                        KEY_ACTIVITIES: [
                            activity[KEY_ACTIVITY_NAME]
                            for activity in each_park[KEY_ACTIVITIES]
                        ],
                        KEY_FEES: [
                            {
                                KEY_COST: each[KEY_COST],
                                KEY_DESCRIPTION: each[KEY_DESCRIPTION],
                            }
                            for each in each_park[KEY_ENTRANCEFEES]
                        ],
                        KEY_DIRECTIONS_INFO: each_park[KEY_DIRECTIONS_INFO],
                        KEY_DIRECTIONS_URL: each_park[KEY_DIRECTIONS_URL],
                        KEY_OPERATING_HOURS: [
                            {
                                KEY_DESCRIPTION: each[KEY_DESCRIPTION],
                                KEY_STANDHOURS: each[KEY_STANDHOURS],
                            }
                            for each in each_park[KEY_OPERATING_HOURS]
                        ],
                        KEY_IMAGES: [
                            {
                                KEY_IMAGE_URL: each[KEY_IMAGE_URL],
                                KEY_IMAGE_CAPTION: each[KEY_IMAGE_CAPTION],
                                KEY_IMAGE_ALT_TEXT: each[KEY_IMAGE_ALT_TEXT],
                            }
                            for each in each_park[KEY_IMAGES]
                        ],
                    }
                )
            with open(NATIONAL_PARK_CACHE_FILE, "w", encoding="utf8") as cache_file:
                json_object = json.dumps(
                    {
                        KEY_TIMESTAMP: datetime.now().timestamp(),
                        KEY_DATA: output,
                    },
                    indent=4,
                )
                cache_file.write(json_object)
        except KeyError:
            pass
    return output
