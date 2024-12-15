from typing import List
import requests
from apis.api_all_authors_response import ApiAllAuthorsResponse
from config.configuration import config
from config.logger import logger
from validators.validators import validate_authors


class ApiGetAllAuthors:
    def get_authors(self) -> List[str]:
        """
        Get all authors.

        :return: A list of authors.
        """
        url = f"{config.BASE_URL}/author"

        try:
            response = requests.get(url)
            response.raise_for_status()

            authors_data = response.json()
            authors_list = authors_data.get("authors")

            # Validation of the authors list
            validated_authors = validate_authors(authors_list)

            return ApiAllAuthorsResponse(authors=validated_authors).authors

        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching authors: {e}")
            return []
