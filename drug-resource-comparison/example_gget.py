#!/usr/bin/env python
"""Provides an example use of the gget opentargets command to obtain
the diseases and drugs resources for a given gene id.
"""
import json
from pathlib import Path

import gget

gene_symbol = "KCNK3"
gene_id = "ENSG00000171303"

results_path = Path(f"../results/{gene_symbol}_gget.json")
if not results_path.exists():

    print(f"Getting gget data for {gene_symbol}")

    results = {}
    results["target"] = {}
    results["target"]["id"] = gene_id
    results["target"]["symbol"] = gene_symbol
    results["target"]["diseases"] = gget.opentargets(gene_id, resource="diseases", json=True)
    results["target"]["drugs"] = gget.opentargets(gene_id, resource="drugs", json=True)
    with open(results_path, "w") as fp:
        json.dump(results, fp, indent=4)
