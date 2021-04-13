# Microservices-based-App
Demonstrates basics principles of  Microservices architecture, its design patterns etc.

### Microservices Application Architecture
1. microservice 1 (Shopping Catalog) - 
		Django (Python 3.7.3, Django 3.1.7, Django REST framework 3.12.2, PyMySQL 1.0.2)
 		A somple microservice that provides REST endpoints to perfrom CRUD operations.
2. database - default Django available database (MySQL 8.0)
3. front end app - REACT
4. API Gateway - netflix zuul API Gateway is used (Spring boot based) Performs server side load balancing using Ribbon.
5. Eureka server - to handle service registry (Spring boot based)
6. Sidecar application - to handle communication among Django microservice and Eureka server (Spring boot based)
7. microservicde 0 - Depicts and intermediate microservice. In this case it simply forwards the request to microservice1 for demonstration purposes. Integrated with Ribbon load balancer to perform client side load balancing.

All the componants are dockerized and deplyed using docker compose.

![image](https://user-images.githubusercontent.com/47441406/114512353-5e7c1500-9c7c-11eb-91df-a58f65a72d8a.png)







