# Environment Setup

## Recommended Architecture

```text
Windows Host
|
+-- WSL2
|    |
|    +-- Ubuntu
|         |
|         +-- Git
|         +-- Python
|         +-- Node.js
|         +-- Docker Engine
|         +-- Docker Compose
|         |
|         +-- ~/projects/
|              |
|              +-- soc-log-collector
|
+-- Browser
|
+-- Antigravity / VS Code
|
+-- Optional Windows VM
     |
     +-- collector.exe testing
```

## Git

Install Git inside WSL once.

```bash
sudo apt update
sudo apt install git -y
```

Verify:

```bash
git --version
```

Git does not need to be installed separately for each repository.

## Python

Check:

```bash
python3 --version
```

Use a virtual environment for Python development:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Node.js

Check:

```bash
node --version
npm --version
```

Use a current LTS release.

## Docker

Check:

```bash
docker --version
docker compose version
```

If Docker Engine is already working inside WSL, Docker Desktop is not required.

## Windows Collector

The collector should be tested on an actual Windows environment.

For safe testing, a Windows VM can be used.

The collector is eventually packaged with PyInstaller:

```text
Python application
        |
     PyInstaller
        |
   collector.exe
```

## AI Development

Recommended primary workflow:

- Antigravity for agentic coding
- ChatGPT for architecture, learning, debugging, and review
- Git for version control

Keep the repository documentation as the source of truth rather than relying on an AI conversation's memory.
