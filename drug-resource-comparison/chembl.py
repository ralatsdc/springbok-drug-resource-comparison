#!/usr/bin/env python

import argparse
import json
from pathlib import Path
import time

from chembl_webresource_client.new_client import new_client

from LoaderUtilities import get_gene_name_to_ids_map, map_gene_name_to_ids


def main():
    """Provides an example use of the ChEMBL Python client library to
    obtain targets, activities, and molecules for given a gene symbol
    from ChEMBL. Also use the client library to obtain the molecule
    image for a given ChEMBL id.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the ChEMBL Python client library"
    )
    parser.add_argument(
        "--gene-symbol",
        default="ADRB2",
        help="gene symbol for which to obtain ChEMBL data (default: ADRB2)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="force update of existing files",
    )
    args = parser.parse_args()

    gene_symbol = args.gene_symbol
    if gene_symbol == "ADRB2":
        gene_id = "ENSG00000169252"

    else:
        gnm2ids = get_gene_name_to_ids_map()
        gene_id = map_gene_name_to_ids(gene_symbol, gnm2ids)

    results_path = Path(f"../results/{gene_symbol}-chembl.json")
    if not results_path.exists() or args.force:

        results = {}
        results["gene_symbol"] = gene_symbol
        results["gene_id"] = gene_id

        # == target

        start_time = time.time()
        print(f"Getting ChEMBL target data for {gene_symbol}")

        only = ["organism", "target_chembl_id"]
        target = new_client.target
        target_results = target.filter(
            target_synonym__icontains=gene_symbol, organism__exact="Homo sapiens"
        ).only(only)[0]
        results["target"] = target_results

        # == activity

        print(f"Getting ChEMBL activity data for {gene_symbol}")

        activity = new_client.activity
        activity_results = activity.filter(
            target_chembl_id=target_results["target_chembl_id"]
        )  # .filter(standard_type="IC50")
        results["activity"] = list(activity_results)

        # == molecule

        print(f"Getting ChEMBL molecule data for {gene_symbol}")

        molecule = new_client.molecule
        molecule_chembl_ids = [a_r["molecule_chembl_id"] for a_r in activity_results]
        molecule_results = molecule.filter(
            molecule_chembl_id__in=molecule_chembl_ids, max_phase=4
        )
        results["molecule"] = list(molecule_results)

        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

        stop_time = time.time()
        print(
            f"Got ChEMBL target data for {gene_symbol} in {stop_time - start_time} seconds"
        )

    # == image
    drug_id = "CHEMBL714"
    drug_name = "ALBUTEROL"
    image_path = Path(f"../results/{drug_name}-chembl.svg")
    if not image_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting ChEMBL SVG for {drug_name}")

        image = new_client.image
        image.set_format("svg")
        with open(image_path, "w") as fp:
            fp.write(image.get(drug_id))

        stop_time = time.time()
        print(f"Got ChEMBL SVG for {drug_name} in {stop_time - start_time} seconds")


if __name__ == "__main__":
    main()
