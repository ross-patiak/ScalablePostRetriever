# Description:

**posts-api:** A placeholder API that supposed to represent any generic API that retrieve *(1)* all posts in a database, or *(2)* all posts that contains at most one tag. The placeholder database I've created is immutable and is only 1000 posts long.

  

**app.py (the main API):** This backend program returns a list of posts from a generic API like posts-api. Unlike posts-api, this API can retrieve based on any number of tags and can be sorted. Since posts-api can only retrieve posts one tag at a time, requests would be expensive and time-consuming. However, this program circumvents this problem by running API calls concurrently using multi-threading. It then stores the results of these API requests to a cache, which would allow the program to bypass API calls completely for common requests, thus significantly accelerating look-up times.

  
  

## How To Run:

1. Install Flask by running command: `pip install flask`.

2. Install Flask-RESTful by running command: `pip install flask-restful`.

3. Run command `python3 posts-api.py` to run the complementary API

4. Run command `python3 app.py` to run the main API.
