FROM openjdk:8-jdk-alpine
COPY target/service_registry-0.0.1-SNAPSHOT.jar service_registry-0.0.1-SNAPSHOT.jar
EXPOSE 8761
RUN apk --no-cache add curl
ENTRYPOINT ["java","-jar","/service_registry-0.0.1-SNAPSHOT.jar"]