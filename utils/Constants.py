
block_size = 1024 * 1024

saiko_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 
    'accept': '*/*', 
    'Referer': 'https://download.saikoanimes.net/secure/uploads/{}?shareable_link={}', 
    'cookie': 'theme=light; _gid=GA1.2.1558720664.1641603094; SaikÃ´ Direct_cookie_notice=1; XSRF-TOKEN=eyJpdiI6IjdaNXNGbUlEclg0TDVHcDB6VU9wZmc9PSIsInZhbHVlIjoiMFRYaEtaZkVqV09abE5vSnVCWGlDandheWF6S2g4TjRQVW5TbmNtT3UyY296L1czUHJ2V0JNK3JiemgyaDUwU1h3Mm1QQ0o1UWpiT0Z0eE5WNWhieVpkSG15Q0NabzhyL3VRN2xXWGVPQ1FCdWxHa1dHb2NCOVA4MDk0RGZDN3QiLCJtYWMiOiIwODMyN2E2ZWY3ZGU3YWUzNjYwZDUyNGZiMTMxNDZhMDkzNjgwOGFmY2MxM2RjNTNjMDk0NDQxNDhmYTdmNzM2IiwidGFnIjoiIn0%3D; saiko_direct_session=eyJpdiI6IldZTkNpVlpOWTFBWVpHY3ZPY0xNTEE9PSIsInZhbHVlIjoiSGd2SlhiVlpkNXBnaW51RnhDYW16T3ViZ0o4UHJDblkyWTRGamErRkpyZWN4eWRzeUxocmZIS1JEY2JOTUIvU25hV3lQMmFUdTliaEtZOVZPV0lmanp5c1drM21KSDd2MFpkWjcwdjZwTWx5ckt4VkViSEk5VkNCTDMvUkJTaW0iLCJtYWMiOiIwZjMwODk2NGFhN2NhMDAyYjVhODQ5ZmY5YTkyYjBhYzJjYzkwNjM2MGNiMjQxZjNiZTU3NGNiY2RmNTMzYjJmIiwidGFnIjoiIn0%3D; _ga_SGJM7RJB0N=GS1.1.1641693412.138.0.1641693412.0; _ga=GA1.2.457857542.1503198075; crisp-client%2Fsession%2F81f2f730-82ea-42ac-ac28-6061d2d4eca1=session_bd7d2e65-5026-4412-bace-0cbb32f7812e'
}

saiko_episodes_infos_url = 'https://download.saikoanimes.net/secure/drive/shareable-links/{}?withEntries=true'

saiko_episode_download_url = 'https://download.saikoanimes.net/secure/uploads/{}?shareable_link={}'

saiko_title_xpath = '//*[@id="main"]/section/div/div[1]/div[2]/div[1]/text()'

saiko_cover_xpath = '//*[@id="main"]/section/div/div[1]/div[1]/img'

saiko_sonopse_xpath_1 = '//*[@id="box"]/text()'

saiko_sonopse_xpath_2 = '//*[@id="main"]/section/div/div[1]/div[2]/div[4]/div/div[2]/div[2]/text()'

saiko_tags_xpath = '//*[@id="main"]/section/div/div[1]/div[2]/div[4]/div/div[1]/div/div/text()'

saiko_episodes_url_xpath = '//*[@id="50"]/div/a'

season_animes = [
    # 'https://saikoanimes.net/anime/world-trigger-3rd-season/',
    # 'https://saikoanimes.net/anime/kaijin-kaihatsu-bu-no-kuroitsu-san/',
    # 'https://saikoanimes.net/anime/karakai-jouzu-no-takagi-san-3/',
    # 'https://saikoanimes.net/anime/akebi-chan-no-sailor-fuku/',
    # 'https://saikoanimes.net/anime/sono-bisque-doll-wa-koi-wo-suru/',
    # 'https://saikoanimes.net/anime/shikkaku-mon-no-saikyou-kenja/',
    # 'https://saikoanimes.net/anime/shuumatsu-no-harem/',
    # 'https://saikoanimes.net/anime/cue/',
    # 'https://saikoanimes.net/anime/dolls-frontline/',
    'https://saikoanimes.net/anime/slow-loop/'
    # 'https://saikoanimes.net/anime/platinum-end/',
    # 'https://saikoanimes.net/anime/ousama-ranking-dublado/',
    # 'https://saikoanimes.net/anime/tokyo-24-ku/',
    # 'https://saikoanimes.net/anime/leadale-no-daichi-nite/',
    # 'https://saikoanimes.net/anime/orient/',
    # 'https://saikoanimes.net/anime/kimetsu-no-yaiba-yuukaku-hen/'
    # 'https://saikoanimes.net/anime/boruto-naruto-next-generations/',
    # 'https://saikoanimes.net/anime/shingeki-no-kyojin-the-final-season/'
]

regex_remove_special_characters = '[^A-Za-z0-9]'

regex_remove_last_sopace_and_tabulation = '[ \t]+$'

vision_title_xpath = '//*[@id="ani_detail"]/div/div/div[2]/div[2]/h2/text()'

vision_cover_xpath = '//*[@id="ani_detail"]/div/div/div[2]/div[1]/div/img'

vision_sonopse_xpath = '//*[@id="ani_detail"]/div/div/div[2]/div[2]/div[5]/div/text()'

vision_tags_xpath = '//*[@id="ani_detail"]/div/div/div[2]/div[3]/div[1]/div[9]/a/text()'

download_folder = './downloads'