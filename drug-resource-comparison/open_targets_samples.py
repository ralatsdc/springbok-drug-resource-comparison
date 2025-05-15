queries = {
    "associatedTargets": {
        "purpose": "Find targets associated with a specific disease or phenotype",
        "variables": {
            "efoId": "MONDO_0004979"
        },
        "query_string": """
query associatedTargets($efoId: String!) {
  disease(efoId: $efoId) {
    id
    name
    associatedTargets {
      count
      rows {
        target {
          id
          approvedSymbol
        }
        score
      }
    }
  }
}
""",
    },
    "associatedDiseases": {
        "purpose": "Find diseases and phenotypes associated with a specific target",
        "variables": {
            "ensemblId": "ENSG00000169252",
        },
        "query_string": """
query associatedDiseases($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    id
    approvedSymbol
    associatedDiseases {
      count
      rows {
        disease {
          id
          name
        }
        datasourceScores {
          id
          score
        }
      }
    }
  }
}
""",
    },
    "targetDiseaseEvidence": {
        "purpose": "Explore evidence that supports a specific target-disease association",
        "variables": {
            "efoId": "MONDO_0004979",
            "datasourceIds": ["chembl"],
            "ensemblIds": ["ENSG00000169252"],
        },
        "query_string": """
query targetDiseaseEvidence($efoId: String!, $datasourceIds: [String!]!, $ensemblIds: [String!]!) {
  disease(efoId: $efoId) {
    id
    name
    evidences(datasourceIds: $datasourceIds, ensemblIds: $ensemblIds) {
      count
      rows {
        disease {
          id
          name
        }
        diseaseFromSource
        target {
          id
          approvedSymbol
        }
        mutatedSamples {
          functionalConsequence {
            id
            label
          }
          numberSamplesTested
          numberMutatedSamples
        }
        resourceScore
        significantDriverMethods
        cohortId
        cohortShortName
        cohortDescription
      }
    }
  }
}
""",
    },
    "targetAnnotation": {
        "purpose": "Find tractability and safety information for a specific target",
        "variables": {
            "ensemblId": "ENSG00000169252",
        },
        "query_string": """
query targetAnnotation($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    id
    approvedSymbol
    tractability {
      modality
      label
      value
    }
    safetyLiabilities {
      event
      eventId
      biosamples {
        cellFormat
        cellLabel
        tissueLabel
        tissueId
      }
      effects {
        dosing
        direction
      }
      studies {
        name
        type
        description
      }
      datasource
      literature
    }
  }
}
""",
    },
    "diseaseAnnotation": {
        "purpose": "Find clinical signs and symptoms for a specific disease",
        "variables": {
            "efoId": "MONDO_0004979",
        },
        "query_string": """
query diseaseAnnotation($efoId: String!) {
  disease(efoId: $efoId) {
    id
    name
    phenotypes {
      rows {
        phenotypeHPO {
          id
          name
          description
          namespace
        }
        phenotypeEFO {
          id
          name
        }
        evidence {
          aspect
          bioCuration
          diseaseFromSourceId
          diseaseFromSource
          evidenceType
          frequency
          frequencyHPO {
            name
            id
          }
          qualifierNot
          onset {
            name
            id
          }
          modifiers {
            name
            id
          }
          references
          sex
          resource
        }
      }
    }
  }
}
""",
    },
    "GWASStudiesQuery": {
        "purpose": "GWAS studies associated with a specified disease",
        "variables": {
            "diseaseIds": ["MONDO_0004979"],
        },
        "query_string": """
query GWASStudiesQuery($diseaseIds: [String!]) {
  studies(diseaseIds: $diseaseIds ) {
    count
    rows {
      id
      projectId
      traitFromSource
      publicationFirstAuthor
      publicationDate
      publicationJournal
      nSamples
      cohorts
      pubmedId
      ldPopulationStructure {
        ldPopulation
        relativeSampleSize
      }
    }
  }
}
""",
    },
    "drugApprovalWithdrawnWarningData": {
        "purpose": "Find approval status and withdrawn and black-box warning for a specific drug",
        "variables": {
            "chemblId": "CHEMBL714",
        },
        "query_string": """
query drugApprovalWithdrawnWarningData($chemblId: String!) {
  drug(chemblId: $chemblId) {
    name
    id
    isApproved
    hasBeenWithdrawn
    blackBoxWarning
    drugWarnings {
      warningType
      description
      toxicityClass
      year
      references {
        id
        source
        url
      }
    }
  }
}
""",
    },
    "QTLCredibleSetsQuery": {
        "purpose": "Credible sets from quantitative trait loci associated with molecular traits containing a specified variant",
        "variables": {
            "variantId": "1_152312600_CACTG_C",
        },
        "query_string": """
query QTLCredibleSetsQuery($variantId: String!) {
  variant(variantId: $variantId) {
    id
    qtlCredibleSets: credibleSets(
      studyTypes: [scsqtl, sceqtl, scpqtl, sctuqtl, sqtl, eqtl, pqtl, tuqtl]
    ) {
      count
      rows {
        studyLocusId
        pValueMantissa
        pValueExponent
        beta
        finemappingMethod
        confidence
        variant {
          id
          chromosome
        }
        study {
          id
          studyType
          condition
          target {
            id
            approvedSymbol
          }
          biosample {
            biosampleId
            biosampleName
          }
        }
        locus(variantIds: ["19_44908822_C_T"]) {
          rows {
            posteriorProbability
          }
        }
        locusSize: locus {
          count
        }
      }
    }
  }
}
""",
    },
    "SharedTraitStudiesQuery": {
        "purpose": "Information about a specified study",
        "variables": {
            "studyId": "gtex_exon_stomach_ensg00000143376_14_1_151693484_151693543",
        },
        "query_string": """
query SharedTraitStudiesQuery($studyId: String!) {
  studies(studyId: $studyId) {
    count
    rows {
      id
      studyType
      traitFromSource
      projectId
      diseases {
        id
        name
      }
      publicationFirstAuthor
      publicationDate
      publicationJournal
      pubmedId
      nSamples
      cohorts
      ldPopulationStructure {
        ldPopulation
        relativeSampleSize
      }
    }
  }
}
""",
    },
    "GWASColocQuery": {
        "purpose": "Colocalisation metrics for overlapping credible sets from GWAS studies",
        "variables": {
            "studyLocusId": "4fea74b7dcc65149b658a71b5c5fa0f3",
        },
        "query_string": """
query GWASColocQuery($studyLocusId: String!) {
  credibleSet(studyLocusId: $studyLocusId) {
    colocalisation(studyTypes: [gwas]) {
      count
      rows {
        otherStudyLocus {
          studyLocusId
          study {
            id
            projectId
            traitFromSource
            publicationFirstAuthor
          }
          variant {
            id
            chromosome
            position
            referenceAllele
            alternateAllele
          }
          pValueMantissa
          pValueExponent
        }
        numberColocalisingVariants
        colocalisationMethod
        h3
        h4
        clpp
        betaRatioSignAverage
      }
    }
  }
}
""",
    },
}
