FROM python:3.7-slim

# Build image:
#   docker build -t mobility_model:0.1.0 .
# Run image:
#   docker run -d --name model -p 9002:9002 --env LOGGING_LEVEL=DEBUG mobility_model:0.1.0

RUN apt-get clean && \
    apt-get update -qy && \
    apt-get install -y python-dev python-pip --fix-missing && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9002

RUN chmod +x ./start.sh
CMD ["sh", "./start.sh"]
