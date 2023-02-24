FROM python:3.10-slim-buster

# Inside the container
# make a new folder inside the container
WORKDIR /backend-flask

#outside container  -> inside container
#this contains the libraries we want to install to run the app
COPY requirements.txt requirements.txt

#inside container
#install python libraies used for the app
RUN pip3 install -r requirements.txt

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/cache/apk/*
#outside container  -> inside container
# . means everthing in the current directory
#first . -/backend-flask (outside container)
#second . -/backend-flask (inside container)
COPY . .

#set environment variables
#inside container and will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

#command
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]