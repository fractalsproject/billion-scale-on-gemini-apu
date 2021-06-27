# T3 Track: Table of Contents  
[Introduction](#introduction)  
[For Participants](#for_participants)  
[For Organizers](#for_organizers)  
   
<a name="introduction"/>
## Introduction

<a name="for_participants"/>
## For Participants

### Requirements

* You will need the following installed on your machine:
* * Docker ( we tested with Docker version 19.03.15, build 99e3ed8919 )
* * Python ( we tested with Anaconda's 3.6 )

### Getting Started

* Clone this repository and cd into the project directory:
'''
git clone <REPO_URL>
'''
* Install the python package requirements:
> pip install -r requirements.txt
* Build an example T3 image from its location in the './t3' directory:
> python install.py --dockerfile t3/faiss_cpu/Dockerfile
* Create a sample dataset:
> python create_dataset.py --dataset random-s
* Run an evaluation using the matching algos.yaml definition file:
> python run.py --definitions t3/faiss_cpu/algos.yaml
* Analyze the results:
>python plot.py 

### Developing Your Algorithm

* Choose a short name for your team without spaces or special characters.  
* In the '.t3/' directory, create a directory using that name.
* Develop and add your Docker build file into that directory.
* * During evaluation, this docker image will be run and your algorithm (covered next) will run inside the container that is instantiated.
* * Make sure you use the following command to build the image:
> python install.py --dockerfile [path_to_dockerfile]
* Develop and add your algorithm to the benchmarks/algorithms directory.
* * You will need to subclass from the BigAnn class in benchmarks/algorithms/base.py and implement the functions of that parent class.
* * See the examples benchmarks/algorithms/faiss_inmem.py or benchmarks/algorithms/diskann.py
* * As you develop and test your algorithm, you will likley need to test on smaller datasets.  The framework provides a way to create atasets of various sizes.  For example, to create a dataset with 10000 20-dimensional random floating point vectors, run:
> python create_dataset.py --dataset random-xs
* When you are ready to test on the competition datasets, use the create_dataset.py script as follows:
> python create_dataset.py --dataset [sift-1B|bigann-1B|text2image-1B|msturing-1B|msspacev-1B|ssnpp-1B]

### Submitting Your Algorithm


<a name="for_organizers"/>
## For Organizers

### Evaluating A Participant Algorithm


