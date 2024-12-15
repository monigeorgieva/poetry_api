import pytest
import allure
from apis.api_poem_by_author import ApiGetPoemByAuthor


@pytest.mark.TestGetPoemByAuthor
@allure.title("Test Get Poem By Author")
@allure.description("Test for getting poems by author")
@pytest.mark.normal
class TestGetPoemByAuthor:
    api_get_poem_by_author = ApiGetPoemByAuthor()

    @allure.description("Send a get request to /author with parameter 'author'"
                        "Expected result: get a list with a poem by specific author")
    def test_get_poem_by_author(self):
        author = "Emily Dickinson"
        poems = self.api_get_poem_by_author.get_poem_by_author(author)

        assert len(poems) > 0, "Expected at least one poem"
        for poem in poems:
            assert poem.author == author, f"Expected author to be '{author}', but got '{poem.author}'."

