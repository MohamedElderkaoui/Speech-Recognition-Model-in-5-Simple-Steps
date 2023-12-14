from pathlib import Path
filesize = Path('somefile.txt').stat().st_size
print(filesize)