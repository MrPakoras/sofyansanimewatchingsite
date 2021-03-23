from PIL import Image as i
import math, os, time, re, colorama
from colorama import Fore
colorama.init()
from git import Repo 

### Edit HTML

f = open('index.html','r+')
fr = f.read()

u = input('>> Enter episode number, date:   ')

def fwrite(text):
	f.seek(0)
	f.write(text)
	f.truncate()

try:
	ul = u.split(',')

	if len(ul) == 2:
		new = re.sub(r"var start_date = new Date\('.*'\)\.getTime\(\); \/\/ Edit this", f"var start_date = new Date('{ul[1]}').getTime(); // Edit this", fr)
		fwrite(new)
		print(f'{Fore.GREEN}>> Updated HTML - Ep: {ul[0]} | Date: {ul[1]}')
	elif len(ul) == 1:
		dt = time.strftime('%b %d %Y')
		new = re.sub(r"var start_date = new Date\('.*'\)\.getTime\(\); \/\/ Edit this", f"var start_date = new Date('{dt}').getTime(); // Edit this", fr)
		fwrite(new)		
		print(f'{Fore.GREEN}Updated HTML - Ep: {ul[0]} | Date: {dt}')

	new = re.sub(r'var eps_watched = [0-9]*; \/\/ Edit this', f'var eps_watched = {ul[0]}; // Edit this', new)
	fwrite(new)
except:
	print(error)

#f.truncate()

f.close()



### Creating Progress Bar

eps = int(ul[0]) # Episdes watched

file = open('ep.txt','r') # Text file with current episode number
ce = int(file.read()) # Currnt episode
file.close()

print(f'{Fore.MAGENTA}Total Episodes: {ce}')
perc = eps/ce # Fraction completed
print(f'{Fore.MAGENTA}Percentage Complete: {round(perc*100, 3)}%')

mode = 'RGB'
twid, thei = 2000, 100

bkg = i.new(mode, (twid, thei)) # Background
bar = i.new(mode, (math.floor((twid-20)*perc), thei-20), (220,0,41))# Progress bar

bkg.paste(bar, (10,10))

bkg.save('progress_bar.png')
#bkg.show()

# filepath = 'C:/Users/Anas/AppData/Local/GitHubDesktop/GitHubDesktop.exe'
# os.startfile(filepath)

## https://stackoverflow.com/questions/41836988/git-push-via-gitpython

PATH_OF_GIT_REPO = "H:/Anas' Stuff/HTML-CSS-JS/HTML/PAShA/.git"  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Updated Progress Bar'

print(f'{Fore.CYAN}Pushing to Github...')

try:
	repo = Repo(PATH_OF_GIT_REPO)
	repo.git.add(update=True)
	repo.index.commit(COMMIT_MESSAGE)
	origin = repo.remote(name='origin')
	origin.push()
	print(f'{Fore.GREEN}Done.')
except:
	print(f'{Fore.RED}Some error occured while pushing the code')