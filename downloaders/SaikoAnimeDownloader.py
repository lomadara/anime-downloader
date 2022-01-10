import os
from lxml import html
import requests
import re

from interfaces.AnimeDownloaderInterface import AnimeDownloaderInterface
from utils import Constants
from utils.CustomErrors import AlreadyExistsError, NotFoundError

class SaikoAnimeDownloader(AnimeDownloaderInterface):
    def get_tree(self, anime_url) -> html:
        anime_page = requests.get(anime_url)
        return html.fromstring(anime_page.content)
    
    def get_title(self, tree) -> str:
        search_result = tree.xpath(Constants.saiko_title_xpath)
        if search_result:
            title = search_result[0]
            title = re.sub(Constants.regex_remove_last_sopace_and_tabulation, '', title)
            title = re.sub(Constants.regex_remove_special_characters, '-', title)
            
            return title
        
        raise NotFoundError("Title not found")
    
    def get_cover(self, tree) -> str:
        search_result = tree.xpath(Constants.saiko_cover_xpath)
        if search_result:
            return search_result[0].get('src')
        
        raise NotFoundError("Cover not found")
        
    def get_sinopse(self, tree) -> str:
        search_result = tree.xpath(Constants.saiko_sonopse_xpath_1)
        if not search_result:
            search_result = tree.xpath(Constants.saiko_sonopse_xpath_2)
        
        if search_result:
            return search_result[0]
            
        raise NotFoundError("Sinopse not found")
    
    def get_tags(self, tree) -> list:
        result_search = tree.xpath(Constants.saiko_tags_xpath)
        if result_search:
            return result_search
        
        raise NotFoundError("Tags not found")
    
    def get_episodes_url(self, tree) -> str:
        result_search = tree.xpath(Constants.saiko_episodes_url_xpath)
        if result_search:
            return result_search[0].get('href')
        
        raise NotFoundError("Episodes url not found")
    
    def create_folder(self, anime_title):
        if not os.path.exists('./assistindo/{}'.format(anime_title)):
            os.mkdir('./assistindo/{}'.format(anime_title))
    
    def download_cover(self, anime_title, cover_url) -> None:
        cover_response = requests.get(cover_url)
        with open("./assistindo/{}/{}".format(anime_title, "cover.jpg"), 'wb') as file:
            for data in cover_response.iter_content(Constants.block_size):
                file.write(data)
    
    def get_items_informations(self, hash):
        return requests.get(Constants.saiko_episodes_infos_url.format(hash)).json()
    
    def map_episodes_informations(self, anime_id, item, maped_episodes_information):
        maped_episodes_information.append({
            "anime_id": anime_id,
            "episode_id": item.get('id'),
            "episode_name": item.get('name')
        })
        
        return maped_episodes_information
        
    def get_episodes_informations(self, episodes_url) -> None:
        anime_hash = episodes_url.split('/')[5]
        items_informations = self.get_items_informations(anime_hash)
        anime_id = items_informations.get('link').get('id')
        items = items_informations.get('folderChildren').get('data')
        maped_episodes_information = []
        for item in items:
            if item.get('type') == 'folder':
                episodes_informations = self.get_items_informations(anime_hash + ':' + item.get('hash'))
                episodes = episodes_informations.get('folderChildren').get('data')
                for episode in episodes:
                    maped_episodes_information = self.map_episodes_informations(anime_id, episode, maped_episodes_information)
            else:
                maped_episodes_information = self.map_episodes_informations(anime_id, item, maped_episodes_information)
            
        return maped_episodes_information
    
    def download_episode(self, anime_title, episode_information) -> None:
        episode_id = episode_information.get('episode_id')
        anime_id = episode_information.get('anime_id')
        episode_name = episode_information.get('episode_name')
        
        headers = Constants.saiko_headers
        headers['Referer'] = headers['Referer'].format(episode_id, anime_id)
        
        if not os.path.exists("./assistindo/{}/{}".format(anime_title, episode_name)):
            video_response = requests.get(Constants.saiko_episode_download_url.format(episode_id, anime_id),headers= headers, stream=True)
            total_length_in_bytes = 0

            with open("./assistindo/{}/{}".format(anime_title, episode_name), 'wb') as file:
                while True:
                    for data in video_response.iter_content(Constants.block_size):
                        file.write(data)
                        total_length_in_bytes += Constants.block_size
                        os.system('cls')
                        print("\033[1;33;40m {} total length : {} GB".format(episode_name, round(total_length_in_bytes / 1073741824, 3)))
            
        else:
            raise AlreadyExistsError("{} already exists".format(episode_name))