from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Retrieves the weather for a given city.
    
    Parameters:
    city (str): The name of the city to get the weather for.
    
    Returns:
    str: A string describing the current weather in the city.
    """
    print(f"get_weather() called with city={city}")
    # Simulated weather data
    weather_data = {
        "New York": "Sunny, 25°C",
        "Los Angeles": "Cloudy, 22°C",
        "Chicago": "Rainy, 18°C"
    }
    
    result = weather_data.get(city, "Weather data not available for this city.")
    print(f"get_weather() returning {result}")
    return result

if __name__ == "__main__":
    print("Starting Weather MCP Server...")
    mcp.run(transport="streamable-http")