import discogs_auth
import html_price_scraper as scraper

d = discogs_auth.authorize()

class ResultData(object):
	topResult = {}
	artist = ""
	tracklist = {}
	labels = {}
	title = ""
	rId = 0
	year = 0
	release = {}
	url = ""
	prices = {}
	
	def __init__ (self,topResult,artist,tracklist,labels, title, rId, year, release, url, prices):
		self.topResult = topResult
		self.artist = artist
		self.tracklist = tracklist
		self.labels = labels
		self.title = title
		self.rId = rId
		self.year = release
		self.url = url
		self.prices = prices

def retrieveData(results):
	topResult = results[0]
	artist = topResult.artists[0].name
	tracklist = topResult.tracklist
	labels = topResult.labels
	title = topResult.title
	rId = topResult.id
	year = topResult.year
	release = d.release(rId)
	tracklist = release.tracklist
	url = release.data['uri']
	prices = scraper.getPrice(url)
	
	return ResultData(topResult,artist,tracklist,labels, title, rId, year, release, url, prices)
	
def Search(s):
	return d.search(s, type='release')
	
    
    

