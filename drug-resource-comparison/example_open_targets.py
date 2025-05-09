#!/usr/bin/env python
"""Provides an example use of the Open Targets GraphQL API to obtain
proteins, drugs, and diseases given a gene id."""
import json
from pathlib import Path
import requests

gene_symbol = "KCNK3"
gene_id = "ENSG00000171303"

results_path = Path(f"../results/{gene_symbol}_open_targets.json")
if not results_path.exists():

    print(f"Getting Open Targets data for {gene_symbol}")

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
        tep {
          description
          name
          therapeuticArea
          uri
        }
        pathways {
          pathwayId
          pathway
          topLevelTerm
        }
        geneOntology {
          geneProduct
          source
          aspect
          evidence
          term {
            id
            name
          }
        }
        tractability {
          label
          modality
          value
        }
        targetClass {
          id
          level
          label
        }
      }
    }
    """
    base_url = "https://api.platform.opentargets.org/api/v4/graphql"
    variables = {"ensemblId": gene_id}
    response = requests.post(base_url, json={"query": query_string, "variables": variables})
    results = json.loads(response.text)["data"]
    with open(results_path, "w") as fp:
        json.dump(results, fp, indent=4)
