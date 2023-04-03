FROM python:3.9
LABEL Maintainer="Sheren Shaikh"

WORKDIR /home

#copy all the files to the container
COPY requirements.txt ./
COPY src ./src

#install all libraries
RUN pip install -r requirements.txt

#run the tests
RUN pytest

ENV FASTAPI_APP = app.py

#exposing container port
EXPOSE 8000

#command to run the API
CMD ["uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port" , "8000"]
