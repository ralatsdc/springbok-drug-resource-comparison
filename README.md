# Drug Resource Comparison for the Cell Knowledge Network

## Motivation

The Cell Knowledge Network (Cell KN) pilot aims to create a
comprehensive cell phenotype knowledge network that integrates
knowledge about diseases and drugs to facilitate discovery of new
biomarkers and therapeutic targets. The Cell KN captures single cell
genomics data from existing data repositories, such as CELLxGENE, uses
NSForest to identify cell type-specific marker genes, and integrates
external knowledge from resources such as ChEMBL, NCATS Inxight Drugs,
and Open Targets, among others.

## Purpose

The `springbok-drug-resource-comparison` repository provides simple
Python command line utilities for fetching example data from
[ChEMBL](https://www.ebi.ac.uk/chembl/), [NCATS Inxight
Drugs](https://drugs.ncats.io/), and [Open Targets
Platform](https://platform-docs.opentargets.org/getting-started) in
order to compare how comprehensive, organized, and accessible each
resource appears.  The repository includes LaTeX source for a Beamer
presentation describing the data obtained for gene target ADRB2,
approved drug Albuterol, and disease Asthma.

## Dependencies

### Submodule

The `springbok-drug-resource-comparison` repository includes the
`cell-kn-etl-results` repository as a submodule. After cloning
`springbok-drug-resource-comparison`, initialize and update the
submodule as follows:
```
git submodule init
git submodule update
```

### Python

Python 3.13 and Poetry are required to run the command line
utilities. Install the dependencies as follows:
```
$ python3.13 -m venv .poetry
$ source .poetry/bin/activate
$ python -m pip install -r .poetry.txt
$ deactivate
$ python3.13 -m venv .venv
$ source .venv/bin/activate
$ .poetry/bin/poetry install
```

## Usage

Run the Python command line utilities to see usage as follows:
```
$ cd drug-resource-comparison
$ python chembl.py -h
$ python gget_cli.py -h
$ python ncats.py -h
$ python open_targets.py -h
```
