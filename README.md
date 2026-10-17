# MashLoop Ultra

A separate development line based on [Mash ∞ Loop](https://github.com/lvt1693/mashloop). It preserves the upstream music-analysis, infinite-loop, and cross-track DJ-mixing engine while adding reliability and usability improvements incrementally.

**Upstream attribution:** the original project and its MIT license are preserved. The original documentation is available in [UPSTREAM_README.md](UPSTREAM_README.md). This repository is not the upstream project and does not modify it.

## What is in this repository

- Original Python analysis pipeline, beat/key/mood and phrase-structure analysis, transition search, and worker orchestration.
- Original FastAPI server, track/source ingestion, session handling, and audio streaming.
- Original web player, visualization, UI styles, and time-stretching vendor module.
- Original test/evaluation utilities and deployment scripts.
- A new JSON liveness endpoint at `/health` and `/api/health`, plus a small standard-library test.

## New changes in Ultra

### 0.1.0 — Baseline import + health check
- Imported the upstream source files and retained the upstream README as `UPSTREAM_README.md`.
- Added `GET /health` and `GET /api/health` for platform liveness checks. Responses are JSON and intentionally avoid exposing filesystem paths or secrets.
- Added `tools/test_health.py` to verify that both routes are registered and the payload stays minimal.

The health endpoint is a **liveness** check; it does not claim that model downloads, audio analysis workers, or external source providers are all healthy.

## Run locally

Follow the prerequisites and Windows setup steps in [UPSTREAM_README.md](UPSTREAM_README.md). In summary, the upstream project expects Python 3.11+, FFmpeg, Node.js 20+, and its documented PyTorch/torchaudio, Beat This!, and Demucs setup. Audio analysis may download model weights the first time.

After installing dependencies, run from the repository root:

```powershell
.\run.ps1
```

The app defaults to `http://127.0.0.1:8765`; the liveness check is at `http://127.0.0.1:8765/health`.

Run the health-route test with:

```powershell
.\.venv\Scripts\python.exe tools\test_health.py
```

## Development priorities

1. Establish a reproducible smoke-test baseline and report failures clearly.
2. Harden player/library recovery after refresh and transient source errors.
3. Improve queue and analysis progress visibility.
4. Add measured transition-quality evaluation before changing DSP behavior.
5. Audit uploads, URL handling, session boundaries, resource limits, and deployment settings.

Items above are plans, not claimed completed features. Changes should remain incremental and must not silently bypass platform terms, DRM, paywalls, or artists' rights.
