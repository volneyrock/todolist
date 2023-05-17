FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app 

# Install any needed packages specified in poetry.lock
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Gunicorn port
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "ToDoList.wsgi:application", "-b", "0.0.0.0:8000"]