---
layout: doc_file
title: The Search Feature
previousdoc: docs/5-editanddelete.html
nextdoc: docs/7-filter.html

---

Dream Journal employs a simple keyword search feature for dreams. The search is simple and straightforward. There are multiple ways to complete a search.

![The right home menu containing the search link](/{{ site.gh_url_prefix }}/assets/docs/6-search/right-menu.png)

To get to the search page:
* Go to the homepage and click "Search" next to the magnifying glass icon
**or**
* Go directly to the search url by going to `/search`.

The search page has a search bar and search button:

![The search page](/{{ site.gh_url_prefix }}/assets/docs/6-search/search.png)

To perform a search, type your query into the bar and click the button. All results show below the bar as shown:

![The search page with multiple search results](/{{ site.gh_url_prefix }}/assets/docs/6-search/search-results.png)

In the event that there are no results to your search, the following message will be displayed:

![The search page with no search results](/{{ site.gh_url_prefix }}/assets/docs/6-search/search-empty.png)

Clicking on any of the search result links will lead you to that dream's page.

## Query String Parameters

For those who are tech savvy or have interest in extracting data, a search can be performed with query string parameters. The url goes in the form of:
```
/search?q=QUERY+GOES+HERE
```
