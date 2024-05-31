FROM python:3.8-slim

WORKDIR /app

# Install dependencies for MySQL and Python
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && apt-get clean

# Install Python packages
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables and run the application
CMD ["flask", "run", "--host=0.0.0.0"]
