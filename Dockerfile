FROM python:3.8.6

RUN python -m pip install --upgrade pip
RUN pip install poetry

WORKDIR /usr/src/app

COPY . .

RUN poetry config virtualenvs.create false && poetry install

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]