# Overview

Here is the repository that contains all materials for the ML systems attached to the VoX Wallet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

- Download Python 3.6

In each folder where coding is required there should be a requirements file present.

```
pip install -r requirements.txt
```

It is recommended that virtual environments are used when practising the code in the examples. This avoids complication in installing unneeded dependencies.

```
python3 -m venv myenv

source myenv/bin/activate
```

## AWS Framework

Below shows a technical diagram of what the operational network will look like when deployed

![ML Framework](ML-Framework.jpg)

## Development

Provides the material for all development of the core Machine Learning systems underlying the service. The folder is sub-divided into the seperate development stages of the service. They include help files or cheat sheets to benefit the developer and without needed resarch.

### Data Collection

A Python library extension of Web3 is used to collect the data from the blockchain. This will both be saved and posted into AWS for the machine learning process. A folder in development is dedicated to coding the collection and storage.

### Machine Learning Techniques

Files containing the different machine learning techniques that are tested against each other. Provides the samples that can be used once data is highly available.

### CLI Commands

Provides a list of useful CLI commands needed for development.

## Built With

* [AWS](https://aws.amazon.com/) - The cloud interface used
* [Serverless](https://serverless.com/) - Provided by AWS Lambda
* [Python](https://www.python.org/) - Language used for machine learning code
* [Jupyter](https://jupyter.org/) - Software used for presentable documentation

## Authors

* **Sam Peek** - *Creator* - [supsam89](https://github.com/supsam89)