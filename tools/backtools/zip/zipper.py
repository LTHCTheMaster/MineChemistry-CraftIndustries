import zipfile
from os import path as pt, mkdir
from .copypaster import copypaste
from .deleter import removeall
import threading

BACKPATH = './'

class ZipppingThread (threading.Thread):
	def __init__(self, threadID, name, path: str, zip_name: str):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		#####
		self.path: str = path
		self.zip_name: str = zip_name
	def run(self):
		dump = copypaste(BACKPATH + self.path)
		compress(zip_name = self.zip_name + '.zip', src = dump["file"])
		removeall(dump, self.path)

def compress(zip_name: str, src: list[str]):
	if not pt.exists('zip'): mkdir('zip')
	file = zipfile.ZipFile('zip/' + zip_name, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9)
	for i in src:
		file.write(i, i[len('/'.join(i.split('/')[0:5])):])
	file.close()

def runZip() -> None:
	datapackThread = ZipppingThread(1, "Thread-Datapack", 'Datapack', 'DatapackZip')
	resourcepackThread = ZipppingThread(2, "Thread-Resourcepack", 'Resourcepack', 'ResourcepackZip')

	datapackThread.start()
	resourcepackThread.start()
