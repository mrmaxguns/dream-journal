---
layout: page
title: Contribute
permalink: /contribute/
sidebar_link: true

---
The dream journal repository:  [https://github.com/mrmaxguns/dream-journal/](https://github.com/mrmaxguns/dream-journal/)

Dream Journal is written in Python 3 using the Flask and Flask SQLAlchemy packages. It also uses bootstrap (v5) for the front-end. This means that a variety of contributions are welcome, including **but not limited to**:

* Python development
* Front-end with bootstrap
* Fixing typos in the code and docs
* Improving the documentation

We welcome all positive contributions, as long as the following rules are followed.

## General
* Hate speech, discrimination and derogatory comments are not welcome; we welcome feedback of any kind as long as it is not offensive
* The workflow is standard; all changes are made with pull requests (see: [Workflow](#workflow)).
* Issues must be descriptive and helpful; make sure you read the docs before creating an issue.

## Workflow
Our workflow is the standard fork/clone/commits/PR type. Please follow the steps below to set up for development. **Please note the git, Python 3.6 or greater and PIP are required**
* Fork [the github repository](https://github.com/mrmaxguns/dream-journal/).
* Clone your forked repository by typing the following (make sure to replace `YOUR_USERNAME` with your username:
  ```bash
  git clone https://github.com/YOUR_USERNAME/dream-journal.git
  ```
* Enter the `dream-journal` directory:
  ```bash
  cd dream-journal
  ```
* Add the original repository as the upstream by typing:
  ```bash
  git remote add upstream https://github.com/mrmaxguns/dream-journal.git
  ```
* Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
* Run the app:
  ```
  python3 dream-journal/run.py
  ```
* Make any commits and once done open a pull request. If you have any questions or problems with any of the steps above, please contact [@mrmaxguns](github.com/mrmaxguns).

## Developing With Python
If you choose to improve the python code, make sure to follow the simple rules below:
* Use minimal amounts of comments: your code should describe itself
* Use functions to store repeating tasks
* Use the latest version of python
* Before submitting a pull request:
  * Make sure to run `black .` (code linting). Black is installed with requirements.
  * Run `isort .` (import sorting). Isort is installed with requirements.
  
## Developing the HTML/CSS/JS
* When adding to the code, stick to the theme defined in the `static/css/main.css` file.
* Make sure to use bootstrap 5 when possible.
* Try to minimize JavaScript use whenever possible.
* Adding dynamic information will require the use of python; do not try to add in JavaScript.

## Questions/Comments/Concerns
If you have any questions, comments or concerns consider creating an issue or messaging [@mrmaxguns](https://github.com/mrmaxguns/).
