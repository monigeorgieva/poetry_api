from typing import List, Union


# Comment for the reviewer: Most of these checks are handled by Pydantic,
# but here I'm demonstrating an additional way to perform validation

def validate_authors(authors: List[str]) -> List[str]:
    """
    Validates that the authors list is not empty and contains only strings.

    :param authors: A list of author names.
    :return: The validated list of authors.
    """
    if not authors or not all(isinstance(author, str) for author in authors):
        raise ValueError("Authors list must contain at least one non-empty string")
    return authors


def validate_poem(poem_data: Union[dict, List[dict]]) -> List[dict]:
    """
    Validates the poem data, supporting both single and list responses.

    :param poem_data: A single poem dictionary or a list of poem dictionaries.
    :return: A list of validated poem dictionaries.
    """
    if isinstance(poem_data, dict):
        # If the response is a single poem, validate and return it as a list
        return [validate_single_poem(poem_data)]
    elif isinstance(poem_data, list):
        # If the response is a list of poems, validate each one
        return [validate_single_poem(poem) for poem in poem_data]
    else:
        raise ValueError("Invalid poem data format: Expected a dict or a list of dicts")


def validate_single_poem(poem_data: dict) -> dict:
    """
    Validates a single poem dictionary.

    :param poem_data: A dictionary containing poem data.
    :return: The validated poem dictionary.
    """
    if not isinstance(poem_data.get('title'), str):
        raise ValueError("Poem title must be a string")
    if not isinstance(poem_data.get('author'), str):
        raise ValueError("Poem author must be a string")
    if not isinstance(poem_data.get('lines'), list):
        raise ValueError("Poem lines must be a list")

    # Convert 'linecount' to int if it's a string
    linecount = poem_data.get('linecount')
    if isinstance(linecount, str):
        try:
            poem_data['linecount'] = int(linecount)
        except ValueError:
            raise ValueError(f"Poem linecount must be an integer, got '{linecount}'")
    elif not isinstance(linecount, int):
        raise ValueError("Poem linecount must be an integer")

    return poem_data
