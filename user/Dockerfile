FROM python:3.12-slim



RUN apt-get update && apt-get install -y netcat-openbsd 

WORKDIR /code


COPY python_helpers /tmp/python_helpers
RUN pip install /tmp/python_helpers

COPY user/requirements.txt ./requirements.txt


RUN pip install --no-cache-dir -r requirements.txt


COPY user/. .

RUN chmod +x start.sh

RUN ls

EXPOSE 8001 

CMD ["sh", "./start.sh"]
