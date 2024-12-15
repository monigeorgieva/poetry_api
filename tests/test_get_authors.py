import allure
import pytest
from apis.api_all_authors import ApiGetAllAuthors


@pytest.mark.TestGetAllAuthors
@allure.title("Test Get All Authors")
@allure.description("Test for getting all authors")
@pytest.mark.normal
class TestGetAllAuthors:
    api_get_all_authors = ApiGetAllAuthors()

    @allure.description("Send a get request to /author without any parameters"
                        "Expected result: get a list with all authors")
    def test_get_authors(self):
        authors = self.api_get_all_authors.get_authors()

        assert len(authors) > 0, "The authors list should not be empty."
        assert all(isinstance(author, str) for author in authors), "All items in the authors list should be strings."
