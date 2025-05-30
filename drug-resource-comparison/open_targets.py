#!/usr/bin/env python

import argparse
import json
from pathlib import Path
import time

import requests

from LoaderUtilities import get_gene_name_to_ids_map, map_gene_name_to_ids
from open_targets_examples import example_queries
from open_targets_gget import gget_queries

BASE_URL = "https://api.platform.opentargets.org/api/v4/graphql"


def main():
    """Provides an example use of the Open Targets GraphQL API to
    obtain proteins, drugs, and diseases given a gene id.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the Open Targets GraphQL API"
    )
    parser.add_argument(
        "--gene-symbol",
        default="ADRB2",
        help="gene symbol for which to obtain Open Targets data (default: ADRB2)",
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
        gene_id = map_gene_name_to_ids(gene_symbol, gnm2ids)

    disease_id = "MONDO_0004979"
    disease_name = "asthma"

    drug_id = "CHEMBL714"
    drug_name = "ALBUTEROL"

    # == target

    results_path = Path(f"../results/{gene_symbol}-open-targets-target.json")
    if not results_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting Open Targets target data for {gene_symbol}")

        # See: https://api.platform.opentargets.org/api/v4/graphql/browser
        query_string = """
        query target($ensemblId: String!) {
          target(ensemblId: $ensemblId) {
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
        variables = {"ensemblId": gene_id}
        response = requests.post(
            BASE_URL, json={"query": query_string, "variables": variables}
        )
        results = json.loads(response.text)["data"]
        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

        stop_time = time.time()
        print(
            f"Got Open Targets target data for {gene_symbol} in {stop_time - start_time} seconds"
        )

    # == disease

    results_path = Path(f"../results/{gene_symbol}-open-targets-disease.json")
    if not results_path.exists() or args.force:

        start_time = time.time()
        print(f"Getting Open Targets target disease for {disease_name}")

        # See: https://api.platform.opentargets.org/api/v4/graphql/browser
        query_string = """
        query disease($efoId: String!) {
          disease(efoId: $efoId) {
            directLocationIds
            id
            descendants
            obsoleteTerms
            description
            dbXRefs
            indirectLocationIds
            synonyms {
              relation
              terms
            }
            ancestors
            name
            therapeuticAreas {
              id
              name
            }
            parents {
              id
              name
            }
            children {
              id
              name
            }
            directLocations {
              id
              name
            }
            indirectLocations {
              id
              name
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
            isTherapeuticArea
            phenotypes {
              rows {
                phenotypeHPO {
                  id
                }
                phenotypeEFO {
                  id
                }
              }
            }
            otarProjects {
              otarCode
              status
              reference
              integratesInPPP
              projectName
            }
            knownDrugs {
              rows {
                drugId
              }
            }
            associatedTargets {
              rows {
                datatypeScores {
                  id
                }
                datasourceScores {
                  id
                }
                score
                target {
                  id
                }
              }
            }
          }
        }
        """
        variables = {"efoId": disease_id}
        response = requests.post(
            BASE_URL, json={"query": query_string, "variables": variables}
        )
        results = json.loads(response.text)["data"]
        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

        stop_time = time.time()
        print(
            f"Got Open Targets disease data for {disease_name} in {stop_time - start_time} seconds"
        )

    # == drug

    results_path = Path(f"../results/{drug_name}-open-targets-drug.json")
    if not results_path.exists() or args.force:

        start_time = time.time()
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
        variables = {"chemblId": drug_id}
        response = requests.post(
            BASE_URL, json={"query": query_string, "variables": variables}
        )
        results = json.loads(response.text)["data"]
        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

        stop_time = time.time()
        print(
            f"Got Open Targets drug data for {drug_name} in {stop_time - start_time} seconds"
        )

    # == example queries

    for name, query in example_queries.items():

        results_path = Path(f"../results/open-targets-example-{name}.json")
        if not results_path.exists() or args.force:

            start_time = time.time()
            print(f"Running Open Targets example query {name}")

            response = requests.post(
                BASE_URL,
                json={"query": query["query_string"], "variables": query["variables"]},
            )
            results = {}
            results["purpose"] = query["purpose"]
            results["variables"] = query["variables"]
            results["data"] = json.loads(response.text)["data"]
            with open(results_path, "w") as fp:
                json.dump(results, fp, indent=4)

            stop_time = time.time()
            print(
                f"Ran Open Targets example query {name} in {stop_time - start_time} seconds"
            )

    # == gget queries

    for name, query in example_queries.items():

        results_path = Path(f"../results/open-targets-gget-{name}.json")
        if not results_path.exists() or args.force:

            start_time = time.time()
            print(f"Running Open Targets gget query {name}")

            response = requests.post(
                BASE_URL,
                json={"query": query["query_string"], "variables": query["variables"]},
            )
            results = {}
            results["purpose"] = query["purpose"]
            results["variables"] = query["variables"]
            results["data"] = json.loads(response.text)["data"]
            with open(results_path, "w") as fp:
                json.dump(results, fp, indent=4)

            stop_time = time.time()
            print(
                f"Ran Open Targets gget query {name} in {stop_time - start_time} seconds"
            )


if __name__ == "__main__":
    main()
