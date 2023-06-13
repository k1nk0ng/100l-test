FROM ubuntu

WORKDIR /100l
COPY /100l .

RUN apt-get update -y && \
    apt-get install -y python3-pip
RUN pip3 install pip --upgrade pip && \
    pip3 install -r reqs.txt

CMD ["python3", "starter.py"]
