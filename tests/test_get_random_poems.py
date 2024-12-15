import pytest
import allure
from apis.api_random_poem import ApiGetRandomPoem
from apis.api_random_poem_response import ApiRandomPoemResponse


@pytest.mark.TestGetRandomPoems
@allure.title("Test Get Random Poems")
@allure.description("Test for getting random poems")
@pytest.mark.normal
class TestGetRandomPoems:
    api_get_random_poems = ApiGetRandomPoem()

    @allure.description("Send a get request to /random without any parameters"
                        "Expected result: get a random poem")
    def test_get_random_poem(self):
        random_poem = self.api_get_random_poems.get_random_poem()

        assert random_poem is not None, "Expected a poem, but got None."
        for poem in random_poem:
            assert isinstance(poem, ApiRandomPoemResponse), "Expected an instance of ApiRandomPoemResponse"
            assert isinstance(poem.title, str), "Poem title should be a string"
            assert isinstance(poem.author, str), "Poem author should be a string"
            assert isinstance(poem.lines, list), "Poem lines should be a list"
            assert isinstance(poem.linecount, int), "Poem linecount should be an integer"

    @allure.description("Send a get request to /random with parameter 'count'"
                        "Expected result: the number of poems returned should match the specified count")
    def test_get_random_poems_by_count(self):
        count = 3
        random_poems_by_count = self.api_get_random_poems.get_random_poem_count(count)

        assert len(random_poems_by_count) == count, f"Expected number of poems to be '{count}'"


