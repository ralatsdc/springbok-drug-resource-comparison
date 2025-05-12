#!/usr/bin/env python

import argparse
import json
from pathlib import Path

from chembl_webresource_client.new_client import new_client

from LoaderUtilities import get_gene_name_to_ids_map, map_gene_name_to_ids


def main():
    """Provides an example use of the ChEMBL Python client library to
    obtain targets, activities, and molecules for given a gene symbol
    from ChEMBL. Also use the client library to obtain the molecule
    image for a given ChEMBL id.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate use of the ChEMBL Python client library"
    )
    parser.add_argument(
        "--gene-symbol",
        default="ADRB2",
        help="gene symbol for which to obtain ChEMBL data (default: ADRB2)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="force update of existing files",
    )
    args = parser.parse_args()

    gene_symbol = args.gene_symbol
    if gene_symbol == "ADRB2":
        gene_id = "ENSG00000169252"

    else:
        gnm2ids = get_gene_name_to_ids_map()
        gene_id = map_gene_name_to_ids(gene_symbol, gnm2ids)

    results_path = Path(f"../results/{gene_symbol}-chembl.json")
    if not results_path.exists() or args.force:

        results = {}
        results["gene_symbol"] = gene_symbol
        results["gene_id"] = gene_id

        # == target

        print(f"Getting ChEMBL target data for {gene_symbol}")

        """Example data:
        {'cross_references': [],
         'organism': 'Homo sapiens',
         'pref_name': 'Potassium channel subfamily K member 3',
         'species_group_flag': False,
         'target_chembl_id': 'CHEMBL2321613',
         'target_components': [{'accession': 'O14649',
           'component_description': 'Potassium channel subfamily K member 3',
           'component_id': 7234,
           'component_type': 'PROTEIN',
           'relationship': 'SINGLE PROTEIN',
           'target_component_synonyms': [{'component_synonym': 'Acid-sensitive potassium channel protein TASK-1',
             'syn_type': 'UNIPROT'},
            {'component_synonym': 'KCNK3', 'syn_type': 'GENE_SYMBOL'},
            {'component_synonym': 'Potassium channel subfamily K member 3',
             'syn_type': 'UNIPROT'},
            {'component_synonym': 'TASK', 'syn_type': 'GENE_SYMBOL_OTHER'},
            {'component_synonym': 'TASK1', 'syn_type': 'GENE_SYMBOL_OTHER'},
            {'component_synonym': 'TWIK-related acid-sensitive K(+) channel 1',
             'syn_type': 'UNIPROT'},
            {'component_synonym': 'Two pore K(+) channel KT3.1',
             'syn_type': 'UNIPROT'},
            {'component_synonym': 'Two pore potassium channel KT3.1',
             'syn_type': 'UNIPROT'}],
           'target_component_xrefs': [{'xref_id': 'O14649',
             'xref_name': None,
             'xref_src_db': 'AlphaFoldDB'},
            {'xref_id': 'O14649', 'xref_name': None, 'xref_src_db': 'ExpressionAtlas'},
            {'xref_id': 'GO:0005886',
             'xref_name': 'plasma membrane',
             'xref_src_db': 'GoComponent'},
            {'xref_id': 'GO:0016020',
             'xref_name': 'membrane',
             'xref_src_db': 'GoComponent'},
            {'xref_id': 'GO:0045202',
             'xref_name': 'synapse',
             'xref_src_db': 'GoComponent'},
            {'xref_id': 'GO:0005216',
             'xref_name': 'monoatomic ion channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0005252',
             'xref_name': 'open rectifier potassium channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0005267',
             'xref_name': 'potassium channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0005272',
             'xref_name': 'sodium channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0005515',
             'xref_name': 'protein binding',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0015271',
             'xref_name': 'outward rectifier potassium channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0022841',
             'xref_name': 'potassium ion leak channel activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0044548',
             'xref_name': 'S100 protein binding',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0046872',
             'xref_name': 'metal ion binding',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0046982',
             'xref_name': 'protein heterodimerization activity',
             'xref_src_db': 'GoFunction'},
            {'xref_id': 'GO:0006813',
             'xref_name': 'potassium ion transport',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0006814',
             'xref_name': 'sodium ion transport',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0007268',
             'xref_name': 'chemical synaptic transmission',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0034220',
             'xref_name': 'monoatomic ion transmembrane transport',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0035725',
             'xref_name': 'sodium ion transmembrane transport',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0051481',
             'xref_name': 'negative regulation of cytosolic calcium ion concentration',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0060075',
             'xref_name': 'regulation of resting membrane potential',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0071294',
             'xref_name': 'cellular response to zinc ion',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0071456',
             'xref_name': 'cellular response to hypoxia',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0071468',
             'xref_name': 'cellular response to acidic pH',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0071805',
             'xref_name': 'potassium ion transmembrane transport',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0090102',
             'xref_name': 'cochlea development',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'GO:0099605',
             'xref_name': 'regulation of action potential firing rate',
             'xref_src_db': 'GoProcess'},
            {'xref_id': 'HGNC:6278', 'xref_name': 'KCNK3', 'xref_src_db': 'HGNC'},
            {'xref_id': 'O14649', 'xref_name': None, 'xref_src_db': 'IntAct'},
            {'xref_id': 'IPR003092',
             'xref_name': '2pore_dom_K_chnl_TASK',
             'xref_src_db': 'InterPro'},
            {'xref_id': 'IPR003280',
             'xref_name': '2pore_dom_K_chnl',
             'xref_src_db': 'InterPro'},
            {'xref_id': 'IPR005406', 'xref_name': 'KCNK3', 'xref_src_db': 'InterPro'},
            {'xref_id': 'IPR013099',
             'xref_name': 'K_chnl_dom',
             'xref_src_db': 'InterPro'},
            {'xref_id': 'PTHR11003',
             'xref_name': 'POTASSIUM CHANNEL, SUBFAMILY K',
             'xref_src_db': 'PANTHER'},
            {'xref_id': 'PTHR11003:SF138',
             'xref_name': 'POTASSIUM CHANNEL SUBFAMILY K MEMBER 3',
             'xref_src_db': 'PANTHER'},
            {'xref_id': '6RV2', 'xref_name': None, 'xref_src_db': 'PDB'},
            {'xref_id': '6RV3', 'xref_name': None, 'xref_src_db': 'PDB'},
            {'xref_id': '6RV4', 'xref_name': None, 'xref_src_db': 'PDB'},
            {'xref_id': 'PF07885', 'xref_name': 'Ion_trans_2', 'xref_src_db': 'Pfam'},
            {'xref_id': 'PA30060',
             'xref_name': 'potassium two pore domain channel subfamily K member 3',
             'xref_src_db': 'PharmGKB'},
            {'xref_id': 'O14649', 'xref_name': None, 'xref_src_db': 'Pharos'},
            {'xref_id': 'R-HSA-1299316',
             'xref_name': 'TWIK-releated acid-sensitive K+ channel (TASK)',
             'xref_src_db': 'Reactome'},
            {'xref_id': 'R-HSA-5576886',
             'xref_name': 'Phase 4 - resting membrane potential',
             'xref_src_db': 'Reactome'},
            {'xref_id': 'O14649',
             'xref_name': 'Potassium channel subfamily K member 3',
             'xref_src_db': 'UniProt'},
            {'xref_id': 'Q53SU2',
             'xref_name': 'Potassium channel subfamily K member 3',
             'xref_src_db': 'UniProt'}]}],
         'target_type': 'SINGLE PROTEIN',
         'tax_id': 9606}
        """
        only = ["organism", "target_chembl_id"]
        target = new_client.target
        target_results = target.filter(
            target_synonym__icontains=gene_symbol, organism__exact="Homo sapiens"
        ).only(only)[0]
        results["target"] = target_results

        # == activity

        print(f"Getting ChEMBL activity data for {gene_symbol}")

        """Example data:
        {'action_type': None,
         'activity_comment': None,
         'activity_id': 12662605,
         'activity_properties': [],
         'assay_chembl_id': 'CHEMBL2327429',
         'assay_description': 'Inhibition of TASK-1 (unknown origin)',
         'assay_type': 'B',
         'assay_variant_accession': None,
         'assay_variant_mutation': None,
         'bao_endpoint': 'BAO_0000190',
         'bao_format': 'BAO_0000357',
         'bao_label': 'single protein format',
         'canonical_smiles': 'CCCC(=O)C1CCN(c2ncnc3c2CN(C(=O)c2ccc(-c4ccccc4)cc2)CC3)CC1',
         'data_validity_comment': None,
         'data_validity_description': None,
         'document_chembl_id': 'CHEMBL2321869',
         'document_journal': 'J Med Chem',
         'document_year': 2013,
         'ligand_efficiency': {'bei': '13.92',
          'le': '0.25',
          'lle': '1.59',
          'sei': '9.82'},
         'molecule_chembl_id': 'CHEMBL2324344',
         'molecule_pref_name': None,
         'parent_molecule_chembl_id': 'CHEMBL2324344',
         'pchembl_value': '6.52',
         'potential_duplicate': 0,
         'qudt_units': 'http://www.openphacts.org/units/Nanomolar',
         'record_id': 1850391,
         'relation': '=',
         'src_id': 1,
         'standard_flag': 1,
         'standard_relation': '=',
         'standard_text_value': None,
         'standard_type': 'IC50',
         'standard_units': 'nM',
         'standard_upper_value': None,
         'standard_value': '300.0',
         'target_chembl_id': 'CHEMBL2321613',
         'target_organism': 'Homo sapiens',
         'target_pref_name': 'Potassium channel subfamily K member 3',
         'target_tax_id': '9606',
         'text_value': None,
         'toid': None,
         'type': 'IC50',
         'units': 'nM',
         'uo_units': 'UO_0000065',
         'upper_value': None,
         'value': '300.0'}
        """
        activity = new_client.activity
        activity_results = activity.filter(
            target_chembl_id=target_results["target_chembl_id"]
        )  # .filter(standard_type="IC50")
        results["activity"] = list(activity_results)

        # == molecule

        print(f"Getting ChEMBL molecule data for {gene_symbol}")

        """Example data:
        {'atc_classifications': ['R02AD02',
          'D04AB01',
          'N01BB02',
          'S01HA07',
          'C01BB01',
          'N01BB52',
          'S02DA01',
          'C05AD01'],
         'availability_type': 1,
         'biotherapeutic': None,
         'black_box_warning': 1,
         'chebi_par_id': 6456,
         'chemical_probe': 0,
         'chirality': 2,
         'cross_references': [{'xref_id': 'lidocaine',
           'xref_name': 'lidocaine',
           'xref_src': 'DailyMed'}],
         'dosed_ingredient': True,
         'first_approval': 1948,
         'first_in_class': 0,
         'helm_notation': None,
         'indication_class': 'Anesthetic (local),Anesthetic (topical)',
         'inorganic_flag': 0,
         'max_phase': '4.0',
         'molecule_chembl_id': 'CHEMBL79',
         'molecule_hierarchy': {'active_chembl_id': 'CHEMBL79',
          'molecule_chembl_id': 'CHEMBL79',
          'parent_chembl_id': 'CHEMBL79'},
         'molecule_properties': {'alogp': '2.58',
          'aromatic_rings': 1,
          'cx_logd': '2.33',
          'cx_logp': '2.84',
          'cx_most_apka': '13.78',
          'cx_most_bpka': '7.75',
          'full_molformula': 'C14H22N2O',
          'full_mwt': '234.34',
          'hba': 2,
          'hba_lipinski': 3,
          'hbd': 1,
          'hbd_lipinski': 1,
          'heavy_atoms': 17,
          'molecular_species': 'NEUTRAL',
          'mw_freebase': '234.34',
          'mw_monoisotopic': '234.1732',
          'np_likeness_score': '-1.69',
          'num_lipinski_ro5_violations': 0,
          'num_ro5_violations': 0,
          'psa': '32.34',
          'qed_weighted': '0.85',
          'ro3_pass': 'N',
          'rtb': 5},
         'molecule_structures': {'canonical_smiles': 'CCN(CC)CC(=O)Nc1c(C)cccc1C',
          'molfile': '\n     RDKit          2D\n\n 17 17  0  0  0  0  0  0  0  0999 V2000\n   -1.0208    0.4875    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -0.4083    0.8458    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n    0.2000    0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.6458    0.8375    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.0208   -0.2167    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    0.2042   -0.2125    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0\n    0.8167    0.8458    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    1.4375    0.5000    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -2.2583   -0.2167    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.6375   -0.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -2.2583    0.4833    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -0.4000   -0.5667    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.6458    1.5583    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    2.0542    0.8458    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    1.4417   -0.2167    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    2.6667    0.4875    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    2.0542   -0.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n  2  1  1  0\n  3  2  1  0\n  4  1  2  0\n  5  1  1  0\n  6  3  2  0\n  7  3  1  0\n  8  7  1  0\n  9 10  1  0\n 10  5  2  0\n 11  4  1  0\n 12  5  1  0\n 13  4  1  0\n 14  8  1  0\n 15  8  1  0\n 16 14  1  0\n 17 15  1  0\n  9 11  2  0\nM  END\n> <chembl_id>\nCHEMBL79\n\n> <chembl_pref_name>\nLIDOCAINE',
          'standard_inchi': 'InChI=1S/C14H22N2O/c1-5-16(6-2)10-13(17)15-14-11(3)8-7-9-12(14)4/h7-9H,5-6,10H2,1-4H3,(H,15,17)',
          'standard_inchi_key': 'NNJVILVZKWQKPM-UHFFFAOYSA-N'},
         'molecule_synonyms': [{'molecule_synonym': 'ALGRX 3268',
           'syn_type': 'RESEARCH_CODE',
           'synonyms': 'ALGRX 3268'},
          {'molecule_synonym': 'ALGRX-3268',
           'syn_type': 'RESEARCH_CODE',
           'synonyms': 'ALGRX-3268'},
          {'molecule_synonym': 'Alphacaine',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'ALPHACAINE'},
          {'molecule_synonym': 'Anestacon',
           'syn_type': 'OTHER',
           'synonyms': 'Anestacon'},
          {'molecule_synonym': 'Anestacon',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'Anestacon'},
          {'molecule_synonym': 'Dentipatch',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'DENTIPATCH'},
          {'molecule_synonym': 'Embolex', 'syn_type': 'OTHER', 'synonyms': 'Embolex'},
          {'molecule_synonym': 'Iontocaine',
           'syn_type': 'OTHER',
           'synonyms': 'Iontocaine'},
          {'molecule_synonym': 'Lidocaina',
           'syn_type': 'INN_SPANISH',
           'synonyms': 'LIDOCAINA'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'USAN',
           'synonyms': 'Lidocaine'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'ATC',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'BNF',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'FDA',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'INN',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'JAN',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'MERCK_INDEX',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'OTHER',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocaine',
           'syn_type': 'USP',
           'synonyms': 'LIDOCAINE'},
          {'molecule_synonym': 'Lidocainum',
           'syn_type': 'OTHER',
           'synonyms': 'LIDOCAINUM'},
          {'molecule_synonym': 'Lidocaton',
           'syn_type': 'OTHER',
           'synonyms': 'Lidocaton'},
          {'molecule_synonym': 'Lidoderm',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'LIDODERM'},
          {'molecule_synonym': 'Lidopen', 'syn_type': 'OTHER', 'synonyms': 'Lidopen'},
          {'molecule_synonym': 'Lignocaine',
           'syn_type': 'BAN',
           'synonyms': 'LIGNOCAINE'},
          {'molecule_synonym': 'Lignocaine Hcl',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'Lignocaine HCl'},
          {'molecule_synonym': 'Lignostab',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'Lignostab'},
          {'molecule_synonym': 'Lmx 4', 'syn_type': 'TRADE_NAME', 'synonyms': 'LMX 4'},
          {'molecule_synonym': 'NSC-40030',
           'syn_type': 'RESEARCH_CODE',
           'synonyms': 'NSC-40030'},
          {'molecule_synonym': 'Octocaine',
           'syn_type': 'OTHER',
           'synonyms': 'Octocaine'},
          {'molecule_synonym': 'Oraqix',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'ORAQIX'},
          {'molecule_synonym': 'Solarcaine',
           'syn_type': 'OTHER',
           'synonyms': 'SOLARCAINE'},
          {'molecule_synonym': 'Vagisil',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'VAGISIL'},
          {'molecule_synonym': 'Xylestesin',
           'syn_type': 'OTHER',
           'synonyms': 'XYLESTESIN'},
          {'molecule_synonym': 'Xylocaine',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'XYLOCAINE'},
          {'molecule_synonym': 'Xylodase',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'XYLODASE'},
          {'molecule_synonym': 'Xylotox',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'XYLOTOX'},
          {'molecule_synonym': 'Ztlido',
           'syn_type': 'TRADE_NAME',
           'synonyms': 'ZTLIDO'}],
         'molecule_type': 'Small molecule',
         'natural_product': 1,
         'oral': True,
         'orphan': 0,
         'parenteral': True,
         'polymer_flag': 0,
         'pref_name': 'LIDOCAINE',
         'prodrug': 0,
         'structure_type': 'MOL',
         'therapeutic_flag': True,
         'topical': True,
         'usan_stem': '-caine',
         'usan_stem_definition': 'local anesthetics',
         'usan_substem': '-caine',
         'usan_year': None,
         'withdrawn_flag': False}
        """
        molecule = new_client.molecule
        molecule_chembl_ids = [a_r["molecule_chembl_id"] for a_r in activity_results]
        molecule_results = molecule.filter(
            molecule_chembl_id__in=molecule_chembl_ids, max_phase=4
        )
        results["molecule"] = list(molecule_results)

        with open(results_path, "w") as fp:
            json.dump(results, fp, indent=4)

    # == image
    drug_id = "CHEMBL714"
    drug_name = "ALBUTEROL"
    image_path = Path(f"../results/{drug_name}-chembl.svg")
    if not image_path.exists() or args.force:

        print(f"Getting ChEMBL SVG for {drug_name}")

        image = new_client.image
        image.set_format("svg")
        with open(image_path, "w") as fp:
            fp.write(image.get(drug_id))


if __name__ == "__main__":
    main()
