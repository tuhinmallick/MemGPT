# import tempfile
# import asyncio
import os

# import asyncio
from datasets import load_dataset

import memgpt
from memgpt.cli.cli_load import load_directory, load_database, load_webpage

# import memgpt.presets as presets
# import memgpt.personas.personas as personas
# import memgpt.humans.humans as humans
# from memgpt.persistence_manager import InMemoryStateManager, LocalStateManager

# # from memgpt.config import AgentConfig
# from memgpt.constants import MEMGPT_DIR, DEFAULT_MEMGPT_MODEL
# import memgpt.interface  # for printing to terminal


def test_postgres():
    return


def test_chroma():
    return

    # index = memgpt.embeddings.Index(name)

    ## query chroma
    ##chroma_client = chromadb.Client()
    # chroma_client = chromadb.PersistentClient(path="/Users/sarahwooders/repos/MemGPT/chromadb")
    # collection = chroma_client.get_collection(name=name)
    # results = collection.query(
    #    query_texts=["cinderella be getting sick"],
    #    n_results=2
    # )
    # print(results)
    # assert len(results) == 2, f"Expected 2 results, but got {len(results)}"


def test_load_directory():
    return


def test_load_webpage():
    pass


def test_load_database():
    return
