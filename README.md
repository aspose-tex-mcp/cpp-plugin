# Aspose.TeX for C++ Extraction Plugin

Prepare Aspose.TeX for C++ documentation and API references for retrieval through the Aspose context engine and MCP server.

This Python worker discovers Markdown, extracts documentation and C++ examples, produces chunks and structured symbols, and supplies a retrieval profile. Runtime dependencies are standard-library only. It does not serve HTTP or compile C++ code.

## Project family

| Repository | Responsibility |
| --- | --- |
| [context-engine](https://github.com/aspose-core-mcp/context-engine) | Shared ingestion, storage, retrieval and MCP infrastructure |
| [cpp-plugin](https://github.com/aspose-tex-mcp/cpp-plugin) | TeX C++ extraction and retrieval configuration (this repository) |
| `aspose-tex-mcp/cpp-server` | Separate deployment integrating the engine and plugin |

## Quick start

Requires Python 3.12+ and Git. From this plugin checkout:

```powershell
py -3.12 -m venv .venv
$pluginPython = Join-Path $PWD '.venv/Scripts/python.exe'
$env:PYTHONPATH = Join-Path $PWD 'src'
& $pluginPython -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Plugin tests failed.' }
```

Linux:

```sh
python3.12 -m venv .venv
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -v
```

Tests use fixtures and do not require downloaded corpora or an engine. Clone this repository with `git clone https://github.com/aspose-tex-mcp/cpp-plugin.git` if you do not already have a checkout.

## Download sources

Run from the plugin root. These are normal clones, without sparse checkout. Use only when the destination folders do not exist:

```powershell
$env:GIT_LFS_SKIP_SMUDGE = '1'
New-Item -ItemType Directory -Force sources | Out-Null
git clone --branch main https://github.com/aspose-tex-mcp/docs.git sources/tex-documentation
if ($LASTEXITCODE -ne 0) { throw 'Documentation clone failed.' }
git clone --branch master https://github.com/aspose-tex-mcp/reference.git sources/tex-api-reference
if ($LASTEXITCODE -ne 0) { throw 'API reference clone failed.' }
```

Linux:

```sh
export GIT_LFS_SKIP_SMUDGE=1
mkdir -p sources
git clone --branch main https://github.com/aspose-tex-mcp/docs.git sources/tex-documentation
git clone --branch master https://github.com/aspose-tex-mcp/reference.git sources/tex-api-reference
```

Stop if a clone fails. LFS binary downloads are skipped; source Markdown is still checked out. Although the repositories contain other content, the manifest selects only these C++ paths:

| Source | Local path | Prefix | Branch |
| --- | --- | --- | --- |
| Docs | `sources/tex-documentation` | `en/cpp` | `main` |
| API | `sources/tex-api-reference` | `english/cpp` | `master` |

Do not change sources while ingestion is running. Existing checkouts must match the manifest's repositories; preserve local work before migrating an old checkout.

## Prepare Gist examples and audit

Cloning documentation does not download the referenced Gist code. In the same PowerShell session:

```powershell
& $pluginPython -m adcs_tex_cpp.gist_examples --source-root sources/tex-documentation/en/cpp --cache sources/gist-examples.json --resolve-history
if ($LASTEXITCODE -ne 0) { throw 'Gist preparation failed.' }
& $pluginPython scripts/audit_sources.py --output artifacts/corpus-audit.json
if ($LASTEXITCODE -ne 0) { throw 'Corpus audit failed.' }
```

Linux:

```sh
PYTHONPATH=src .venv/bin/python -m adcs_tex_cpp.gist_examples --source-root sources/tex-documentation/en/cpp --cache sources/gist-examples.json --resolve-history
.venv/bin/python scripts/audit_sources.py --output artifacts/corpus-audit.json
```

Continue only after each step succeeds. Extraction uses the cache offline and rejects missing or corrupt referenced examples. Historical Gist resolution records the recovered revision. The audit validates extraction; it does not publish data.

## Engine integration

Add this checkout's absolute `plugin.json` path to the engine catalog's `plugins` array. From the engine environment:

```text
python -m adcs.plugins.cli aspose.tex.cpp --catalog <absolute-catalog.json> --workspace <absolute-plugin-checkout> --python <absolute-plugin-python> --source-kind both --timeout 300
```

After validation succeeds and persistence, retrieval and embedding services are configured, publish explicitly using the same command with `--source-kind docs --publish`, then `--source-kind apiref --publish`.

Source paths are relative to `--workspace`. The download/audit commands above assume the plugin checkout is the workspace. If a server wrapper uses its `engine` folder, place the repositories at `engine/sources/tex-documentation` and `engine/sources/tex-api-reference`, and prepare Gists from that documentation path into `plugins/tex-cpp/sources/gist-examples.json`. The standalone audit expects plugin-local sources.

## Repository layout

| Path | Purpose |
| --- | --- |
| `plugin.json` | Identity, source settings, worker command and retrieval profile |
| `worker.py` | Isolated extraction launcher |
| `src/adcs_tex_cpp/` | Parsing, normalization, chunking, symbols and Gist handling |
| `retrieval-profile.json` | TeX C++ retrieval configuration |
| `scripts/audit_sources.py` | Source-corpus extraction audit |
| `tests/` | Offline regression tests and fixtures |
| `docs/` | Extraction notes and historical verification records |

## Package installation

```sh
.venv/bin/python -m pip install .
```

The distribution is `adcs-tex-cpp-extractor`, the import namespace is `adcs_tex_cpp`, and the installed command is `adcs-tex-cpp-extract`. Alternatively, `python -I worker.py` reads one `adcs.extraction.v1` JSON request from stdin and emits one response. Use the source checkout for engine integration; the wheel does not include the manifest, retrieval profile, corpora, or Gist cache.

## Development

GitHub Actions runs the standalone regression suite with Python 3.12. GitLab CI is retained for mirrors. The parser and symbol normalization originated from the Words plugin; legacy synthetic fixture names are not claims about TeX SDK APIs. Official TeX fixtures test TeX content separately. The retrieval profile has no Words-specific ranking rules or namespace exclusions.

See [extraction notes](docs/extraction-notes.md). Historical records do not establish current ingestion. No ingestion or publication is performed by the unit tests.

## License and provenance

[MIT License](LICENSE). Derived from the [Words/C++ extraction plugin](https://github.com/aspose-words-mcp/cpp-plugin), with the original copyright notice preserved. Fixture origins and revisions are documented in [tests/fixtures/README.md](tests/fixtures/README.md). Downloaded documentation and examples retain their upstream terms and attribution.
