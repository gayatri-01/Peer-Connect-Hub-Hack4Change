# Use the official Python image
FROM python:3.12.3

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt --verbose

# Copy the rest of the application code
COPY . .

# Specify the command to run the app
CMD [ "python", "app.py"]