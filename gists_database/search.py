from .models import Gist

def search_gists(db_connection, **kwargs):
    query = 'SELECT * FROM gists'
    result = []
    params = {}
    
    for name, value in kwargs.items():
        if name == 'created_at':
            git_name = name
            query += ' WHERE datetime({git_name}) = datetime(:date) AND'.format(
                                                                    git_name)
            params.update({'date' : value})
       
        else:
            git_name = name
            query += ' WHERE {git_name} = :value AND'.format(git_name)
            params.update({'value' : value})
    
    
    query = query.rstrip(' AND')
    cursor = db_connection.execute(query, params)
        
    for gist in cursor:
        result.append(Gist(gist))
    
    return result