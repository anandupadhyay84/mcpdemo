# MCP Demo

This project demonstrates a simple Multi-Server MCP (Modular Command Protocol) setup using Python. It includes a math server, a weather server, and a client that interacts with both using LangChain and MCP adapters.

## Project Structure

- `mathserver.py`: Provides math operations (add, subtract) as MCP tools.
- `weatherserver.py`: Provides weather information for cities as an MCP tool.
- `client.py`: Connects to both servers and demonstrates tool invocation.
- `requirements.txt`: Lists required Python packages.

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Start the weather server:**
   ```sh
   python weatherserver.py
   ```

3. **Run the client:**
   ```sh
   python client.py
   ```
   > The client will automatically start the math server as a subprocess.

## Example Output

```
Math Response: 8
Weather Response: Sunny, 25°C
```

## Notes

- The math server uses `stdio` transport.
- The weather server uses `streamable_http` transport on `http://127.0.0.1:8000/mcp`.
- Update the `api_key` in `client.py` for the language model