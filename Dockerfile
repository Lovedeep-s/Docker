# Use the official R base image
FROM rocker/r-base:latest

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the R script into the container
COPY rcode.r .

# Run the R script
CMD ["Rscript", "rcode.r"]
