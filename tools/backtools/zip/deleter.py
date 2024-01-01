from os import rmdir, remove

def removechain(src: dict):
	for i in src["file"]:
		remove(i)
	for i in src["dir"]:
		rmdir(i)

def removefixed(folder: str):
	remove(f'./tools/backtools/zip/{folder}-dumpfile.txt')
	remove(f'./tools/backtools/zip/{folder}-dumpdir.txt')

def removeall(src: dict, folder: str) -> None:
	removechain(src)
	removefixed(folder)
