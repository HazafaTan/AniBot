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

async def queryChar():
    return '''query ($id: Int, $search: String) {
  Character(id: $id, search: $search) {
    id
    age
    gender
    description
    media {
      edges {
        id
        node {
          id
          bannerImage
        }
      }
    }
    dateOfBirth {
      year
      month
      day
    }
    name {
      full
    }
    image {
      large
    }
  }
}
    '''
