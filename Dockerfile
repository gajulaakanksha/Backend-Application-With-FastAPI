# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application cose into the container
COPY . .

# Expose the port  FastAPI will run on   
EXPOSE 8000

# Define the Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
