# CUDA Dev Container

This is a VSCode dev container configuration for CUDA development and my personal use.

## Usage

1. `Reopen in Container` from the `Open a Remote Window` menu in VSCode bottom left corner.
2. run `uv sync` to install the python dependencies if python is needed for your project.

## Note

### python environment

- `python` environment is in `/home/vscode/.venv`.
- python dependencies are cached in two volumes: `uv-cache` and `uv-python`.

### git setup

if you fail to push to git from the container, see [Sharing Git credentials with your container](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials) for details about git credential sharing between host and container.

## Useful Resource

- [CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/)
- [NVIDIA cuda-samples repo](https://github.com/NVIDIA/cuda-samples)
