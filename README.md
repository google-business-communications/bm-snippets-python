# Business Messages: Python snippets

These code snippets demonstrate how to perform operations with the Business Messages API using Python.

This project contains multiple examples. Each file contains a single operation with the Business Messages API.

To run the Python scripts you need to be signed up with [Business Messages](https://developers.google.com/business-communications/business-messages/guides/set-up/register).

## Documentation

The documentation for the Business Messages API can be found [here](https://developers.google.com/business-communications/business-messages/reference/rest).

## Prerequisite

You must have the following software installed on your machine:

- [Google Cloud SDK](https://cloud.google.com/sdk/) (aka gcloud)
- [Python](https://www.python.org/downloads/)

## Before you begin

1.  [Register with Business Messages](https://developers.google.com/business-communications/business-messages/guides/set-up/register).
1.  Once registered, follow the instructions to [enable the APIs for your project](https://developers.google.com/business-communications/business-messages/guides/set-up/register#enable-api).

## Installation

### Mac/Linux

python -m venv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install -r requirements.txt

### Windows

python -m venv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install -r requirements.txt

## Supported Python Versions

Python 3.5, 3.6 and 3.7, and 3.8 are fully supported and tested.

## How to run the Python scripts?

1. Locate the file with the code snippet you want to execute.
1. Replace all the values of the variables on top of the file that are set to `EDIT_HERE`.
1. Make sure the path to your [service account key](https://developers.google.com/business-communications/business-messages/guides/quickstarts/prerequisite-setup?hl=en#create_a_service_account) is correct. The scripts use a default path as `./service_account_key.json`.
1. On your terminal, run `python file-name-to-be-executed.py`

## Learn more

To learn more about setting up Business Messages and supporting
chat from Search and Maps, see the [documentation](https://developers.google.com/business-communications/business-messages/guides).
