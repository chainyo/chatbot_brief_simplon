FROM python:3.8.9-slim-buster

COPY . /app

RUN pip install -r ./app/requirements.txt

EXPOSE 8081

RUN python -m nltk.downloader punkt

RUN python -m nltk.downloader stopwords

RUN python -m nltk.downloader wordnet

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]