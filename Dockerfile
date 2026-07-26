FROM python:3.9-alpine
WORKDIR /app
# Update Alpine packages to patch the OpenSSL vulnerability
RUN apk update && apk upgrade --no-cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
