# AI-Ops-Agent

An LLM-driven autonomous troubleshooting and code generation workflow designed for infrastructure maintenance, network diagnostics, log analysis and script-assisted repair.

---

## Project Background

In daily infrastructure and development maintenance, repetitive troubleshooting tasks such as:

- OpenWrt / ImmortalWrt network conflicts
- OpenClash DNS abnormality
- Windows BSOD dump analysis
- Batch / Shell / Python script debugging
- Configuration migration and compatibility checks

usually require engineers to manually search logs, compare configuration files, inspect historical cases, and repeatedly validate repair commands.

This process is highly dependent on human experience and often consumes 30~120 minutes for a single complex issue.

AI-Ops-Agent was built to solve this bottleneck by introducing a long-chain reasoning based multi-agent workflow.

---

## Core Pain Points Solved

### 1. Repetitive log inspection is inefficient
System logs, crash dumps, router configs and command outputs are usually fragmented and noisy.

### 2. Manual configuration fixing is error-prone
A single wrong dnsmasq, firewall or interface parameter can cause complete service failure.

### 3. Traditional Q&A AI lacks execution workflow
Normal chatbot response cannot perform structured diagnosis, verification and script generation.

---

## Multi-Agent Architecture

AI-Ops-Agent adopts a coordinator + sub-agent model.

### Main Coordinator Agent
Responsible for:

- user request intake
- context understanding
- task decomposition
- long-chain reasoning scheduling

### Parser Agent
Parses:

- log files
- config files
- command outputs
- stack traces
- dump summaries

and converts them into machine-readable issue context.

### Reasoning Agent
Performs iterative root-cause deduction:

Issue symptoms  
→ historical pattern matching  
→ possible root cause hypothesis  
→ dependency verification  
→ confidence scoring

This module supports long-chain reasoning rather than single-pass direct answering.

### Script Generator Agent
Automatically generates:

- Shell fix scripts
- PowerShell recovery commands
- Python analysis snippets
- Batch automation scripts

based on the validated diagnosis result.

### Validation Agent
Performs:

- syntax verification
- compatibility check
- side effect estimation
- rollback suggestion generation

to close the execution loop.

---

## Workflow Logic

User Input  
↓  
Coordinator Agent receives logs/config/errors  
↓  
Parser Agent extracts anomaly features  
↓  
Reasoning Agent performs multi-step diagnosis  
↓  
Script Agent generates repair instructions  
↓  
Validation Agent checks risk & compatibility  
↓  
Final structured repair solution exported

---

## Typical Use Cases

### ImmortalWrt/OpenClash DNS Port Conflict Diagnosis
Automatic recognition of:

- Port 53 occupation
- dnsmasq startup conflict
- IPv6 RA abnormal routes
- fake-ip fallback issue

### Windows Crash Dump Analysis
Automatic parsing of:

- CLOCK_WATCHDOG_TIMEOUT
- DRIVER_IRQL_NOT_LESS_OR_EQUAL
- GPU driver timeout
- kernel process deadlock

### Script Refactoring
Generate optimized:

- bat
- shell
- python
- powershell

automation scripts for repetitive maintenance tasks.

---

## Current Usage Scale

- Daily active troubleshooting sessions: 40+
- Average long-context interaction length: 8K~30K tokens
- Daily token consumption: 3M ~ 5M+
- Main usage scenario: infrastructure diagnosis & automated repair reasoning

---

## Current Impact

Compared with manual troubleshooting:

- fault locating efficiency improved by ~70%
- repetitive document searching reduced significantly
- repair script drafting time reduced by ~80%
- configuration modification error rate lowered substantially

---

## Future Plan

Next phase will integrate:

- local execution bridge
- command sandbox verification
- self-healing script recommendation
- continuous case memory retrieval

to build a fully closed autonomous AIOps maintenance assistant.

---

## Status

Actively used in real-world daily infrastructure maintenance and AI-assisted technical support workflow.