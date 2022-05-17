import os
import shutil
import requests
from dotenv import load_dotenv
from zipfile import ZipFile
import subprocess

load_dotenv()


def download_proxy(org, proxy, rev):
    URL = f"https://api.enterprise.apigee.com/v1/organizations/{org}/apis/{proxy}/revisions/{rev}?format=bundle"

    response = requests.get(URL, headers={'Content-Type': 'application/zip'}, auth=(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")))

    with open(f'{proxy}.zip', 'wb') as f:
        f.write(response.content)


def extract_shared_flows(org, sharedflow_name, rev):
    URL = f"https://api.enterprise.apigee.com/v1/organizations/{org}/sharedflows/{sharedflow_name}/revisions/{rev}?format=bundle"

    response = requests.get(URL, headers={'Content-Type': 'application/zip'}, auth=(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")))

    with open(f'{sharedflow_name}.zip', 'wb') as f:
        f.write(response.content)


def unzip_folder(folder_name, loc=None):
    with ZipFile(folder_name, 'r') as zipObj:
        if loc != None:
            zipObj.extractall(loc)
        else:
            zipObj.extractall()
    os.remove(folder_name)


if __name__ == "__main__":
    org_name = input("Organization you want to extract from: ")
    proxy_name = input("Proxy you want to extract: ")
    download_sharedflows = input(
        "Sharedflows you want to download seperate by ';' ").split(';')

    proxy_revisions = requests.get(f"https://api.enterprise.apigee.com/v1/organizations/{org_name}/apis/{proxy_name}/revisions", auth=(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")))
    latest_proxy_rev = list(proxy_revisions.json())[-1]

    download_proxy(org_name, proxy_name, latest_proxy_rev)
    print(f"Download of proxy '{proxy_name}' complete...")

    unzip_folder(f"{proxy_name}.zip")
    print(f"Unzip of folder '{proxy_name}.zip' complete...")

    if os.path.exists("./sharedflows"):
        shutil.rmtree("./sharedflows")
    os.mkdir("./sharedflows")

    for flow in download_sharedflows:
        flow_revisions = requests.get(f"https://api.enterprise.apigee.com/v1/organizations/{org_name}/sharedflows/{flow}/revisions", auth=(
            os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")))
        latest_flow_rev = list(flow_revisions.json())[-1]

        extract_shared_flows(org_name, flow, latest_flow_rev)
        print(f"Download of shared flow '{flow}' complete...")

        unzip_folder(f"{flow}.zip", f"./sharedflows/{flow}")
        print(f"Unzip of folder '{flow}.zip' complete...")

    x = input("\nDone.... \nDo you want to push to GitLab? (y/n) ")

    if(x.lower() == "y"):
        commit_msg = input("Enter a message that will be added by the push: ")
        subprocess.run("git add .")
        subprocess.run(f'git commit -m "{commit_msg}"')
        subprocess.run("git push")
        y = input("Files successfully pushed to GitLab, Press Enter to exit...")

    else:
        y = input("New files not pushed to GitLab, press Enter to exit...")
