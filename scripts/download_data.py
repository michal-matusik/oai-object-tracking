"""Download and extract the datasets linked by the official task notebook."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

import gdown

FILES = {
    "train_data.zip": "1gEV52fT3luVkTU_Qf-aTd2hWj-7rYCpQ",
    "valid_data.zip": "1JDI4nWtIYlBp56QPbS3lsGyxZA9vHw5t",
}


def main(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for name, file_id in FILES.items():
        archive = output / name
        if not archive.exists():
            gdown.download(id=file_id, output=str(archive), quiet=False)
        with zipfile.ZipFile(archive) as source:
            source.extractall(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data"))
    main(parser.parse_args().output)
