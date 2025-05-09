#!/usr/bin/env python
"""Provides an example use of the Open Targets GraphQL API to obtain
proteins, drugs, and diseases given a gene id."""
import json
from pathlib import Path
import requests

gene_symbol = "KCNK3"
gene_id = "ENSG00000171303"

# == target

results_path = Path(f"../results/{gene_symbol}-open-targets-target.json")
if not results_path.exists():

    print(f"Getting Open Targets target data for {gene_symbol}")

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


# == drug
        
drug_id = "CHEMBL714"
drug_name = "ALBUTEROL"

results_path = Path(f"../results/{drug_name}-open-targets-drug.json")
if not results_path.exists():

    print(f"Getting Open Targets drug data for {drug_name}")

    # See: https://api.platform.opentargets.org/api/v4/graphql/browser
    query_string = """
    query drug($chemblId: String!) {
      drug(chemblId: $chemblId) {
        id
        description
        blackBoxWarning
        yearOfFirstApproval
        maximumClinicalTrialPhase
        drugType
        crossReferences {
          reference
          source
        }
        isApproved
        synonyms
        hasBeenWithdrawn
        tradeNames
        name
        parentMolecule {
          id
        }
        childMolecules {
          id
        }
        approvedIndications
        drugWarnings {
          id
          efoIdForWarningClass
          references {
            id
            source
            url
          }
          efoTerm
          description
          country
          efoId
          warningType
          year
          toxicityClass
        }
        similarEntities {
          id
          category
          score
        }
        literatureOcurrences {
          rows {
            pmid
            pmcid
            publicationDate
            sentences {
              section
              matches {
                mappedId
                matchedLabel
                sectionStart
                sectionEnd
                startInSentence
                endInSentence
                matchedType
              }
            }
          }
        }
        mechanismsOfAction {
          rows {
            references {
              urls
              source
              ids
            }
            targetName
            actionType
            mechanismOfAction
          }
        }
        indications {
          rows {
            maxPhaseForIndication
            references {
              source
              ids
            }
            disease {
              id
            }
          }
        }
        knownDrugs {
          rows {
            drugId
          }
        }
        adverseEvents {
          rows {
            logLR
            count
            meddraCode
            name
          }
        }
        pharmacogenomics {
          isDirectTarget
          genotypeAnnotationText
          haplotypeFromSourceId
          phenotypeText
          pgxCategory
          genotypeId
          targetFromSourceId
          studyId
          literature
          variantRsId
          datatypeId
          variantFunctionalConsequenceId
          phenotypeFromSourceId
          evidenceLevel
          datasourceId
          variantId
          genotype
          haplotypeId
          variantFunctionalConsequence {
            id
            label
          }
          target {
            id
          }
          drugs {
            drugId
          }
        }
        linkedDiseases {
          rows {
            id
          }
        }
        linkedTargets {
          rows {
            id
          }
        }
      }
    }
    """
    base_url = "https://api.platform.opentargets.org/api/v4/graphql"
    variables = {"chemblId": drug_id}
    response = requests.post(base_url, json={"query": query_string, "variables": variables})
    results = json.loads(response.text)["data"]
    with open(results_path, "w") as fp:
        json.dump(results, fp, indent=4)
