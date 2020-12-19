docker container kill test-connector
docker container rm test-connector
docker build -t test-connector .
docker run --rm  \
           --name connector \
           --net=host \
           -v $(pwd)/../../../:/pybgl \
           -it test-connector