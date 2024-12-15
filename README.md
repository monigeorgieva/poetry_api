### **Project Overview**

This project is an automated testing suite for testing of API endpoint for https://poetrydb.org/index.html, including getting of poem by author, by title, getting of random poem, getting 
of random poems by count and getting of all authors. It uses Pytest for test structuring, Requests module, Pydantic for validation of the field and Allure for reporting.

### **Installation steps:**

Clone the repository.
Create a virtual environment: 

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install all packages and dependencies outlined in the requirements.txt file:

```bash
pip install -r requirements.txt or pip3 install -r requirements.txt
```

Run the tests using pytest and allure:

```bash
pytest --alluredir=reports/allure-results
```

Open the generated allure reports:

```bash
allure serve reports/allure-results
```

### **Project structure:**

```plaintext
├── apis/
│ ├── api_all_authors.py
│ ├── api_all_authors_response.py
│ ├── api_poem_by_author.py
│ ├── api_poem_by_author_response.py
│ ├── api_poem_by_title.py
│ ├── api_poem_by_title_response.py
│ ├── api_random_poem.py
│ └── api_random_poem_response.py
├── config/
│ ├── configuration.py
│ └── logger.py
├── tests/
│ ├── test_get_authors.py
│ ├── test_get_poem_by_author.py
│ ├── test_get_poem_by_title.py
│ └── test_get_random_poems.py
├── reports/
├── validators/
│  └── validators.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```
### **Testcases:**

| Test Case ID          | Test Title                      | Description                                                    | Steps                                                                                     | Expected Result                                                                                           |
|-----------------------|---------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **TestCase01**        | Test Get All Authors            | Test getting all authors from the `/author` endpoint.          | 1. Send a GET request to `/author`.                                                       | 1. A list of authors is returned.                                                                         |
|                       |                                 |                                                                | 2. Verify the list is not empty and all items are strings.                                | 2. The list should contain only string values.                                                            |
| --------------------- | ------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------                                      |
| **TestCase02**        | Test Get Poem By Author         | Test getting poems by a specific author.                       | 1. Send a GET request to `/author` with the `author` parameter.                           | 1. A list of poems by the specified author is returned.                                                   |
|                       |                                 |                                                                | 2. Verify that all poems belong to the correct author.                                    | 2. All poems should match the specified author.                                                           |
| --------------------- | ------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------                                      |
| **TestCase03**        | Test Get Poem By Title          | Test getting a poem by its title.                              | 1. Send a GET request to `/title` with the `title` parameter.                             | 1. A poem with the specified title is returned.                                                           |
|                       |                                 |                                                                | 2. Verify the poem's title, author, and line count match the expected values.             | 2. Poem's title, author, and line count should match the expected.                                        |
| --------------------- | ------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------                                      |
| **TestCase04**        | Test Get Random Poem            | Tests getting a random poem from the `/random` endpoint.       | 1. Send a GET request to `/random`.                                                       | 1. A random poem is returned.                                                                             |
|                       |                                 |                                                                | 2. Verify the poem is not `None` and contains expected fields (title, author, lines).     | 2. Poem title and author should be strings, lines should be a list, and<br/> line count should be an int. |
| --------------------- | ------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------                                      |
| **TestCase05**        | Test Get Random Poems by Count  | Test getting a specific number of random poems.                | 1. Send a GET request to `/random` with the `count` parameter.                            | 1. The number of poems returned should match the specified count.                                         |
|                       |                                 |                                                                | 2. Verify that the returned list contains exactly the specified number of poems.          | 2. The returned list should contain exactly `count` poems.                                                |


### **Video:**


https://github.com/user-attachments/assets/f2987712-d14a-485b-afab-79c1b5cc7a07


