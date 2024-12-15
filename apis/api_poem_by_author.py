import requests
from typing import List
from apis.api_poem_by_author_response import ApiPoemByAuthorResponse
from config.configuration import config
from config.logger import logger
from validators.validators import validate_poem


class ApiGetPoemByAuthor:
    def get_poem_by_author(self, author: str) -> List[ApiPoemByAuthorResponse]:
        """
        Get poem by a specific author.

        :param author: The name of the author.
        :return: A list of ApiPoemByAuthorResponse objects.
        """
        url = f"{config.BASE_URL}/author/{author}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            poems_by_author_data = response.json()

            # Validate the poem data; returns a list of validated poem dictionaries
            validated_poems = validate_poem(poems_by_author_data)

            # Convert each validated poem dictionary to an ApiPoemByAuthorResponse object
            return [ApiPoemByAuthorResponse(**poem) for poem in validated_poems]

        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching poems by author: {e}")
            return []