# text_similarity

An example of deploying a Flask API using Docker

The API contains one endpoint which accepts a post request containing a JSON array of two strings. Returns the computed cosine similarity between the vectorized strings.

 ## 1. Pull the Docker image from DockerHub
 
 `docker pull elusiveaxion/text_similarity:latest`
 
 ## 2. Build a Container From The Docker Image
 
 `docker run -p 3000:3333 -d --name text_similarity elusiveaxion/text_similarity:latest`
 
 ## 3. Access the API
 The easiest way to test this out is to use the test script in this repository.
 Ensure Python is installed ([python.org](https://python.org))
 Clone this repository:
 `git clone https://github.com/mrdawson/text_similarity.git`,
 open a terminal and navigate to `cd text_similarity/scripts`, and run
 `python test_script.py`
 
   