# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /ML_Code-1

# Copy the current directory contents into the container at /ML_Code-1
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

CMD ["python", "backend/script.py"]
