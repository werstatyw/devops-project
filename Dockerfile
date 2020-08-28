FROM python
COPY . /src
CMD ["python", "hello.py"]