# Docker Image Creation Example - Chapter 5

The files in the repository can be utilzed directly to create the docker image. Once forked or copied on local machine, the following steps needs to be performed:

1. Log on the docker hub using the CLI/Terminal using the below command (ignore this if already done):

   ```sh
    docker login 
   ```
2. Once logged in, excute the below command:
   ```sh
   docker build -t <img-name:tag> -f Dockerfile .
   ```
    >   ___img-name___ : _Any name you want to give to your image_
  __tag__ : _Tag name to the image, default is_ __latest__
   
3. The above command will create the docker image. To push it to remote repository, like docker hub, use the    below commnad 
   ```sh
    docker tag <img-name:tag> <username/img-name>
    docker push <username/img-name>
   ```
   >    ___username___ : Docker hub __userid__

__NOTE : There are other repository for storing docker images including all the cloud vendor repository.However,we will use docker hub only in this book__

## Running the Container
We have created the docker image and pushed it to docker hub. To run the image from anywhere, the below steps needs to excuted:
1. Pull the image using below command
   ```sh
    docker pull <username/img-name:tag>
   ```
    In this particular case use the image name and tag used while creating above. 
2. Once the image is downloaded, use the below command to run it:
   ```sh
    docker run -v $(pwd):/usr/src/app <username/img-name:tag> --filename $CSV_FILE
   ```
   > The -v is used to mount a local directory as working directory which is __"/usr/src/app"__, inside the docker container. This way container can read the file from the machine where it is running and write it back, CSV_FILE is the file to be read and should be present in the current working directory. For more reference on docker run options, refer below link:
   https://docs.docker.com/engine/reference/commandline/run/









