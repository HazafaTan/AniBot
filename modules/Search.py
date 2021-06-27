import discord 

async def queryAnime():
    return  ''' query ($name: String) { # Define which variables will be used in the query (id)
    Media (search: $name, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
        english
        native
        }
        coverImage {
        extraLarge
        large
        medium
        color
        }
        description(asHtml: false)
        bannerImage
        averageScore
        seasonYear
        season
        popularity
        genres
        status
    }
    }
    '''