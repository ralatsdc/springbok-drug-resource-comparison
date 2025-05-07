import json

import gget

gene_symbol = "KCNK3"
gene_id = "ENSG00000171303"

results = {}
results["target"] = {}
results["target"]["id"] = gene_id
results["target"]["symbol"] = gene_symbol
results["target"]["diseases"] = gget.opentargets(gene_id, resource="diseases", json=True)
results["target"]["drugs"] = gget.opentargets(gene_id, resource="drugs", json=True)

with open(f"{gene_symbol}_gget.json", "w") as fp:
    json.dump(results, fp, indent=4)
