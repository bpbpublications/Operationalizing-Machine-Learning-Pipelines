#Base image reference
FROM python:3.7.3

#Setting the working directory
WORKDIR /usr/src/app

#Copy all the files from current folder into working directory
COPY . .

#Running the installation command
RUN pip3 install -r requirement.txt

#Command to run when container starts
ENTRYPOINT ["python", "Null_Value_Modul.py"]