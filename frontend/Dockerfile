FROM node:22-alpine
WORKDIR /frontend
COPY ./package.json /frontend
COPY ./package-lock.json /frontend
RUN npm ci
COPY . /frontend
EXPOSE 3000
CMD ["npm", "start"]

