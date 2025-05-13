#!/usr/bin/env python

import argparse
import base64
import json
from pathlib import Path
import shutil
import time

import pandas as pd
import requests


def main():
    """Provides an example use of the NCATS API to obtain GSRS and
    Stitcher data given a compound id. Also copies the data downloaded
    from Figshare, and base64 decodes the conditions field.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the NCATS Inxight API"
    )
    parser.add_argument(
        "--compound-name",
        default="ALBUTEROL",
        help="compoundname for which to obtain NCATS Inxight data (default: ALBUTEROL)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="force update of existing files",
    )
    args = parser.parse_args()

    compound_name = args.compound_name.upper()
    if compound_name == "ALBUTEROL":
        compound_unii = "QF8SVZ843E"

    else:
        drugs = pd.read_csv("../data/frdb/frdb-drugs.tsv")
        selected_drugs = drugs[drugs["compound_name"].str.contains(f"^{compound_name}")]
        if selected_drugs.shape[0] == 0:
            print(f"Found {selected_drugs.shape[0]} matching compounds")
            return
        elif selected_drugs.shape[0] > 1:
            print(
                f"Found {selected_drugs.shape[0]} matching compounds, using first:{selected_drugs.iloc[0]}"
            )
        compound_unii = selected_drugs.iloc[0, 2]

    gsrs_path = Path(f"../results/{compound_name}-ncats-gsrs.json")
    if not gsrs_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting NCATS GSRS data for {compound_name}")

        gsrs_url = (
            f"https://drugs.ncats.io/api/v1/substances({compound_unii})?view=full"
        )
        gsrs_response = requests.get(gsrs_url)

        with open(gsrs_path, "w") as fp:
            json.dump(json.loads(gsrs_response.text), fp, indent=4)

        stop_time = time.time()
        print(
            f"Got NCATS GSRS data for {compound_name} in {stop_time - start_time} seconds"
        )

    stitcher_path = Path(f"../results/{compound_name}-ncats-stitcher.json")
    if not stitcher_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting NCATS Stitcher data for {compound_name}")

        stitcher_url = f"https://drugs.ncats.io/api/v1/substances({compound_unii})/@additional?view=full"
        stitcher_response = requests.get(stitcher_url)

        with open(stitcher_path, "w") as fp:
            json.dump(json.loads(stitcher_response.text), fp, indent=4)

        stop_time = time.time()
        print(
            f"Got NCATS Stitcher data for {compound_name} in {stop_time - start_time} seconds"
        )

    figshare_path = Path(f"../data/stitcher_json_files/{compound_unii}.json")
    shutil.copy(figshare_path, Path(f"../results/{compound_name}-ncats-figshare.json"))
    with open(figshare_path, "r") as fp:

        print(f"Copying NCATS Figshare data for {compound_name}")

        stitcher_json = json.load(fp)

    conditions_path = Path(f"../results/{compound_name}-ncats-conditions.json")
    if not conditions_path.exists() or args.force:

        start_time = time.time()
        print(f"Decoding NCATS Figshare conditions field for {compound_name}")

        encoded_string = stitcher_json["sgroup"]["properties"]["conditions"][0]["value"]
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        with open(conditions_path, "w") as fp:
            json.dump(json.loads(decoded_string), fp, indent=4)

        stop_time = time.time()
        print(
            f"Decoded NCATS Figshare conditions field for {compound_name} in {stop_time - start_time} seconds"
        )


if __name__ == "__main__":
    main()
