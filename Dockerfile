FROM python:3.12-slim



RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

RUN chmod +x start.sh

RUN ls

CMD ["./start.sh"]
