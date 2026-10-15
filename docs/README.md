# MCP Guild — Complete Step-by-Step Masterclass Guide

This repository contains hands-on implementations based on the course:
**[MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM)** by Ansh Lamba.

---

## 🗺️ Master Curriculum & Progress

| Phase | Chapter | Topic | File / Tool | Guide | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **01** | **Chapter 1** (49:13) | **STDIO MCP Server** | [1_MCPServer_stdio.py](file:///d:/Projects/MCP%20Guild/1_CreateMCP/1_MCPServer_stdio.py) | [01_chapter1_stdio_mcp_server.md](file:///d:/Projects/MCP%20Guild/docs/01_chapter1_stdio_mcp_server.md) | ✅ Completed |
| **02** | **Chapter 1** (1:01:00) | **Python MCP Client** | [2_python_client.py](file:///d:/Projects/MCP%20Guild/1_CreateMCP/2_python_client.py) | [02_chapter1_python_client.md](file:///d:/Projects/MCP%20Guild/docs/02_chapter1_python_client.md) | ✅ Completed |
| **03** | **Chapter 1** (1:21:38) | **LangChain Integration** | [3_langchain_client.py](file:///d:/Projects/MCP%20Guild/1_CreateMCP/3_langchain_client.py) | [03_chapter1_langchain_client.md](file:///d:/Projects/MCP%20Guild/docs/03_chapter1_langchain_client.md) | ✅ Completed |
| **04** | **Chapter 2** (1:34:04) | **HTTP MCP Server** | [1_http_mcp.py](file:///d:/Projects/MCP%20Guild/2_HTTP_MCP/1_http_mcp.py) | [04_chapter2_http_mcp.md](file:///d:/Projects/MCP%20Guild/docs/04_chapter2_http_mcp.md) | ✅ Completed |
| **05** | **Chapter 2** (1:55:07) | **HTTP LangChain Client** | [2_langchain_client.py](file:///d:/Projects/MCP%20Guild/2_HTTP_MCP/2_langchain_client.py) | [05_chapter2_langchain_http.md](file:///d:/Projects/MCP%20Guild/docs/05_chapter2_langchain_http.md) | ✅ Completed |
| **06** | **Chapter 2** (1:42:44) | **MCP Inspector Debugging** | `@modelcontextprotocol/inspector` | [06_chapter2_mcp_inspector.md](file:///d:/Projects/MCP%20Guild/docs/06_chapter2_mcp_inspector.md) | ✅ Completed |
| **07** | **Chapter 3** (2:08:17) | **Community & 3rd-Party MCPs** | `3_3rdParty_MCPs/` | `07_chapter3_community_mcps.md` | ⏳ Upcoming |
| **08** | **Chapter 4** (2:36:51) | **Deploying to PyPI** | `MCP_PYPI/` | `08_chapter4_pypi_deployment.md` | ⏳ Upcoming |
| **09** | **Chapter 5** (3:19:15) | **Creating an MCP Gateway** | `5_MCP_Gateway/` | `09_chapter5_mcp_gateway.md` | ⏳ Upcoming |
| **10** | **Chapter 6** (3:31:12) | **Dockerizing MCP Server** | `6_MCP_Docker/` | `10_chapter6_docker_deployment.md` | ⏳ Upcoming |

---

## ⚡ Quick Start: Running Every Stage End-to-End

### 1. Environment Setup
The project uses [uv](https://github.com/astral-sh/uv) and Node/npm.

```bash
# Sync Python dependencies
uv sync
```

### 2. Stage 1: Run the First STDIO Server
```bash
uv run python 1_CreateMCP/1_MCPServer_stdio.py
```

### 3. Stage 2: Test with Native Python MCP Client
```bash
uv run python 1_CreateMCP/2_python_client.py
```

### 4. Stage 3: Test with LangChain Adapter
```bash
uv run python 1_CreateMCP/3_langchain_client.py
```

### 5. Stage 4: Run the Streamable HTTP MCP Server
```bash
uv run python 2_HTTP_MCP/1_http_mcp.py
```
> Listens on `http://127.0.0.1:8050/mcp`.

### 6. Stage 5: Test HTTP Server via LangChain Client
```bash
uv run python 2_HTTP_MCP/2_langchain_client.py
```

### 7. Stage 6: Test & Debug with MCP Inspector (GUI)
```bash
npx @modelcontextprotocol/inspector
```
> Opens web interface at `http://localhost:5173`. Connect to `http://127.0.0.1:8050/mcp` using `Streamable HTTP`.

---

## 📁 Detailed Phase Guides
- [Phase 1 Guide: STDIO MCP Server](file:///d:/Projects/MCP%20Guild/docs/01_chapter1_stdio_mcp_server.md)
- [Phase 2 Guide: Native Python Client](file:///d:/Projects/MCP%20Guild/docs/02_chapter1_python_client.md)
- [Phase 3 Guide: LangChain MCP Integration](file:///d:/Projects/MCP%20Guild/docs/03_chapter1_langchain_client.md)
- [Phase 4 Guide: Streamable HTTP MCP Server](file:///d:/Projects/MCP%20Guild/docs/04_chapter2_http_mcp.md)
- [Phase 5 Guide: LangChain HTTP Client](file:///d:/Projects/MCP%20Guild/docs/05_chapter2_langchain_http.md)
- [Phase 6 Guide: MCP Inspector Debugging](file:///d:/Projects/MCP%20Guild/docs/06_chapter2_mcp_inspector.md)
