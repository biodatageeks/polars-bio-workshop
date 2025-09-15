# polars-bio-workshop


## Prerequisites

* Python >=3.9<3.14 (preferably 3.12+)
* [uv](https://docs.astral.sh/uv/) or another Python package/environment manager
* wget
* gsutil
* gzip and [bgzip](https://www.htslib.org/doc/bgzip.html), e.g. `brew install htslib`
* Linux/macOS/Windows (preferably Linux or macOS)
* Internet connection (for downloading files)


### Setup the environment

```bash
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

### Check installation

```bash
python -c "import polars_bio; print(polars_bio.__version__)"
```

### Run notebooks

```bash
uv run jupyter-lab notebook
```
