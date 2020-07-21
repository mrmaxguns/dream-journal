[![An image showing the basic layout of the dream journal](docs/assets/img/home.gif)](https://mrmaxguns.github.io/dream-journal/)
<h1 align=center>Dream Journal</h1>

<p align=center>A simple, smart dream journal app built with python flask.</p>
<p align=center><a href="#installation">Install</a> | <a href="https://mrmaxguns.github.io/dream-journal/docs">Documentation</a> | <a href="https://mrmaxguns.github.io/dream-journal/contribute">Contribute</a></p>

## Installation

Make sure you have the following prerequisites:
1. Python >= 3.6
2. pip for your version of python
3. git versioning system

Installing the app is easy:

1. Clone the repository in the directory you wish: `git clone https://github.com/mrmaxguns/dream-journal.git`
2. Enter the `dream-journal` directory. (`cd dream-journal`)
3. Install requirements: `pip install -r requirements.txt`
4. Run the app: `python3 dream-journal/run.py`. On first run, the database will be created. A new tab with the app will open.

## Basic Usage

### The homepage
* The homepage lists all your recorded dreams with the most recent ones first. Click on a dream title in order to visit the dream log.
* The homepage also lists all the functions you can do such as creating a dream, searching dreams or filtering dreams.

## Creating a dream
* Go to the homepage and click on `Create a new dream` on the top left side of the screen.
* Fill out the form with the following information:
  * **Title**: the title must be unique for every dream and describe its contents.
  * **Write what happened in your dream**: in the next input, write out your dream in detail. This input also supports standard markdown headings, bold, italics, quotes, etc. The markdown will render whenever you visit the dream page.
  * **Tags**: write tags separated by a comma that you can use to sort and categorize your dream.
  * **Characters**: The characters in your dream separated by a comma. These can be yourself and even important objects.
  * **Locations**: The times and places of your dream separated by a comma.
  * **Type of dream**: The dream type describes if your dream is regular, a nightmare, lucid dream, etc.
  * **The date of your dream**: The date you had the dream. It is up to you to determine what date the dream happened on.
* Click the Create Dream button once you are done filling out the information.

## Viewing, editing, and deleting dreams
* The easiest way to access the dream is through the homepage. Dreams can also be accessed by searching or filtering.
* Once you open the dream page, you will find all information relating to the dream.
* To edit the dream, click the pencil icon. An editor will pop up. Make sure to save the edits by clicking the "Update" button on the bottom of the page.
* To delete a dream, click on the trash icon. It will then ask if you are sure. Click yes to delete the dream forever.
* To go back to the homepage, click the arrow pointing to the left side.

## Searching for dreams
* This app provides a basic keyword search feature that scans the titles and bodies of dreams and provides most relevant results.
* The search can be accessed through the homepage by clicking on the "Search" link next to a magnifying glass.
* Once at the search page, type your query. Results will show up below.

## Filtering dreams
* Filtering dreams is great for filtering tags, characters, locations and types of dreams.
* To open the filter page, go to the homepage and click the "Filter" text next to the funnel.
* Type your filter query: when typing the query, it must be exactly worded but case doesn't matter. Select the type of item you want to filter in the menu below and press "Filter".

# License
This project is licensed under the MIT license, so we value open-source contributions. Please see the LICENSE file for more details.

# Built with
* [Python 3](https://python.org): programming language
* [Flask](https://flask.palletsprojects.com): web framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com): database
* [Markdown2](https://github.com/trentm/python-markdown2): markdown support
* [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/): python WSGI server
* [Bootstrap](https://getbootstrap.com/): CSS and JS framework
* [Black](https://black.readthedocs.io/en/stable/): Python linting
* [Isort](https://timothycrosley.github.io/isort/): Import sorting

# Creator
Maxim R: [mrmaxguns](https://github.com/mrmaxguns)

# Contribute
Contributions are welcome! To learn how to contribute, visit [our official contribution page](https://mrmaxguns.github.io/dream-journal/contribute/)
