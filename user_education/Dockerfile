FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    procps \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

RUN ls

EXPOSE 8000

CMD ["sh", "./start.sh"] 