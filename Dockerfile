FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /CAP2/app.py
ADD . /CAP2
WORKDIR /CAP2
RUN pip install Flask==1.0.2
EXPOSE 5000
CMD ["python", "app.py"]