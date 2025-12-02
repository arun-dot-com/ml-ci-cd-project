# Dockerfile

# Use a lean official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to take advantage of Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the application will run on (e.g., if using Flask/FastAPI)
EXPOSE 8080

# Command to run the application
# For simplicity, we just run the app.py to confirm it executes
CMD ["python", "app.py"]
