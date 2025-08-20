FROM python:3.13.5-slim-bullseye

WORKDIR /docekr

COPY requirements.txt ./

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m","flask","--app","app","run","--host=-0.0.0.0"]

