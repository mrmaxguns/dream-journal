---
layout: doc_file
title: Quickstart
previousdoc: docs/
nextdoc: docs/2-thehomepage.html
sidebar_link: true

---

## Prerequisites
Before you start the installation, make sure to have all the following prerequisites in order to successfully install this app:
* [Python 3.6 or greater](https://www.python.org/downloads/)
* [Pip (Pip Installs Packages](https://pip.pypa.io/en/stable/installing/)
* [Git Versioning System](https://git-scm.com/downloads)

## Installation
You will need to install this app through the terminal. Start out by heading to your terminal. If you don't know how check out the [windows](https://www.wikihow.com/Open-Terminal-in-Windows), [ubuntu](https://www.wikihow.com/Open-a-Terminal-Window-in-Ubuntu) or [mac](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac) tutorial.
* Head over to the directory in which you want to install dream-journal:
  ```bash
  cd THE_FOLDER_WHERE_YOU_WANT_TO_INSTALL
  ```
* Download dream journal by typing:
  ```bash
  git clone https://github.com/mrmaxguns/dream-journal.git
  ```
* Enter the new `dream-journal` directory:
  ```bash
  cd dream-journal
  ```
* You will then install all the requirements by typing the following command:
  ```bash
  pip install -r requirements.txt
  ```
* You are now set to run the applicaiton. On first run, the database will be created. Type the following command, and a browser window with the dream-journal should open:
  ```bash
  python dream-journal/run.py
  ```

## Running the program
Whenever you want to open up the dream journal, open the terminal and head over to the `dream-journal` directory. Run the app using:
```
python dream-journal/run.py
```

You are now set, and ready to use the journal. Head to the next tutorial in order to learn about the dream journal
