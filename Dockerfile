FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Change to the Django project directory
WORKDIR /app/dbms_proj

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]