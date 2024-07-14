# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV APP_HOME=/app
ENV VENV_PATH=$APP_HOME/venv
ENV PATH="$VENV_PATH/bin:$PATH"

# Set the working directory in the container
WORKDIR $APP_HOME

# Install system dependencies, including ffmpeg
RUN apt-get update --no-cache \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv $VENV_PATH

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies into the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run the application
CMD ["python", "-m", "PyroUbot"]
