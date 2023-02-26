import os


def get_html_files() -> list[str]:
    """Get all html files in the project."""
    root_dir = os.path.dirname(os.path.realpath(__file__))
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                try:
                    if f.readline().startswith("<!DOCTYPE html>"):
                        html_files.append(os.path.join(root, file))
                except UnicodeDecodeError:
                    pass
    return html_files
