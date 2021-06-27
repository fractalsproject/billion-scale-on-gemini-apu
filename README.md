# T3 Track: Table of Contents  
[Introduction](#introduction)  
[For Participants](#for_participants)  
[For Organizers](#for_organizers)  
   
<a name="introduction"/>
## Introduction

<a name="for_participants"/>
## For Participants

### Requirements

You will need the following installed on your machine:
* Docker ( we tested with Docker version 19.03.15, build 99e3ed8919 )
* Python ( we tested with Anaconda's python distribution version 3.6 )

### Getting Started

Clone this repository and cd into the project directory:
```
git clone <REPO_URL>
```
Install the python package requirements:
```
pip install -r requirements.txt
```
Build an example T3 image from its location in the './t3' directory:
```
python install.py --dockerfile t3/faiss_cpu/Dockerfile
```
Create a sample dataset:
```
python create_dataset.py --dataset random-s
```
Run an evaluation using the matching algos.yaml definition file:
```
python run.py --definitions t3/faiss_cpu/algos.yaml
```
Analyze the results:
```
python plot.py 
```

### Developing Your Algorithm

First, please create a short name for your team without spaces or special characters.  This name will be used throughout the competition to identify your submission later.

Create a custom branch off main in the project repository:
```
git checkout -b [your_team_name]
```
In the '.t3/' directory, create a directory using that name.
```
mkdir t3/[your_team_name]
```
Develop and add your Docker build file into that directory.
* During evaluation, this docker image will be run and your algorithm (covered next) will run inside the container that is instantiated.
* Make sure you use the following command to build the docker image:
```
python install.py --dockerfile [path_to_dockerfile]
```
Develop and add your algorithm to the benchmarks/algorithms directory.
* You will need to subclass from the BigAnn class in benchmarks/algorithms/base.py and implement the functions of that parent class.
* See the examples benchmarks/algorithms/faiss_inmem.py or benchmarks/algorithms/diskann.py
* As you develop and test your algorithm, you will likley need to test on smaller datasets.  This framework provides a way to create datasets of various sizes.  For example, to create a dataset with 10000 20-dimensional random floating point vectors, run:
```
python create_dataset.py --dataset random-xs
```
When you are ready to test on the competition datasets, use the create_dataset.py script as follows:
```
python create_dataset.py --dataset [sift-1B|bigann-1B|text2image-1B|msturing-1B|msspacev-1B|ssnpp-1B]
```
To benchmark your algorithm, first create an algorithm configuration yaml in your teams directory called *algos.yaml.*  This file contains the index build parameters and query parameters that will get passed to your algorithm at run-time.  Please look at this example.

Now you can benchmark your algorithm using the run.py script:
```
python run.py --definitions t2/[your_team_name]/algos.yaml
```
### Submitting Your Algorithm

A submission is composed of the following:
* 1 index binary file 
* 1 *./t3/[your_team_name]/algos.yaml* with only 1 set of build parameters and at most 10 sets of query parameters
* Your algorithm's python class ( in the *./benchmark/algorithms/* directory. )
* Your Docker build file ( in the *./t3/[your_team_name]/* directory. )

All but the binary index file can be submitted with a pull request of your custom branch.

We will provide you with an upload area for your binary index file during the competition.

Additional information may be required:
* To qualify for the cost track, please include evidence of the MSRP of your entire system.  Place this evidence in the *./t3/[your_team_name]* directory.
* If all of the source code cannot be included in your pull request, please provide an explanation of what the non-open-source part of the software does.

<a name="for_organizers"/>
## For Organizers

### Evaluating A Participant Algorithm


