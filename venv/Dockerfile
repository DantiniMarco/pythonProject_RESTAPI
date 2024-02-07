# Start your image with a node base image
FROM python:3.8-slim-buster

# The /app directory should act as the main application directory
WORKDIR /app

# Copy local directories to the current local directory of our docker image (/app)
COPY requirements.txt requirements.txt
COPY main.py main.py
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
