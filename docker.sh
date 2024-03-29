#!/bin/bash
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp home.py tempdir/.
cp requirements.txt tempdir/.
cp database.db tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "COPY requirements.txt /home/myapp/" >>tempdir/Dockerfile

echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  home.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  database.db /home/myapp/" >> tempdir/Dockerfile
echo "RUN pip install -r /home/myapp/requirements.txt" >> tempdir/Dockerfile


echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/home.py" >> tempdir/Dockerfile

cd tempdir
docker build -t web2_app .

docker run -t -d -p 8080:8080 --name web2_apprunning web2_app

docker ps -a