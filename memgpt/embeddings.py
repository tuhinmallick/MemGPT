import typer
import os
from llama_index.embeddings import OpenAIEmbedding


def embedding_model():
    """Return LlamaIndex embedding model to use for embeddings"""

    from memgpt.config import MemGPTConfig

    # load config
    config = MemGPTConfig.load()

    endpoint = config.embedding_model
    if endpoint == "azure":
        return OpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name=config.azure_embedding_deployment,
            api_key=config.azure_key,
            api_base=config.azure_endpoint,
            api_type="azure",
            api_version=config.azure_version,
        )
    elif endpoint == "openai":
        return OpenAIEmbedding(
            api_base="https://api.openai.com/v1", api_key=config.openai_key
        )
    else:
        # default to hugging face model
        from llama_index.embeddings import HuggingFaceEmbedding

        os.environ["TOKENIZERS_PARALLELISM"] = "False"
        return HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    # TODO: add back if we decide to support custom embedding endpoints
    # else:
    #    # use env variable OPENAI_API_BASE
    #    model = OpenAIEmbedding()
    #    return model
