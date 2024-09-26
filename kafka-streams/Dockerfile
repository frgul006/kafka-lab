FROM gradle:6.8.3-jdk11 as builder

WORKDIR /home/gradle/src
COPY . /home/gradle/src
RUN gradle installDist

FROM openjdk:11-jre-slim

WORKDIR /app
COPY --from=builder /home/gradle/src/build/install/kafka-streams /app/

CMD ["/app/bin/kafka-streams"]