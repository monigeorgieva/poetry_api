import requests
from apis.api_poem_by_title_response import ApiPoemByTitleResponse
from config.configuration import config
from typing import List
from config.logger import logger
from validators.validators import validate_poem


class ApiGetPoemByTitle:
    def get_poem_by_title(self, title: str) -> List[ApiPoemByTitleResponse]:
        """
        Get poem by title.

        :param title: The title of the poem.
        :return: A list of ApiPoemByTitleResponse objects.
        """
        url = f"{config.BASE_URL}/title/{title}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            poem_by_title_data = response.json()

            # Validate the poem data; returns a list of validated poem dictionaries
            validated_poems = validate_poem(poem_by_title_data)

            # Convert each validated poem dictionary to an ApiPoemByTitleResponse object
            return [ApiPoemByTitleResponse(**poem) for poem in validated_poems]

        except (requests.RequestException, ValueError) as e:
            logger.error(f"Error fetching poem by title: {e}")
            return []
