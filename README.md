# MCP Guild

Welcome to the official repository for the **MCP Guild**! 🚀

This repository serves as our central hub for learning, building, and deploying servers and clients using the **Model Context Protocol (MCP)**. It contains hands-on implementations following the tutorial **[MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM)** by Ansh Lamba (companion repo: `anshlambagit/MCP_Masterclass`).

---

## 🛠️ Tech Stack

- **Language**: Python 3.12+
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (fast Python dependency resolver)
- **MCP Frameworks**: [FastMCP](https://github.com/jondot/fastmcp), Official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- **LLM Integration**: [LangChain](https://www.langchain.com/), `langchain-mcp-adapters`
- **Testing & GUI**: `@modelcontextprotocol/inspector` (via Node.js / `npx`)

---

## 📂 Project Structure

```text
MCP-Guild/
├── 1_CreateMCP/                  # Chapter 1: Standard Input/Output (STDIO) MCP
│   ├── 1_MCPServer_stdio.py      # First FastMCP server over stdio transport
│   ├── 2_python_client.py        # Native Python client testing stdio server
│   └── 3_langchain_client.py     # LangChain client integrating stdio MCP tools
├── 2_HTTP_MCP/                   # Chapter 2: Streamable HTTP Transport
│   ├── 1_http_mcp.py             # HTTP MCP server running on port 8050
│   └── 2_langchain_client.py     # LangChain client connecting over HTTP (/mcp)
├── docs/                         # Step-by-step educational documentation
│   ├── README.md                 # Documentation master index & curriculum
│   ├── 01_chapter1_stdio_mcp_server.md
│   ├── 02_chapter1_python_client.md
│   ├── 03_chapter1_langchain_client.md
│   ├── 04_chapter2_http_mcp.md
│   ├── 05_chapter2_langchain_http.md
│   └── 06_chapter2_mcp_inspector.md
├── AGENTS.md                     # Agent workflow instructions & rules
├── pyproject.toml                # Project configuration & dependencies
└── README.md                     # This file
```

---

## 🗺️ Masterclass Progress

| Phase | Chapter & Topic | Status | Detailed Guide |
| :---: | :--- | :---: | :--- |
| **01** | **Chapter 1**: STDIO MCP Server (`fetch`, `process`) | ✅ Completed | [01_chapter1_stdio_mcp_server.md](docs/01_chapter1_stdio_mcp_server.md) |
| **02** | **Chapter 1**: Native Python MCP Client | ✅ Completed | [02_chapter1_python_client.md](docs/02_chapter1_python_client.md) |
| **03** | **Chapter 1**: LangChain Adapter Integration | ✅ Completed | [03_chapter1_langchain_client.md](docs/03_chapter1_langchain_client.md) |
| **04** | **Chapter 2**: Streamable HTTP MCP Server (Port 8050) | ✅ Completed | [04_chapter2_http_mcp.md](docs/04_chapter2_http_mcp.md) |
| **05** | **Chapter 2**: LangChain HTTP Client | ✅ Completed | [05_chapter2_langchain_http.md](docs/05_chapter2_langchain_http.md) |
| **06** | **Chapter 2**: MCP Inspector GUI Debugging | ✅ Completed | [06_chapter2_mcp_inspector.md](docs/06_chapter2_mcp_inspector.md) |
| **07** | **Chapter 3**: Community & 3rd-Party MCPs | ✅ Completed | [07_chapter3_community_mcps.md](docs/07_chapter3_community_mcps.md) |
| **08** | **Chapter 4**: Deploying MCP to PyPI | ⏳ Upcoming | `08_chapter4_pypi_deployment.md` |
| **09** | **Chapter 5**: Building an MCP Gateway | ⏳ Upcoming | `09_chapter5_mcp_gateway.md` |
| **10** | **Chapter 6**: Containerizing MCP with Docker | ⏳ Upcoming | `10_chapter6_docker_deployment.md` |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Python 3.12+** installed
- **uv** installed (`pip install uv` or winget/curl)
- **Node.js** (for MCP Inspector GUI)

### 2. Environment Setup
Clone the repository and sync all dependencies:
```bash
uv sync
```

---

### 3. Running Chapter 1: STDIO MCP

#### Step 1: Run the Server Directly
```bash
uv run python 1_CreateMCP/1_MCPServer_stdio.py
```

#### Step 2: Test with the Native Python Client
```bash
uv run python 1_CreateMCP/2_python_client.py
```

#### Step 3: Test with LangChain
```bash
uv run python 1_CreateMCP/3_langchain_client.py
```

---

### 4. Running Chapter 2: HTTP MCP

#### Step 1: Start the HTTP Server (Terminal 1)
```bash
uv run python 2_HTTP_MCP/1_http_mcp.py
```
> The server listens on `http://127.0.0.1:8050/mcp`.

#### Step 2: Test with LangChain HTTP Client (Terminal 2)
```bash
uv run python 2_HTTP_MCP/2_langchain_client.py
```

#### Step 3: Inspect visually with MCP Inspector
```bash
npx @modelcontextprotocol/inspector
```
1. Open the inspector URL (e.g. `http://localhost:6274`).
2. Select **Streamable HTTP** and enter `http://127.0.0.1:8050/mcp`.
3. Click **Connect** and test tools interactively!

---

## 📖 In-Depth Guides

For comprehensive line-by-line code breakdowns, theoretical concepts, and troubleshooting, explore the [docs/ directory](docs/README.md).

---

## 🤝 Contributing

Contributions, feedback, and questions are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.