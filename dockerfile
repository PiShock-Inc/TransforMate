FROM python:3.11-alpine
COPY . .
RUN apk update && apk add --no-cache gcc libffi-dev c-ares-dev openssl-dev cargo make git musl-dev linux-headers python3-dev make cmake && pip3 install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-m", "main"]