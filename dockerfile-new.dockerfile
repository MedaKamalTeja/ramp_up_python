# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Robot Framework test suites and any other code
COPY . /app

# Install Robot Framework and any other dependencies
RUN pip install robotframework

# Expose ports or configure environment variables if needed
# ...

# Run Robot Framework tests
CMD ["robot", "C:\Users\Kamal Teja INT-212\PycharmProjects\Myproject\Framework"]
