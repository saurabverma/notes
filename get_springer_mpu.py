# During COVID-19 period, a lot of Springer books are available for free.
# Details are mentioned here: https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4
# This python3 program helps download all of the books in parallel.
# User may update 'num_thread' variable to tune number of parallel downloads.

import os
import requests
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool, TimeoutError
from signal import signal, SIGINT

shutdown = False
num_thread = 3



def signal_handler(sig, frame):
	global shutdown
	shutdown = True



def download_book(input_values):
	url, title, author, pk_name = input_values

	r = requests.get(url)
	new_url = r.url

	new_url = new_url.replace('/book/','/content/pdf/')
	new_url = new_url.replace('%2F','/')
	new_url = new_url + '.pdf'

	final = title.replace(',','-').replace('.','').replace('/',' ') + '__' + author.replace(', ','+').replace('.','').replace('/',' ') + '.pdf'

	dir = os.path.join(cwd,pk_name)
	if not os.path.exists(dir):
		os.mkdir(dir)

	if not shutdown:
		myfile = requests.get(new_url, allow_redirects=True)
		open(os.path.join(dir,final), 'wb').write(myfile.content)



if __name__=='__main__':

	signal(SIGINT, signal_handler)
	print("Press 'Ctrl+C' to cancel current downloads, use multiple times to exit.\n")

	cwd = os.getcwd()
	books = pd.read_excel(os.path.join(cwd,'Free+English+textbooks.xlsx'))
	values = books[['OpenURL', 'Book Title', 'Author', 'English Package Name']].values

	pool = Pool(processes=num_thread)

	for _ in tqdm(pool.imap_unordered(download_book, values), total=len(values)):
		pass
