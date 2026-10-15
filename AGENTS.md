# Agent Instructions — MCP Guild Course Implementation

## 🎯 Project Goal
Follow and implement the **[MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM)** tutorial by Ansh Lamba (companion repo: `anshlambagit/MCP_Masterclass`) step-by-step for educational purposes.

---

## 📋 Mandatory Workflow Rules for Every Step

Whenever the user asks to implement the next step or phase:

### 1. Step-by-Step Implementation Only
- Implement **one phase/stage at a time** in strict chronological alignment with the course timestamps.
- Do NOT jump ahead or bundle multiple phases into a single unguided code dump.

### 2. File Organization
- Organize code into matching chapter directories:
  - Chapter 1: `CreateMCP/` (`1_MCPServer_stdio.py`, `2_python_client.py`, `3_langchain_client.py`)
  - Chapter 2: `CH-2_HTTP_MCP/` (`1_http_mcp.py`, `2_langchain_client.py`)
  - Chapter 3: `CH-3_3rdParty_MCPs/`
  - Chapter 4: `CH-4_PyPI_MCP/`
  - Chapter 5: `CH-5_MCP_Gateway/`
  - Chapter 6: `CH-6_MCP_Docker/`

### 3. Detailed Explanations
For every file/phase created or modified, explain:
- **Video Timestamp Reference**: Exact point in the tutorial.
- **What this part does**: Architectural purpose, transport mechanism, and key concepts.
- **Code breakdown**: Line-by-line / block-by-block explanation of the logic.

### 4. Running & Testing
- Always provide the **exact, copy-pasteable command** to execute and test the file using `uv run`.
- Proactively run and verify the script in the terminal to ensure zero runtime or dependency errors.
- Document the **expected terminal output**.

### 5. Documentation Maintenance
For each phase:
- **Dedicated Guide**: Create a corresponding markdown file in `docs/` (e.g. `docs/04_chapter2_http_mcp.md`).
- **Update Master Index**: Update `docs/README.md` with:
  - Stage completion status (✅ Completed).
  - Quick-start end-to-end command sequence.
  - Clickable link to the new phase guide.

### 6. Dependency & Version Safety
- Use `uv` for all package management (`uv add`, `uv run`).
- Keep `fastmcp`, `mcp`, and `langchain-mcp-adapters` mutually compatible.
- Ensure previous working stages are never broken by new package installations.
