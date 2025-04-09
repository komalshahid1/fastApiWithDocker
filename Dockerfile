# FROM python:3.11

# # Install netcat (choose openbsd variant)
# RUN apt-get update && apt-get install -y netcat-openbsd

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY start.sh /start.sh
# RUN chmod +x /start.sh

# COPY . .

# CMD ["/start.sh"]




FROM python:3.12

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY alembic.ini .
COPY alembic ./alembic
COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY . .

CMD ["/start.sh"]
