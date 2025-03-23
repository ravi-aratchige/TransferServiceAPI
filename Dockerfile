# Use official Python image as base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port (default 8000)
EXPOSE 8000

# Command to run the application
CMD ["fastapi", "run", "main.py"]
