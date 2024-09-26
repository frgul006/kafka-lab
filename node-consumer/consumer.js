const { Kafka } = require("kafkajs");
const redis = require("redis");

const kafka = new Kafka({
  clientId: "node-consumer",
  brokers: [process.env.KAFKA_BOOTSTRAP_SERVERS || "kafka:9092"],
});

const topic = "bar-topic";
const redisHost = process.env.REDIS_HOST || "redis";
const redisClient = redis.createClient({ host: redisHost });

const consumer = kafka.consumer({ groupId: "node-consumer-group" });

const run = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic, fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ message }) => {
      const msg = message.value.toString();
      console.log(`Consumed message: ${msg}`);
      redisClient.incr("bar-counter", (err, reply) => {
        if (err) console.error(err);
        else console.log(`Updated Redis counter: ${reply}`);
      });
    },
  });
};

run().catch(console.error);
