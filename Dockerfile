
FROM rocker/r-base:latest

WORKDIR /usr/src/app
COPY rcode.r .
CMD ["Rscript", "rcode.r"]





