- Building OSB environment on #Docker to test monitoring
  based on [LinkedIn Article](https://www.linkedin.com/pulse/running-development-oracle-osbsoa-suite-domain-docker-rodrigo?articleId=6669229357975789568)
	- Build OSB Image
	  ```
	  # build jdk base image
	  git clone https://github.com/oracle/docker-images
	  cd docker-images/OracleJava/8/
	  mv /root/prom/OracleOSB/jdk-8u311-linux-x64.tar.gz .
	  sed -i 's/server-jre-8u311-linux-x64.tar.gz/jdk-8u311-linux-x64.tar.gz/g' Dockerfile*
	  sed -i 's/JAVA_SHA256.*//g' Dockerfile*
	  	  
	  docker build -t oracle/serverjre:8 .
	  	  
	  # build the SOA image
	  git clone https://github.com/damasiormoura/soasuitequickstart_docker_image.git
	  cd soasuitequickstart_docker_image/dockerfiles/12.2.1.4
	  mv /root/prom/OracleOSB/fmw_12.2.1.4.0_soa_quickstart* install/
	  sed -i 's@store/oracle/serverjre:1.8.0_241-b07@oracle/serverjre:8@g' Dockerfile
	  	  
	  docker build -t soaquickstart:12.2.1.4 .
	  ```
	- Build DB image
	  ```
	  git clone https://github.com/oracle/docker-images.git
	  cd docker-images/OracleDatabase/SingleInstance/dockerfiles/12.2.0.1/
	  docker build --build-arg DB_EDITION=ee -t oracle/database:12.2.0.1-ee .
	  docker run -d -it --name devdomain-db -p 1521:1521 oracle/database:12.2.0.1-ee
	  docker logs -f devdomain-db
	  docker ps
	  docker exec -ti devdomain-db ./setPassword.sh dbuser123
	  ```
	- #+BEGIN_TIP
	  use below command to delete all temporary docker images to free up space
	  ```
	  podman rmi $(podman images | grep '^<none>' | awk '{print $3}')
	  ```
	  #+END_TIP
	- Run RCU
	  ```
	  xhost +
	  docker run -it --rm soaquickstart:12.2.1.4 oracle_common/bin/rcu -silent -createRepository -databaseType ORACLE -connectString devdomain-db:1521:ORCLPDB1 -dbUser sys -dbRole SYSDBA -schemaPrefix poc -useSamePasswordForAllSchemaUsers true -component IAU -component IAU_APPEND -component IAU_VIEWER -component OPSS -component STB -component MDS -f < password.txt
	  ```