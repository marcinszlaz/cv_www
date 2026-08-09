FROM python:3.12-slim
WORKDIR /app
COPY app.py requirements.txt .flaskenv ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --break-system-package -r requirements.txt
#CMD ["python", "-u", "-m", "flask", "run"]
CMD ["python", "-u", "-m", "gunicorn", "-k", "gevent", "-w", "4", "-b", "0.0.0.0:5015", "app:app"]
