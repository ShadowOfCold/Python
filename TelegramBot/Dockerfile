FROM python:3.9

WORKDIR /CodeReview/Bot

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "TgBot.py" ]