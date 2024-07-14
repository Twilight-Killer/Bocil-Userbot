FROM python:3.9-slim

RUN apt update

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "PyroUbot"]