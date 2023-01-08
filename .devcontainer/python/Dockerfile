FROM python:3.11.1-bullseye

# Install packages required for the development environment.
COPY dev_requirements.txt ./
RUN pip install --no-cache-dir -r dev_requirements.txt
RUN rm dev_requirements.txt

# Install packages required by the codes.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt