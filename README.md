# CMPE 273 – Week 1 Lab 1: First Distributed System

## Run Service A Only (FROM PROJECT ROOT)
```bash
docker build -t cmpe273-service-a ./services/service-a
docker run --rm -p 8080:8080 --name service-a cmpe273-service-a
```
## To Stop Service A
```bash
docker stop service-a
```

## Run Service B Only (FROM PROJECT ROOT)
```bash
docker build -t cmpe273-service-b ./services/service-b
docker run --rm -p 8081:8081 --name service-b cmpe273-service-b
```
## To Stop Service B
```bash
docker stop service-b
```

## Pasted Success Output


## Screenshot of Failure


## What makes this distributed?
According to Professor Ranjan's Week 1 Lecture notes, we can call a system "distributed" when it satisfies 4 characteristics. The first characteristic is that components run in different processes. The second characteristic is that components in the system communicate over a network. The third characteristic is that different components can fail independently. And the last characteristic that makes a system distributed is that different components have no shared clock or memory. Lab 1 satisfies all of these characteristics. Service A and Service B run different processes independent of each other. Service B communicates with Service A over a network. Service A can fail without causing Service B to fail as well (see screenshots above). Lastly, Service A and Service B are separate services that can communicate with each other to obtain information through network requests, but they have no shared memory or shared clock. 
