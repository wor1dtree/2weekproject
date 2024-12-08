FROM python
WORKDIR /app
COPY templates ./templates
COPY web.py ./
RUN pip install flask
CMD ["python", "web.py" ]