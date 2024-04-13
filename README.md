# IT Revolution final task

## Running locally

### Installing using Github

Python 3.11+ is a must

1. Clone the repository in the terminal:
`git clone https://github.com/vladlevkovich/it-revolution-24.git`
2. Create virtual env:
`python -m venv venv`
3. Setup virtual env:
    * On Windows: `venv\Scripts\activate`
    * On Linux or MacOS: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Make migrations: `python manage.py migrate`
6. Now you can run it: `python manage.py runserver`

### Running with Docker

## See API on the server

Use the following link to test this API:
`https://it-revolution-24.onrender.com`

**Notice:** it is required to be authorized, so use these urls first:
- `/users/register`
- `/users/login/`

All details in the documentation:

`here would be a swagger link`

