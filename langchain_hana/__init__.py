from importlib import metadata

from langchain_hana.chains.graph_qa import HanaSparqlQAChain
from langchain_hana.embeddings import (
    HanaInternalEmbeddings,
    MultiGPUEmbeddings,
    HanaTensorRTMultiGPUEmbeddings,
    CacheConfig
)
from langchain_hana.error_utils import create_context_aware_error, handle_database_error
from langchain_hana.graphs import HanaRdfGraph
from langchain_hana.vectorstores import HanaDB

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    # Vector stores
    "HanaDB",
    
    # Embeddings
    "HanaInternalEmbeddings",
    "MultiGPUEmbeddings",
    "HanaTensorRTMultiGPUEmbeddings",
    "CacheConfig",
    
    # Graphs
    "HanaRdfGraph",
    
    # Chains
    "HanaSparqlQAChain",
    
    # Utilities
    "create_context_aware_error",
    "handle_database_error",
    
    # Version
    "__version__",
]
