FROM python:3.9

WORKDIR /home

COPY requirements.txt ./
COPY src/MLmodel.pkl ./src/
COPY src/app.py ./src/

RUN pip install -r requirements.txt

ENV FASTAPI_APP = app.py

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port" , "8000"]
