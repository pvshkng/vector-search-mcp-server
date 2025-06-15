from fastmcp import Context
async def log_request_details(ctx: Context):
    """Log detailed information about the incoming request."""
    try:
        request = ctx.get_http_request()
        
        sections = []
        
        sections.append("=== Request Information ===")
        sections.append(f"Method: {request.method}")
        sections.append(f"URL: {request.url}")
        
        sections.append("\n=== Headers ===")
        for header, value in request.headers.items():
            if header.lower() in ['authorization', 'cookie', 'api-key']:
                sections.append(f"{header}: [MASKED]")
            else:
                sections.append(f"{header}: {value}")
        
        sections.append("\n=== Request Body ===")
        try:
            body = await request.body()
            if body:
                try:
                    body_text = body.decode('utf-8')
                    sections.append(f"Body: {body_text}")
                except UnicodeDecodeError:
                    sections.append("Body: [Binary content]")
            else:
                sections.append("Body: [Empty]")
        except Exception as e:
            sections.append(f"Body: [Error reading body: {str(e)}]")
        
        sections.append("\n=== Query Params ===")
        if request.query_params:
            for param, value in request.query_params.items():
                sections.append(f"{param}: {value}")
        else:
            sections.append("No query parameters")

        sections.append("\n=== Client Info ===")
        if request.client:
            sections.append(f"Client Host: {request.client.host}")
            sections.append(f"Client Port: {request.client.port}")
        else:
            sections.append("No client information available")
        
        print("\n".join(sections))
        
    except Exception as e:
        print(f"Error logging request details: {str(e)}")