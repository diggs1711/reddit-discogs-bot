import sys

def create(submission, result):
    lowestPrice = result.prices['Lowest'].encode('utf-8')
    medianPrice = result.prices['Median'].encode('utf-8')
    highestPrice = result.prices['Highest'].encode('utf-8')
    
    song = ""
    prices = ""
    
    for track in result.tracklist:
        song += """{}. {} 
         | | | | """.format(track.position, track.title)
    
    prices += """*Lowest*: {}  *Highest*: {}  *Median*: {}""".format(lowestPrice, highestPrice, medianPrice)
    
    comment = """Artist | Title | Url | Price | Other tracks
               ---------|----------|---------- |---------- |----------
                     {} | {}       | {} | {} | {}""".format(result.artist.encode('utf-8'), result.title, result.url, prices, song)
                     
    try:
        print "Adding comment to " + submission.title
        #submission.add_comment(comment)
    except:
        print "Error: ", sys.exc_info()[0]
    
