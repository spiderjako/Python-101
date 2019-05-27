from bs4 import BeautifulSoup
import requests

def main():
    list_with_bg_sites = []
    r = requests.get('http://register.start.bg/')
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        list_with_bg_sites.append(link.get('href'))
    
    print(list_with_bg_sites)
        

        
if __name__ == '__main__':
    main()