FROM python:3.12-slim



RUN apt-get update && apt-get install -y netcat-openbsd git

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

RUN chmod +x start.sh

RUN ls

EXPOSE 8001 

CMD ["sh", "./start.sh"]
