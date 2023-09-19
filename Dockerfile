# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application's source code into the container
COPY . .

# Expose port 5000, which is the default port for Flask applications
EXPOSE 5000

# Define the command to run your application
CMD ["python", "Func3.py"]
