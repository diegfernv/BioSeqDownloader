from typing import Any, Dict, List
import re
import pandas as pd

# Constants
DATABASES = {
    'go_terms': 'GO',
    'pfam_ids': 'Pfam',
    'alphafold_ids': 'AlphaFoldDB',
    'pdb_ids': 'PDB',
    'kegg_ids': 'KEGG',
    'brenda_ids': 'BRENDA',
    'reactome_ids': 'Reactome',
    'refseq_ids': 'RefSeq'
}

# Specific extraction functions
def extract_simple(value: Any) -> Any:
    """Extracts a simple value from the data"""
    return value

def extract_ec_numbers(ec_data: List) -> List[str]:
    """Extracts EC numbers"""
    return [ec['value'] for ec in ec_data] if isinstance(ec_data, list) else []

def extract_database_terms(xrefs: List, database: str) -> List[str]:
    """Extracts database terms"""
    return [x['id'] for x in xrefs if isinstance(x, dict) and x.get('database') in database]

def extract_references(refs: List) -> List[Dict]:
    """Extracts references"""
    extracted = []
    for ref in refs if isinstance(refs, list) else []:
        citation = ref.get('citation', {})
        extracted.append({
            'title': citation.get('title'),
            'authors': citation.get('authors', []),
            'journal': citation.get('journal'),
            'pub_date': citation.get('publicationDate'),
            'pmid': next((x['id'] for x in citation.get('citationCrossReferences', []) 
                        if x.get('database') == 'PubMed'), None)
        })
    return extracted

def extract_features(features: List) -> List[Dict]:
    """Extracts protein features"""
    return [{
        'type': f.get('type'),
        'description': f.get('description', ''),
        'location': f.get('location', {})
    } for f in features if isinstance(features, list)]

def extract_keywords(keywords: List) -> List[str]:
    """Extracts keywords"""
    return [kw.get('name', '') for kw in keywords if isinstance(keywords, list)]
