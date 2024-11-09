# Start with a lightweight Python 3.12 base image on Alpine
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy the necessary files into the container
COPY config.py generator.py run.py requirements.lock ./

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir -r requirements.lock

# Set the default command to execute `run.py`
CMD ["python", "run.py"]