FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY . .


CMD ["bot.py"]
ENTRYPOINT [ "python3" ]
