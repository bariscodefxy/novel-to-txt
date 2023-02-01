import argparse
import lib.mangabilgini as lib

parser = argparse.ArgumentParser(description='novel to txt')
parser.add_argument('-u', '--url', help='novel or manga url')
parser.add_argument('-f', '--filename', help='file name to save')

if __name__ == "__main__":
	args = parser.parse_args()
	url = args.url
	Lib = lib.Mangabilgini()
	file = open(args.filename, 'w')
	file.write(Lib.get_text(url).replace('\n', '\n\n\n'))
	file.close()