FROM python:3.10
RUN apt-get update 
RUN apt-get install -y sqlite3 
RUN apt-get install -y libsqlite3-dev
RUN apt-get install -y libglib2.0-0 ffmpeg libsm6 libxrender1 libxext6
WORKDIR /usr/src/
COPY ./apps /usr/src/apps
COPY ./local.sqlite /usr/src/local.sqlite
COPY ./requirements.txt /usr/src/requirements.txt
COPY ./model.pt /usr/src/model.pt
RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
RUN echo "building..."
ENV FLASK_APP "apps.app:create_app('local')"
ENV IMAGE_URL "/storage/images/"
EXPOSE 5000
CMD ["flask","run","-h","0.0.0.0"]
