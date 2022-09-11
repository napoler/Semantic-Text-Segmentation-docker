# FROM python:3.9
FROM python:3.9-buster

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install -r requirements.txt -i Https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install  "uvicorn[standard]" -i Https://pypi.tuna.tsinghua.edu.cn/simple && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader stopwords

#
COPY ./ /code/

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
