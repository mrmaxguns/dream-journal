---
layout: doc_file
title: Documentation
permalink: /docs/
sidebar_link: true
nextdoc: docs/1-quickstart.html

---

Welcome to the documentation here you will find information about the application and its use. All pages of the documentation are listed below.

## Table of Contents
{% for doc in site.docs %}
* [{{ doc.title }}](/{{ site.gh_url_prefix }}{{ doc.url }})
{% endfor %}

If you have a question or issue not addressed in the documentation, please feel free to open up [an issue](https://github.com/mrmaxguns/dream-journal/issues/new?body=Type+your+issue+here) or pull request (if you know how to fix a bug)
