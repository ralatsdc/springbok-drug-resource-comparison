#!/usr/bin/env python

import argparse
import json
from pathlib import Path
import time

import gget

from LoaderUtilities import get_gene_name_to_ids_map, map_gene_name_to_ids


def main():
    """Provides an example use of the gget opentargets command to
    obtain the diseases and drugs resources for a given gene id.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the gget opentargets command"
    )
    parser.add_argument(
        "--gene-symbol",
        default="ADRB2",
        help="gene symbol for which to obtain gget data (default: ADRB2)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="force update of existing files",
    )
    args = parser.parse_args()

    gene_symbol = args.gene_symbol.upper()
    if gene_symbol == "ADRB2":
        gene_id = "ENSG00000169252"

    else:
        gnm2ids = get_gene_name_to_ids_map()
        gene_id = map_gene_name_to_ids(gene_symbol, gnm2ids)[0]

    results_path = Path(f"../results/{gene_symbol}-gget.json")
    if not results_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting gget data for {gene_symbol}")

        results = {}
        results["target"] = {}
        results["target"]["id"] = gene_id
        results["target"]["symbol"] = gene_symbol

        # == diseases

        results["target"]["diseases"] = gget.opentargets(
            gene_id, resource="diseases", json=True
        )

        # == drugs

        results["target"]["drugs"] = gget.opentargets(
            gene_id, resource="drugs", json=True
        )

        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

        stop_time = time.time()
        print(f"Got gget data for {gene_symbol} in {stop_time - start_time} seconds")


if __name__ == "__main__":
    main()
