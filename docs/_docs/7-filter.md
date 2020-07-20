---
layout: doc_file
title: The Filter Feature
previousdoc: docs/6-search.html

---

Another cool organization feature is the filter feature. It is especially handy when trying to sort by tags, but you can also sort by characters, locations and dream types (soon dates too).

![The right home menu containing the filter link](/{{ site.gh_url_prefix }}/assets/docs/6-search/right-menu.png)

To get to the filter feature:
* Go to the homepage and then click Filter.
**OR**
* Go to the `/filter` url.

The filter page has a query bar (where you type what you want to filter for) and a selection bar (where you type what you want to filter by).

![The right home menu containing the filter link](/{{ site.gh_url_prefix }}/assets/docs/7-search/filter.png)

* First type in what you want to filter for. Make sure it is exactly spelled. The filter is **not** case-sensitive.
* Then, choose a dropdown option for what you want to filter by:
  * **Tag**: tags are the most popular thing to filter by, as they are meant for filtering. Tags label each dream.
  * **Character**: filter for a certain character
  * **Location**: filter for a certain location
  * **Type**: filter by dream type
  
![The right home menu containing the filter link](/{{ site.gh_url_prefix }}/assets/docs/7-filter/filter-results.png)

Once you have selected an option and typed your query, click on the blue "filter" button. Results (if any) appear under the search form.

## A word on tags
As you may have already noticed, at the homepage, each dream has all of its tags next to the title.

![The right home menu containing the filter link](/{{ site.gh_url_prefix }}/assets/docs/7-filter/tags.png)

Clicking on the tag takes you automatically to the filter for that tag, which is extremely helpful when you want to get similar dreams. The same can also be done with locations, characters and dream types by going to a dream's page and clicking on the location/character/type.

## Query String Parameters

If you are especially interested, you can perform filters using query string paramters in the following way:

```
/filter?q=QUERY_GOES_HERE&by=FILTER_BY_GOES_HERE
```

* `q`: the query parameter
* `by`: the parameter specifying what you want to perform the filter by:
  * `tag`: for tags
  * `char`: for characters
  * `loc`: for locations
  * `type`: for dream types
  
For example, to query for the character "max" the url would be: `/filter?q=max&by=char`.
