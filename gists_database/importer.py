import requests

query = '''INSERT INTO gists (
                        github_id, html_url, git_pull_url, git_push_url, 
                        commits_url, forks_url, public, created_at, updated_at, 
                        comments, comments_url
                        )
                VALUES (                  
                        :github_id, :html_url, :git_pull_url, :git_push_url, 
                        :commits_url, :forks_url, :public, :created_at, 
                        :updated_at, :comments, :comments_url
                        );'''
                        
URL = 'https://api.github.com/users/{username}/gists'


def import_gists_to_database(db, username, commit=True):
    
    response = requests.get(URL.format(username=username))

    response.raise_for_status()
    gist_data = response.json()

    for gist in gist_data:
        gist_params = {
            "github_id": gist['id'],
            "html_url": gist['html_url'],
            "git_pull_url": gist['git_pull_url'],
            "git_push_url": gist['git_push_url'],
            "commits_url": gist['commits_url'],
            "forks_url": gist['forks_url'],
            "public": gist['public'],
            "created_at": gist['created_at'],
            "updated_at": gist['updated_at'],
            "comments": gist['comments'],
            "comments_url": gist['comments_url'],
        }
        
        db.execute(query, gist_params)
        
        if commit:
            db.commit()