FROM python:3.12-slim

# Setup working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy over the application code
COPY . .

# Run Flask app
CMD ["python", "app.py"]
