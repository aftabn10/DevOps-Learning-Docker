# Base image
FROM python:3.8-slim

# Set working directory in container
WORKDIR /app

# Install dependencies (Flask and redis)
COPY app.py .
RUN pip install flask redis

# Copy files from local folder into container
COPY . .

# Expose port for external access
EXPOSE 5002

# Run the application
CMD ["python", "app.py"]