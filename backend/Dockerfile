FROM node:22-alpine
WORKDIR /backend
COPY ./package.json /backend
COPY ./package-lock.json /backend
RUN npm ci
COPY . /backend
EXPOSE 5000
