#!/usr/bin/env python
"""Provides an example use of the NCATS API to obtain GSRS and Sticher
data given a compound id. Also copies the data downloaded from
Figshare, and base64 decodes the conditions field."""
import base64
import json
from pathlib import Path
import shutil

import requests

compound_id = 1408
compound_name = "OLMESARTAN"
compound_unii = "8W1IQP3U10"

gsrs_path = Path(f"../results/{compound_name}-ncats-gsrs.json")
if not gsrs_path.exists():

    print(f"Getting NCATS GSRS data for {compound_name}")

    gsrs_url = f"https://drugs.ncats.io/api/v1/substances({compound_unii})?view=full"
    gsrs_response = requests.get(gsrs_url)
    with open(gsrs_path, "w") as fp:
        json.dump(json.loads(gsrs_response.text), fp, indent=4)

stitcher_path = Path(f"../results/{compound_name}-ncats-stitcher.json")
if not stitcher_path.exists():

    print(f"Getting NCATS Stitcher data for {compound_name}")

    stitcher_url = f"https://drugs.ncats.io/api/v1/substances({compound_unii})/@additional?view=full"
    stitcher_response = requests.get(stitcher_url)
    with open(stitcher_path, "w") as fp:
        json.dump(json.loads(stitcher_response.text), fp, indent=4)

figshare_path = Path(f"../data/stitcher_json_files/{compound_unii}.json")
shutil.copy(figshare_path, Path(f"../results/{compound_name}-ncats-figshare.json"))
with open(figshare_path, "r") as fp:

    print(f"Copying NCATS Figshare data for {compound_name}")

    stitcher_json = json.load(fp)

conditions_path = Path(f"../results/{compound_name}-ncats-conditions.json")
if not conditions_path.exists():

    print(f"Decoding NCATS Figshare conditions field for {compound_name}")

    encoded_string = stitcher_json["sgroup"]["properties"]["conditions"][0]["value"]
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    with open(conditions_path, "w") as fp:
        json.dump(json.loads(decoded_string), fp, indent=4)
