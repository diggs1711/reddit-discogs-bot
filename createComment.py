import sys

def create(submission, result):
    lowestPrice = result.prices['Lowest'].encode('utf-8')
    medianPrice = result.prices['Median'].encode('utf-8')
    highestPrice = result.prices['Highest'].encode('utf-8')
    
    song = ""
    prices = ""
    
    for track in result.tracklist:
        print track.fetch
        print track.data
        song += """{}. {} 
         | | | | """.format(track.position, track.title)
    
    prices += """*Lowest*: {}  *Highest*: {}  *Median*: {}""".format(lowestPrice, highestPrice, medianPrice)
    
    comment = """Artist | Title | Url | Price | Other tracks
               ---------|----------|---------- |---------- |----------
                     {} | {}       | {} | {} | {}""".format(result.artist, result.title, result.url, prices, song)
    try:
        submission.add_comment(comment)
    except:
        print "Error: ", sys.exc_info()[0]
    
