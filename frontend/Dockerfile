FROM node:18-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm i

EXPOSE 3000

ENTRYPOINT ["npm"]

CMD ["run", "dev"]
