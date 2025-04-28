# syntax=docker/dockerfile:1
FROM python:3.12-alpine
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./src /src
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
