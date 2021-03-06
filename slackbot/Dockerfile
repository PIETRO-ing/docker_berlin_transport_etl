FROM python:3.8-slim


WORKDIR /app

# copy requirements file from the directory the Dockerfile is in into the /app directory of the container
COPY requirements.txt /app

# executes pip install comand and installs all required python libraries
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "slackbot.py"]