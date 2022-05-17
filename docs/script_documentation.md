# Export Script Documentation

## About this script

This script is created to be able to export API Proxies and sharedflows from Apigee more easily. This script is using the 'Management API' of Apigee to extract everything that is needed to recreate a proxy on another instance of Apigee. Not only will the files be exported from Apigee, they will be placed in the correct directory structure used on GitLab. After everything is exported, you will be able to let the script automatically push the files to the repository you are running the script in.

## Pre Requirements

Before you can run this python script you need to make sure you have installed Python 3.x or higher (script is created in Python 3.10) and the following packages:

        requests (pip3 install requests)
        python-dotenv (pip3 install python-dotenv)

Because we are using the 'Management API' of Apigee, you will need to authenticate using Basic Authentication. Therefor you need to create a `.env` file in the same directory as this python script, the content of the `.env` file should be:

        CLIENT_ID=<cliend_id>
        CLIENT_SECRET=<client_secret>

## How to use this script

1) First of all you need to put the script in the local repository corresponding to the repository you want to push the Apigee files to.
2) Navigate to the location of the script
3) Run the script

**On Windows:**
Open the commandline and enter `export_from_apigee.py` or dubble click on the `export_from_apigee.py` file.

**On Linux / MacOS:**
Open the commandline and enter `python3 export_from_apigee.py`

