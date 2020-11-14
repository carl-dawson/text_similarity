# text_similarity

An example of deploying a Flask API using Docker

The API contains one endpoint which accepts a POST request containing a JSON array of two strings. Returns the computed cosine similarity between the vectorized strings.

The following instructions should work on a linux system with the Docker engine and Python>=3.6 installed.
 
 ## 1. Pull the Docker image from DockerHub
 
 `docker pull elusiveaxion/text_similarity:latest`
 
 ## 2. Build/Run a Container from the Docker Image
 Build and run (`docker run`) a detached (`-d`) container named text_similarity (`--name text_similarity`) from the image pulled above. Connect port 3000 of the local machine to the exposed port 3333 of the docker image (`-p 3000:3333`).
 
 `docker run -p 3000:3333 -d --name text_similarity elusiveaxion/text_similarity:latest`
 
 ## 3. Access the API
 The easiest way to test this out is to use the test script in this repository.
 Ensure Python>=3.6 is installed ([python.org](https://python.org))
 Clone this repository:
 `git clone https://github.com/mrdawson/text_similarity.git`, navigate to `cd text_similarity/scripts`, and run
 `python3 test_script.py`
 
 Or, using curl:
 `curl -H 'Content-Type: application/json' -X POST -d '["test text one",
"test text two"]' localhost:3000/compare_texts`
 
   