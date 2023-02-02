import argparse
import os
import sys

parser = argparse.ArgumentParser(description='novel to txt', add_help=False)
parser.add_argument('-u', '--url', type=str, help='novel or manga url')
parser.add_argument('-e', '--episodes-url', type=str, default=None, help='url to fetch episodes')
parser.add_argument('-f', '--filename', type=str, default="out.txt", help='file name to save')
parser.add_argument('-a', '--api', type=str, default=None, help='API name')
parser.add_argument('--list-apis', type=None, default=None, help="Shows list of APIs")

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "--list-apis":
		print("Available APIs:\n")
		for api in os.listdir('./lib'):
			if api.endswith('.py'):
				print(api.split('.py')[0])
		exit(0)
	args = parser.parse_args()
	url = args.url
	if not url:
		parser.print_help()
		exit(0)
	try:
		Lib = getattr(__import__('lib.'+args.api, fromlist=[None]), args.api)() # what the fuck?
		file = open(args.filename, 'w')
		file.write(Lib.get_text(url))
		file.close()
	except Exception as a:
		print("An exception occured: " + str(a))
		exit(0)