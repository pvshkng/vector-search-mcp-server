from fastmcp import FastMCP, Context
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair
from app.core.embeddings import embedding_service
from app.core.vector_store import vector_store
from typing import Annotated

key_pair = RSAKeyPair.generate()

mcp = FastMCP(name="Vector_Search_MCP_Server", port=8000)

# description="Search for documents using vector embeddings"


@mcp.tool(name="vector_search")
async def vector_search(
    query: Annotated[
        str,
        "User's natural language question about Text2SQL research. The query will be enhanced to focus on technical and academic aspects before being converted to embeddings for vector search."
    ],
    ctx: Context = Context(),
):
    """Search and retrieve relevant chunks from academic papers about Text2SQL technology and research.

    This tool performs semantic search on a collection of Text2SQL research papers. It enhances the input query
    to focus on technical aspects of converting natural language to SQL queries, such as:
    - Neural architectures for Text2SQL
    - Schema linking and database context understanding
    - SQL query generation techniques
    - Evaluation methodologies and benchmarks
    - Error handling and query optimization

    Example queries:
        - "What are the latest approaches for handling complex joins in Text2SQL?"
        - "How do Text2SQL models handle schema understanding?"
        - "Best practices for evaluating Text2SQL models
    """

    query_embedding = embedding_service.encode(query)
    results = await vector_store.search(query_embedding)

    return [
        {
            "score": hit.distance,
            "document_name": hit.entity.get("document_name"),
            "chunk": hit.entity.get("chunk"),
        }
        for hits in results
        for hit in hits
    ]

if __name__ == "__main__":
    mcp.run(transport="sse")
