# GSG_fake_news

# Backend Server Setup 

## Prerequisites
- Python 3.7 or higher installed on your system.
- [pip](https://pip.pypa.io/en/stable/) (Python package manager) installed.
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) for creating a virtual environment.

## Installation

- clone the repo: `git clone <repo link>` 
- cd to the lab application: `cd GSG_fake_news/FastApiDataLab On Windows, use GSG_fake_news\FastApiDataLab`
- create virtual environment: `python -m venv venv`
- load the venv: `source venv/bin/activate  # On Windows, use venv\Scripts\activate`
- install the requirements: `pip install -r req.txt`
- cd to backend application: `cd Backend`
- run the server : `uvicorn main:app --reload`
