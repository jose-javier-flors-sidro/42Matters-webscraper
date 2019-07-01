# Data extraction
# Most relevant metadata
class Utils:

    def parseData(self,data):
        result = []
        for app in data:
            appres = {}
            if 'title' in app:
                appres['title'] = app['title']
            else:
                appres['title'] = ''
            if 'price_numeric' in app:
                appres['price'] = app['price_numeric']
            else:
                appres['price_numeric'] = ''
            if 'permissions' in app:
                appres['permissions'] = self.getPermissions(app['permissions'])
            else:
                appres['permissions'] = ''
            if 'rating' in app:
                appres['rating'] = app['rating']
            else:
                appres['rating'] = ''
            if 'downloads' in app:
                appres['downloads'] = app['downloads']
            else:
                appres['downloads'] = ''
            if 'ratings_1' in app:
                appres['ratings'] = app['ratings_1'] + app['ratings_2'] + app['ratings_3'] + app['ratings_4'] + app[
                    'ratings_5']
            else:
                appres['ratings'] = 0
            if 'contains_ads' in app:
                appres['contains_ads'] = app['contains_ads']
            else:
                appres['contains_ads'] = ''
            if 'cat_key' in app:
                appres['cat_key'] = app['cat_key']
            else:
                appres['cat_key'] = ''
            if 'short_desc' in app:
                appres['short_desc'] = app['short_desc']
            else:
                appres['short_desc'] = ''
            if 'website' in app:
                appres['website'] = app['website']
            else:
                appres['website'] = ''
            if 'privacy_policy' in app:
                appres['privacy_policy'] = app['privacy_policy']
            else:
                appres['privacy_policy'] = ''
          
            result.append(appres)
        return result


    
    def getPermissions(self,data):
        perm = []
        for permission in data:
            perm.append(permission['id'].rpartition('.')[2])
        return perm
