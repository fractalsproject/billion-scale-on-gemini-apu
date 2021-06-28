# T3 Track

## Table Of Contents

- [Introduction](#introduction)  
- [For Participants](#for_participants) 
  - [Getting Started](#getting_started) 
  - [Developing Your Algorithm](#developing_your_algorithm) 
  - [How To Get Help](#how_to_get_help)
- [For Organizers](#for_organizers)  
  - [Evaluating Participant Algorithms](#evaluating_participant_algorithms)
   
## Introduction

The T1 and T2 tracks of the competition restrict the evaluation of algorithms to standard Azure CPU servers with 64GB of RAM and 2TB of SSD.  The only restriction in the T3 track is that the evaluation machine must be a 4U chassis or smaller.  Participants can enter any commercially available hardware ( including any commercially available add-on PCIe boards ).  T3 will maintain three leaderboards:
* One based on the typical ANN performances metrics recall-vs-throughput
* One based on power consumption
* One based on hardware cost

Participants must submit their algorithm via a pull request.  Participants are not required to submit proprietary source code such as software drivers or firmware.

Organizers will evaluate the participant's algorithm and hardware via one of these options:
* Participants send their hardware to the organizers at the participant's expense.
* Participants give organizers remote access to the hardware.
* Participants run the evaluation benchmarks on their own, and send the results to the organizers.

## For_Participants

### Requirements

You will need the following installed on your machine:
* Docker ( we tested with Docker version 19.03.15, build 99e3ed8919 )
* Python ( we tested with Anaconda's python distribution version 3.6 )

### Getting_Started

This section will present a small tutorial about how to use this framework and several of the key scripts you will use throughout the development of your algorithm and eventual submission.

First, clone this repository and cd into the project directory:
```
git clone <REPO_URL>
```
Install the python package requirements:
```
pip install -r requirements.txt
```
Build an example T3 image from its location in the *t3/* directory:
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

### Developing_Your_Algorithm

First, please create a short name for your team without spaces or special characters.  This name will be used throughout the competition to identify your submission later.

Create a custom branch off main in the project repository:
```
git checkout -b [your_team_name]
```
In the *t3/* directory, create a directory using that name.
```
mkdir t3/[your_team_name]
```
Develop and add your Docker build file into that directory.
* During evaluation, this docker image will be run and your algorithm (covered next) will run inside the container that is instantiated.
* See the following Docker file example.
* Make sure you use the following command to build the docker image in the top-level directory of the repository:
```
python install.py --dockerfile [path_to_dockerfile]
```
Develop and add your algorithm to the *benchmarks/algorithms* directory.
* You will need to subclass from the BigAnn class in benchmarks/algorithms/base.py and implement the functions of that parent class.
* See the follow example.
* As you develop and test your algorithm, you will likley need to test on smaller datasets.  This framework provides a way to create datasets of various sizes.  For example, to create a dataset with 10000 20-dimensional random floating point vectors, run:
```
python create_dataset.py --dataset random-xs
```
* To see a complete list of datasets, run the following:
```
python create_dataset.py --help
```
When you are ready to test on the competition datasets, use the create_dataset.py script as follows:
```
python create_dataset.py --dataset [sift-1B|bigann-1B|text2image-1B|msturing-1B|msspacev-1B|ssnpp-1B]
```
To benchmark your algorithm, first create an algorithm configuration yaml in your teams directory called *algos.yaml.*  This file contains the index build parameters and query parameters that will get passed to your algorithm at run-time.  Please look at this example.

Now you can benchmark your algorithm using the run.py script:
```
python run.py --definitions t3/[your_team_name]/algos.yaml
```
### Submitting_Your_Algorithm

A submission is composed of the following:
* 1 index binary file 
* 1 *algos.yaml* with only 1 set of build parameters and at most 10 sets of query parameters ( placed in the *t3/[your_team_name]/* directory. )
* Your algorithm's python class ( in the *benchmark/algorithms/* directory. )
* Your Docker build file ( in the *t3/[your_team_name]/* directory. )

All but the binary index file can be submitted with a pull request of your custom branch.

We will provide you with an upload area for your binary index file during the competition.

Additional information may be required:
* To qualify for the cost track, please include evidence of the MSRP of your entire system.  Place this evidence in the *t3/[your_team_name]/* directory.
* If all of the source code cannot be included in your pull request, please provide an explanation of what the non-open-source part of the software does (host drivers, firmware, etc.)

### How_To_Get_Help

## For_Organizers

### Evaluating_Participant_Algorithms


