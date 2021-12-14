FROM python
COPY requirements.txt /home/myapp/
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  home.py /home/myapp/
COPY  database.db /home/myapp/
RUN pip install -r /home/myapp/requirements.txt
EXPOSE 8080
CMD python3 /home/myapp/home.py
