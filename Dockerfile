# Use a lightweight Python image (version 3.10)
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the working directory
COPY . .

# Expose the Flask app's port
EXPOSE 5926

# Start the Flask app
CMD ["python", "main.py"]
