FROM docker.esf.fangdd.net/fdd-inspection:2
COPY requirements.txt .
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
RUN apk add nginx
RUN mkdir /run/nginx
COPY conf/nginx.conf /etc/nginx/
COPY conf/default.conf /etc/nginx/conf.d/
COPY . .
EXPOSE 65387 8000 80
ENV TZ Asia/Shanghai
CMD ./start.sh
