docker build -t shmuelblau/publisher:1 services/Publisher/.
docker push shmuelblau/publisher:1  

docker build -t shmuelblau/subscriber:1 services/Subscriber/.
docker push shmuelblau/subscriber:1  

docker compose up
