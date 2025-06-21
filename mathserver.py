from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of the two integers.
    """
    print(f"add() called with a={a}, b={b}")
    result = a + b
    print(f"add() returning {result}")
    return result


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The result of the subtraction.
    """
    print(f"subtract() called with a={a}, b={b}")
    result = a - b
    print(f"subtract() returning {result}")
    return


if __name__ == "__main__":
    print("Starting Math MCP Server...")
    mcp.run(transport="stdio")