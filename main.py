from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="FHIRReferenceServer",
    instructions="""
    This server provides FHIR reference materials, Clinical Quality Language reference materials, and access to medical terminology and coding APIs.
    """,
)