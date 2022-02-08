FROM ubuntu:latest


WORKDIR / 
RUN apt-get update && apt-get -y install iputils-ping
COPY . .

CMD [ "bash" ]

# nerdctl build . -f Dockerfile -t takke/ubuntu
# nerdctl run -it --rm takke/ubuntu
# nerdctl rmi takke/ubuntu
# nerdctl rmi takke/ubuntu ; nerdctl build . -f Dockerfile -t takke/ubuntu && nerdctl run -it --rm takke/ubuntu