from __future__ import annotations

import torch


def hello_cuda() -> None:
    print(f"torch={torch.__version__}")
    print(f"cuda_available={torch.cuda.is_available()}")

    try:
        value = torch.tensor([1.0], device="cuda")
        print(f"hello_cuda={value.item()}")
        print(f"device={value.device}")
    except Exception as exc:
        print(f"cuda_error={type(exc).__name__}: {exc}")
        raise


def main() -> None:
    hello_cuda()


if __name__ == "__main__":
    main()
