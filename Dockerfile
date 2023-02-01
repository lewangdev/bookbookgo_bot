FROM python:3.11.1-slim-bullseye as builder

WORKDIR /app
RUN python -m venv venv 
ENV PATH="/app/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.11.1-slim-bullseye
WORKDIR /app
COPY --from=builder /app/venv venv
COPY . .

ENV PATH="/app/venv/bin:$PATH"
CMD ["python", "bookbookgo_bot/main.py"]
