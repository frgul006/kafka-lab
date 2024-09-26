FROM node:14

WORKDIR /app

COPY package.json ./
RUN npm install

COPY consumer.js ./

CMD ["node", "consumer.js"]