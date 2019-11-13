FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /p1.py
ADD . /test.py
ADD , /CAP2
WORKDIR /CAP2
RUN pip install Flask==1.0.2
ENTRYPOINT ["python"]
CMD ["-m unittest test"]