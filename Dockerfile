FROM python:3

RUN apt-get update

WORKDIR /usr/src/code_review_1

COPY . .

RUN pip install --no-cache -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD python3 Scraper.py \
    python3 Bot.py
