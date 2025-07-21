# FastMCP + FastAPI

It is a hello world server written using [FastAPI](https://fastapi.tiangolo.com/) and [fastmcp](https://github.com/jlowin/fastmcp).

## Prerequisite

- install uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- create virtual environment

```
uv venv
```

## Usage

- activate environment

```
source .venv/bin/activate
```

- install packages

```
uv sync
```

- run

  - with python

    ```
    python server.py

    ```

  - or with uvicorn

    ```
    uvicorn server:app --host 0.0.0.0 --port 9090 --reload
    ```

## Test

You can test the server using following curl command

```
curl --location 'http://127.0.0.1:9090/api/v1/mcp' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/event-stream' \
--data '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "add",
    "arguments": {
      "a": 3,
      "b": 4
    }
  }
}'
```
