from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair
from app.core.embeddings import embedding_service
from app.core.vector_store import vector_store
from fastmcp.server.dependencies import get_access_token, AccessToken

key_pair = RSAKeyPair.generate()

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    issuer="https://dev.example.com",
    audience="vector-search-mcp"
)
mcp = FastMCP(name="Vector_Search_MCP_Server", port=8000, auth=auth)

dev_token = key_pair.create_token(
    subject="dev-user",
    issuer="https://dev.example.com",
    audience="vector-search-mcp",
    scopes=["search:read"]
)

# print(f"Use this token for authentication: {dev_token}")

@mcp.tool
async def vector_search(query: str):
    
    # access_token: AccessToken = get_access_token()
    # user_id = access_token.client_id  
    # user_scopes = access_token.scopes


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
