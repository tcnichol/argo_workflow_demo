FROM python:3.11-slim

# Copy the test script into the container
COPY test.py /app/test.py

# Set the working directory
WORKDIR /app

# Set the entrypoint to run python with the script
ENTRYPOINT ["python", "test.py"]

# Set default command (can be overridden)
CMD []