FROM golang:alpine as builder
ARG DIR="/home/test"
RUN apk update \
	&& apk upgrade \
	&& apk add --update --no-cache alpine-sdk \
		   --virtual build-dependencies
WORKDIR $DIR
COPY . $DIR
RUN make all

FROM alpine:latest
WORKDIR /tool
COPY --from=builder /home/test/bin /usr/bin
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
#ENTRYPOINT ["ping-go"]
#CMD [""]
