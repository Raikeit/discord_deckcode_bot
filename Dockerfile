FROM selenium/standalone-firefox

USER root
RUN apt update
RUN apt install -y python3 python3-pip

USER seluser
ADD src /discord
WORKDIR /discord

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]