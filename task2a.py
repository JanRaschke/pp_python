def download_web_page(url: str) -> str:  # 2 Punkte
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    content_div = soup.find('div', id='content')
    
    if content_div:
        return content_div.get_text(separator="\n")
    return ""

def save_file(filepath: str, content: str) -> None:  # 1 Punkt
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

text = download_web_page(url)
save_file(filepath, text)

if os.path.exists(filepath):
    print(f"Website {url} was saved to \"{filepath}\"")