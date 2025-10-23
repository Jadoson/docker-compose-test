FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "/src/main.py"]