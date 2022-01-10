from typing import Type

from interfaces.AnimeDownloaderInterface import AnimeDownloaderInterface
from utils.CustomErrors import AlreadyExistsError

class Dowloader():
    def __init__(self, anime_url) -> None:
        self.anime_url = anime_url
        
    def download(self, anime_dowloader: Type[AnimeDownloaderInterface]):
        tree = anime_dowloader.get_tree(self.anime_url)
        anime_title = anime_dowloader.get_title(tree)
        cover_url = anime_dowloader.get_cover(tree)
        sinopse = anime_dowloader.get_sinopse(tree)
        tags = anime_dowloader.get_tags(tree)
        episodes_url = anime_dowloader.get_episodes_url(tree)
        anime_dowloader.create_folder(anime_title)
        anime_dowloader.download_cover(anime_title, cover_url)
        episodes_informations = anime_dowloader.get_episodes_informations(episodes_url)
        
        for episode_information in episodes_informations:
            try:
                anime_dowloader.download_episode(anime_title, episode_information)
            
            except AlreadyExistsError as ex:
                print("\033[1;32;40m {}".format(ex))
                
            except Exception as ex:
                print("\033[1;31;40m {}".format(ex))
