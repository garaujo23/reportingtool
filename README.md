# Udacity Full Stack Assignment 1

Solution for Assignment 1 of the [Udacity](https://www.udacity.com/) Full Stack  nanodegree. The task is to create a reporting tool to answer questions about  
data in a database:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Quickstart

### Download database

Download the required database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). To setup use:

```command
psql -d news -f <news sql database file>
```

### Install

Download [Python 3.6](https://www.python.org/downloads/) - required to run the python script. Documentation available [here](https://docs.python.org/3.6/)

[psycopg2](http://initd.org/psycopg/docs/install.html) - required to connect to database. Documentation available [here](http://initd.org/psycopg/docs/usage.html). To install run:

```command
pip install psycopg2
```

### Database guide

The databse has three tables:

1) **Articles** - has columns author, title, slug, lead, body, time, id. Note that author is an ID matching table authors column ID.
2) **Authors** - has columns name, bio and ID.
3) **Log** - has columns path, IP, method, status, time and ID. Rows include information  on traffic to all articles, including status of HTTP codes sent to user's browser.

### Create Views

Use the following before running the python script to create the views used in the code. This step is only required once.

```command
psql -d news -f create_views.sql
```

View 1 is used to join the tables articles and authors

View 2 is used to count the views of articles by using the url and article slug from tables articles and log

View 3 is used to group and count total logs for each day

View 4 is used to group and count error logs for each day

View 5 is used to get the % error each day.

#### Command Line

```command
python Assignment.py
```

#### Example result

```text
What are the most popular three articles of all time?
"338647" - Candidate is jerk, alleges rival views
"253801" - Bears love berries, alleges bear views
...
```
