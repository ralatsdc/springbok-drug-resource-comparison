#!/usr/bin/env python

import argparse
import json
from pathlib import Path

import gget


def main():
    """Provides an example use of the gget opentargets command to
    obtain the diseases and drugs resources for a given gene id.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the gget opentargets command"
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="force update of existing files",
    )
    args = parser.parse_args()

    # gene_symbol = "KCNK3"
    # gene_id = "ENSG00000171303"

    gene_symbol = "ADRB2"
    gene_id = "ENSG00000169252"

    results_path = Path(f"../results/{gene_symbol}-gget.json")
    if not results_path.exists() or args.force:

        print(f"Getting gget data for {gene_symbol}")

        results = {}
        results["target"] = {}
        results["target"]["id"] = gene_id
        results["target"]["symbol"] = gene_symbol
        results["target"]["diseases"] = gget.opentargets(
            gene_id, resource="diseases", json=True
        )
        results["target"]["drugs"] = gget.opentargets(
            gene_id, resource="drugs", json=True
        )
        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)


if __name__ == "__main__":
    main()
