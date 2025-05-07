import json
import requests

gene_symbol = "KCNK3"
gene_id = "ENSG00000171303"

# See: https://api.platform.opentargets.org/api/v4/graphql/browser
query_string = """
query target($ensemblId: String!) {
  target(ensemblId: $ensemblId){
    id
    approvedSymbol
    approvedName
    transcriptIds
    associatedDiseases {
      rows {
        disease {
          id
          name
          description
          dbXRefs
        }
        score
      }
    }
    proteinIds {
      id
      source
    }
    knownDrugs {
      rows {
        drugId
        prefName
        drugType
        targetClass
        mechanismOfAction
        drug {
          description
          synonyms
          tradeNames
          isApproved
        }
        diseaseId
        disease {
          name
          description
          dbXRefs
        }
        phase
        status
        ctIds
      }
    }
  }
}
"""

base_url = "https://api.platform.opentargets.org/api/v4/graphql"
variables = {"ensemblId": gene_id}
response = requests.post(base_url, json={"query": query_string, "variables": variables})
results = json.loads(response.text)["data"]

with open("KCNK3_open_targets.json", "w") as fp:
    json.dump(results, fp, indent=4)
