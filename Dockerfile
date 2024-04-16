FROM python:3.11.9-bullseye

WORKDIR /usr/src/app

COPY Requirements.txt ./
RUN pip install -r Requirements.txt

COPY main.py ./

CMD [ "python", "./main.py" ]