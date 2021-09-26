from setuptools_scm import get_version
from pathlib import Path
root_dir = Path().resolve()
code_dir= root_dir / 'src/e211_lib'
git_version = get_version(root=str(root_dir))
print(f"{git_version=}")
version_file = code_dir / 'VERSΙΟΝ.txt'
with open(version_file,'w') as outfile:
    outfile.write(git_version)
print((f"wrote new version number {git_version=}\n"
       f"into file {str(version_file.resolve())}"))

