FROM python:3

WORKDIR /usr/src/app

COPY script/* ./

CMD ["python", "idbscript.py"]