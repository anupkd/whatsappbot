FROM python:3.7
COPY . /app
WORKDIR /app
#RUN apt-get update

RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
ENTRYPOINT ["python"]
CMD ["bot.py", "--host", "0.0.0.0"]