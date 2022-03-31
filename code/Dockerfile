FROM python:3.8-slim

COPY ./ ./src
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host=0.0.0.0","--reload","--port","15400"]