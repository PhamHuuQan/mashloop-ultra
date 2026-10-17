# MashLoop Ultra

> A community-derived enhancement track for Mash ∞ Loop. The goal is to preserve the original music-analysis and continuous-mixing engine while adding better playback reliability, library management, accessibility, observability, and test coverage.

## Upstream and attribution

- Upstream project: https://github.com/lvt1693/mashloop
- Upstream demo: https://mashloop.truclv.com
- The upstream project includes an MIT license. Preserve upstream attribution and the original `LICENSE` when distributing derived versions.
- This repository is a separate development line. Changes here do not modify the upstream repository.

## Development principles

1. Keep the original playback and analysis flow working before refactoring.
2. Make upgrades incremental and feature-flagged where appropriate.
3. Do not claim audio-quality improvements until they have automated tests and listening/evaluation results.
4. Do not bypass copyright controls, login requirements, paywalls, or source-platform restrictions.
5. Keep secrets, downloaded audio, caches, and personal session data out of Git.

## Planned upgrade roadmap

- [ ] Establish an upstream-compatible baseline and verify local startup.
- [ ] Add repeatable smoke and end-to-end tests for ingest, analysis, transitions, and playback.
- [ ] Improve diagnostics: actionable download/analysis errors and visible task progress.
- [ ] Improve player resilience: recovery after refresh, predictable queue behavior, and graceful handling of missing media.
- [ ] Improve library usability: saved playlists, queue editing, and clearer track/analysis states.
- [ ] Evaluate transition quality with measurable criteria before changing the DSP engine.
- [ ] Add security checks for URL validation, uploads, session isolation, and resource limits.
- [ ] Document local setup and deployment with tested commands.

## Status

This repository has just been initialized. A roadmap item is not considered complete until code and tests have been committed.

## Local development

The upstream project documents a Python 3.11+ environment, FFmpeg, Node.js 20+, PyTorch/torchaudio, Beat This!, and Demucs. Review upstream `README.md`, `requirements.txt`, `constraints.txt`, and `run.ps1` after importing the source tree. First-time model downloads and audio processing can require substantial disk, memory, and compute resources.

## Legal and source policy

Use audio only where you have the right to access and process it. Respect platform terms, artists' rights, and source availability. Do not treat this app as a way to defeat DRM or other technical access restrictions.
