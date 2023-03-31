import requests


def shorten_link(full_link, link_name):
    API_KEY = 'fca7b5faf76f58296a73193b2f4cfac66119e'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    payload = {'key': API_KEY, 'short': full_link, 'name':link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()
    
    print("")
    

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Title:', title)
        print('Title:', short_link)
    except:
        status: data['url']['status']
        print('Error Status:', status)
        
link = input('Enter a valid link?  ')
name = input("Enter a name for your link>  ")

shorten_link(link, name)




git config --global user.name "Rolexcodes"
git config --global user.email "olabodeolaleye232@gmail"
