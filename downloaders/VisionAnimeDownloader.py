from lxml import html
import requests

from interfaces.AnimeDownloaderInterface import AnimeDownloaderInterface
from utils.CustomErrors import NotFoundError
from utils import Constants

class VisionAnimeDownloader(AnimeDownloaderInterface):
    def get_tree(self, anime_url) -> html:
        anime_page = requests.get(anime_url)
        return html.fromstring(anime_page.content)
    
    def get_title(self, tree) -> str:
        search_result = tree.xpath(Constants.vision_title_xpath)
        if search_result:
            return search_result[0]
        
        raise NotFoundError("Title not found")
    
    def get_cover(self, tree) -> str:
        search_result = tree.xpath(Constants.saiko_cover_xpath)
        if search_result:
            return search_result[0].get('src')
        
        raise NotFoundError("Cover not found")
    
    def get_sinopse(self, tree) -> str:
        search_result = tree.xpath(Constants.vision_sonopse_xpath)
        if search_result:
            return search_result[0]
            
        raise NotFoundError("Sinopse not found")
    
    def get_tags(self, tree) -> list:
        result_search = tree.xpath(Constants.saiko_tags_xpath)
        if result_search:
            return result_search
        
        raise NotFoundError("Tags not found")