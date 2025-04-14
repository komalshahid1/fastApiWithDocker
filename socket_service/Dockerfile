FROM python:3.12-slim

WORKDIR /code

COPY ./app /code/app

RUN pip install "uvicorn[standard]" fastapi

EXPOSE 8005

CMD ["uvicorn", "app.socket_server:app", "--host", "0.0.0.0", "--port", "8005", "--reload"]
