# Use Python 3.9 or newer
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first (to optimize Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port
EXPOSE 8000

# Start Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
