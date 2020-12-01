**HOW TO RUN**

Install:
> pip install -U pytest    
> pip install pytest-cov

Change working directory:
> cd issue_5

Check tests:
> pytest -v

Check for coverage in terminal:
> pytest -v --cov

Output coverage in htmlcov/index.html:
> pytest --cov . --cov-report html
