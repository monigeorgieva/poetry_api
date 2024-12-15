import pytest
import allure
from apis.api_poem_by_title import ApiGetPoemByTitle


@pytest.mark.TestGetPoemByTitle
@allure.title("Test Get Poem By Title")
@allure.description("Test for getting a poem by title")
@pytest.mark.normal
class TestGetPoemByTitle:
    api_get_poem_by_title = ApiGetPoemByTitle()

    @allure.description("Send a get request to /title with parameter 'title'"
                        "Expected result: get a poem by title")
    def test_get_poem_by_title(self):
        title = "Ozymandias"
        linecount = 14
        author = "Percy Bysshe Shelley"
        poem = self.api_get_poem_by_title.get_poem_by_title(title)

        assert len(poem) > 0, "Expected at least one poem"
        for poem in poem:
            assert poem.title == title, f"Expected title to be '{title}', but got '{poem.title}'."
            assert poem.author == author, f"Expected author to be '{author}', but got '{poem.author}'."
            assert poem.linecount == linecount, f"Expected number of linecount to be '{linecount}', but got '{poem.linecount}'."
