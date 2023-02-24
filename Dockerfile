FROM python:3.8-slim

EXPOSE 8000

WORKDIR /app

COPY . .

RUN chmod -R 777 entrypoint.sh
RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["./entrypoint.sh"]