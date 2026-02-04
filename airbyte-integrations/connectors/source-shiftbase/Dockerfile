# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Sets the working directory in the container
WORKDIR /airbyte/integration_code

# Copies the requirements file into the container
COPY requirements.txt ./

# Installs any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of your connector's code into the container
COPY . ./

# Airbyte's convention is to provide the entrypoint script at /airbyte/integration_code/main.py
ENTRYPOINT ["python", "/airbyte/integration_code/main.py"]