FROM python:3.6.9-alpine3.9
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk add build-base python3-dev musl-dev gcc g++ openssl-dev libffi-dev make
RUN apk add libsodium-dev
RUN apk add --update \
    curl \
    openjdk8 \
 && rm /var/cache/apk/* \
 && echo "securerandom.source=file:/dev/urandom" >> /usr/lib/jvm/default-jvm/jre/lib/security/java.security \
 && echo "networkaddress.cache.ttl=30" >> /usr/lib/jvm/default-jvm/jre/lib/security/java.security
RUN apk add unzip bzip2 font-adobe-100dpi fontconfig msttcorefonts-installer && update-ms-fonts && \
    fc-cache -f
RUN apk add libgcc
ENV PATH $PATH:/usr/lib/jvm/default-jvm/bin
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib/jvm/default-jvm/jre/lib/amd64/server/:/usr/lib/:/lib/
COPY requirements.txt .
RUN pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN apk add tzdata && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
COPY . .
EXPOSE 1322 8000
ENV TZ Asia/Shanghai
CMD ./start.sh