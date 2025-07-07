FROM python:3.11.9

WORKDIR /app

COPY ../requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["sh"]

# build conatiner docker build -f docker/Dockerfile -t myimage:latest .
#run the container + jupyter + port docker run -it --rm -p 8888:8888 -v "${PWD}:/app" myimage:latest jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root