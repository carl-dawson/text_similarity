FROM python:3.7-slim

# Set the default working directory
WORKDIR /text_similarity/

# Copy requirements.txt outside the container
# to /app/ inside the container
COPY requirements.txt /text_similarity/

# Install required packages
RUN pip install -r ./requirements.txt

# Copy app.py and app/ outside the container
# to /text_similarity/ inside the container
COPY app.py /text_similarity/
COPY app/ /text_similarity/app/

# Expose the container's port 3333
EXPOSE 3333

# When the container starts, run this
ENTRYPOINT python ./app.py