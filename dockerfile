FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]