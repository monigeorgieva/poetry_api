from typing import List
import requests
from apis.api_random_poem_response import ApiRandomPoemResponse
from config.configuration import config
from validators.validators import validate_poem
from config.logger import logger


class ApiGetRandomPoem:
    def get_random_poem(self) -> List[ApiRandomPoemResponse]:
        """
        Get a random poem.

        :return: A list of ApiRandomPoemResponse objects containing the poem data.
        """
        url = f"{config.BASE_URL}/random"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    random_poem_data = response.json()

                    # Validate the poem data; returns a list of validated poem dictionaries
                    validated_poem_data = validate_poem(random_poem_data)

                    #  Convert each validated poem dictionary to an ApiRandomPoemResponse object
                    return [ApiRandomPoemResponse(**poem) for poem in validated_poem_data]
                except ValueError as e:
                    logger.error(f"Validation error: {e}")
                    return []
            else:
                logger.error(f"Failed to get poem: Status code {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return []

    def get_random_poem_count(self, count: int) -> List[ApiRandomPoemResponse]:
        """
        Get a list of random poems by count.

        :param count: The number of the random poems which will be retrieved.
        :return: A list of ApiRandomPoemResponse objects containing the poem data.
        """
        url = f"{config.BASE_URL}/random/{count}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    random_poem_data = response.json()

                    # Validate the poem data; returns a list of validated poem dictionaries
                    validated_poem_data = validate_poem(random_poem_data)

                    # Convert each validated poem dictionary to an ApiRandomPoemResponse object
                    return [ApiRandomPoemResponse(**poem) for poem in validated_poem_data]

                except ValueError as e:
                    logger.error(f"Validation error: {e}")
                    return []
            else:
                logger.error(f"Failed to get poem: Status code {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return []
