from pathlib import Path
import sys
import shutil


def parse_args() -> (str, str):
    src_dir = sys.argv[1]

    dst_dir = "dist"
    if len(sys.argv) > 2:
        dst_dir = sys.argv[2]

    return (src_dir, dst_dir)


def copy_recursive(src: Path, dst: Path) -> None:
    try:  # handle exceptions related to directory/file access
        if src.is_dir():
            for child in src.iterdir():
                copy_recursive(child, dst/child.name)
            return
        # update destination path by adding extension directory
        dst_path = dst.parent/get_extension_dir_name(dst)/dst.name
        # makes all intermediate directories (recursive)
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst_path)  # copies file and metadata
    except PermissionError as e:
        print(f"Permission denied when accessing {src}: {e}")
        return
    except Exception as e:
        print(f"Error accessing {src}: {e}")
        return


def get_extension_dir_name(path: Path) -> str:
    ext = path.suffix.lstrip(".")
    # save file without extension (like .gitignore) to `other` dir
    return ext if ext != "" else "other"


def main():
    src_dir, dst_dir = parse_args()
    copy_recursive(Path(src_dir), Path(dst_dir))


if __name__ == "__main__":
    main()
