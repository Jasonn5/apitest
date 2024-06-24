import requests

url = "https://engage.metmuseum.org/api/productioneventapi/events?productionSeasonIds=728093&performancestartdate=2024-07-01T04:00:00.000Z&performanceenddate=2024-09-01T04:00:00.000Z&mos=69"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'es,es-419;q=0.9,es-BO;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Cookie': '_tt_enable_cookie=1; _ttp=rXUKc6hGjw0gmYQ0KCRP7hck6eV; __qca=P0-1408517380-1718669624395; QuantumMetricUserID=16331a686c58e39cb1af178bfb5ae36d; visid_incap_1661922=ZvdQWKm0Ry2kpJEfhdHH5Y7RcGYAAAAAQUIPAAAAAABPHST5qmOHekwHF8kBKm7f; _gid=GA1.2.880578771.1718799889; visid_incap_2349797=fPAuI7IPRViXfRQFtzLTbF7QcmYAAAAAQUIPAAAAAABBDXkDwUQhHA1pOBOyU79Q; _gcl_au=1.1.363802136.1718669622.707382706.1718800520.1718800520; personalisationGroupsPagesViewed=5192,1621; metNotificationBanner=visited; _parsely_session={%22sid%22:5%2C%22surl%22:%22https://www.metmuseum.org/es/art/collection?_gl=1*1gufp6t*_gcl_au*MzYzODAyMTM2LjE3MTg2Njk2MjIuNzA3MzgyNzA2LjE3MTg4MDA1MjAuMTcxODgwMDUyMA..*_ga*MTM0Nzg4MDMzNy4xNzE4NjY5NjIy*_ga_Y0W8DGNBTB*MTcxODgxMzI3OS40LjEuMTcxODgxMzI4NC4wLjAuMA..%22%2C%22sref%22:%22%22%2C%22sts%22:1718828266791%2C%22slts%22:1718818688959}; _parsely_visitor={%22id%22:%22pid=1571cc55-9dc8-404d-8087-28eab0ba4248%22%2C%22session_count%22:5%2C%22last_session_ts%22:1718828266791}; QuantumMetricSessionID=221a5da8b9d3d0619b068493c1e93d35; incap_ses_1454_1661922=Hae0IaGRChixZvmHXqUtFEg/c2YAAAAA3AVQEQpR5G5MHICt4BhR9w==; incap_ses_1693_1661922=v38aT2eVlllWxppdmr5+FwBBc2YAAAAAnTUscbcMZlfccVHxVzJKBA==; incap_ses_1453_1661922=uVrGPCrczxJ8SYnh3xcqFABBc2YAAAAA07aVvb/UP/uyEgVbVJjzdA==; incap_ses_1298_1661922=KjXVLEm+0m7eJp4fMmwDEgFBc2YAAAAAkB3ElhvkfftXTTAJagGcKQ==; incap_ses_1698_1661922=d0FKOc9pDRGURiGUE4KQFwFBc2YAAAAAyHe8wLtaq4YpaU4e94nhNw==; incap_ses_1452_1661922=Y64iOSGaywYrW089YYomFAFBc2YAAAAAWjcvWgjn3TOj2KndCd2ALg==; incap_ses_1241_1661922=g442fwRnpgLcY7fCAes4ERVBc2YAAAAAN0U8QvcwrhMyMVf2ejcf7A==; incap_ses_297_1661922=hh0EQmWEpmMkXYMnAigfBBVBc2YAAAAAuojn07TVc/TruiExIsyJcw==; incap_ses_1694_1661922=jjtORUMAyV43/R0BGUyCFxVBc2YAAAAAPxQQus4k6tHqdF8GQxmUlg==; incap_ses_1239_1661922=3D/8XYk/B0F3PUgmAtAxERVBc2YAAAAAjJfT01rA9g8fXP3aezbMKw==; incap_ses_1470_1661922=41T4CZrPNy25x3fUSH1mFBVBc2YAAAAAn3h0//u6utfol/zKn0Xdmw==; incap_ses_1471_1661922=NVR7HfZvJil8M0x5xwpqFDRCc2YAAAAA6KwqLfUrfqHUgkkGEzulFA==; _ga_N7V713MEFB=GS1.1.1718829690.2.0.1718829690.60.0.0; incap_ses_789_1661922=9HVPRZEgZXeNOB/XZhfzCnlDc2YAAAAAJVHcThSgPNMIjaXWIWMTCg==; incap_ses_787_1661922=ItKXPPg7DB1WhNXca/zrCqhDc2YAAAAAs4nOFXZGchKI+c2yJ748ag==; visid_incap_1662004=7/SSF2vBRz6FQyTp7BsndgxGc2YAAAAAQUIPAAAAAAAw3vUCoJeBDgtBKFMYzEDp; incap_ses_545_1662004=rU1ybE6MURtjej4atDqQBw1Gc2YAAAAANHHW5oHMBbfFdYZm2NXlOg==; incap_ses_1254_1661922=poUsFVa75EXBg/MhcBpnEWhIc2YAAAAA8kVyNbPJ76l49oUj+xR/9Q==; incap_ses_1474_1661922=HgqvMykClQbXdBZnQ7N0FGhIc2YAAAAAmctpp4I/ndFLVWB8dKKVFw==; aceSession=m/SbnuThLinRoYEzGCi15hHoe1cZFO7amtB5mzjqqnvrRoZuOeQtJJuuPPARdieWLJFltuXd966Q7DGcqJGSOr6Odabt6sWTwBZYzXkz3Fkb5u2L1gI5PL6JlGcFduH79G3zXLJktDIQ52uuLvkxhL0pxiKDaSaxctgMR/rRwg0mQg6v2eaDlvwA3uMR6DeK; nlbi_2349797=cx8zWG0RhD69UfnKzMiLaQAAAACqUFEA8xPbBLnutR/n8XAm; incap_ses_545_2349797=GI8OLpqF7zBksUAatDqQB2tIc2YAAAAAhWEzUfkqqgclnx1LHmKrJQ==; personalisationGroupsNumberOfVisits=2; personalisationGroupsNumberOfVisitsSessionStarted=1; incap_ses_8073_1661922=vqWaDcfQa2iTUL+I0Q4JcG1Ic2YAAAAAyvkMpD2FYu0LfJtEpd+7zQ==; incap_ses_1240_1661922=lzL/N3KrfVhHCXAgg101EW5Ic2YAAAAA2hnSVr8JSikbk4k8CY5YnQ==; reese84=3:c4wmSOHB+nHjkiLM9JgomA==:YCs9SAC0cUdMqVmkCPSy+fxJMfuEXSe/m8nVet7MpbauII1OLG6HhF0hK8GOlapyld56xdrazesIS0X+oqdUbwKgmk9gr8xjyqEJFmBafWvQ8HP3vE+SzcsZ1XvRP5mmDUh9L+/X/Oo2/dFFWIFG0Fpak9KsDtfbUeHnaWXSjMhSXPmHCqNFuBUSDOyCQKyGhzx4hJk/Z8cvm/K+TgSgaV7WMHvje/i8/77l/8qy/Bg/qAaBG+epUgiBLxb6NlPB7WyUWE1BLr45pIFzuyUDvinIox9OcPLSYu8p1LU2uyEkqXCMyR2RvehwDyHfQ0qXwzukRMICPp5haSfAwL+5f0esvkGONkNkrOKdl8LJbxWtyb/BxTsz5MGoryo0Z1ytL1ca+62jii3CAeUDTpFs2sqOFPMxtUyBrvIUa09gl7YnkG9JmONcSDpRQK2mLb3392r45VaPRgHUefEbSGAiKQ==:wnwbBwlNFt4WU0mF+cpRydsHXsLZXOky3uqzmeysguI=; incap_ses_1312_1661922=m0EUW9Q/yRCiLoYhHyk1EjlJc2YAAAAAYbAnGrbwCDQBYETrGCv0eg==; __RequestVerificationToken=ZDy1ZFI-ib7z4MqAVp3GlSTDZxlJr2fGCLsZBHdCjabPNYeGNeqzhuYnU6P3g7ktW0NyMc85Y3C4GczicTZnk6ikBgzUOyVG41vgUbWTL8o1; _ga=GA1.1.1347880337.1718669622; nlbi_2349797_2147483392=w68lFGMixwXnfTbyzMiLaQAAAABW9rqF+os1kfel53qshfWX; _ga_L6ZCHWX6DZ=GS1.1.1718831214.3.1.1718831423.0.0.0; _ga_Y0W8DGNBTB=GS1.1.1718828266.6.1.1718831425.0.0.0; _ga_80QRY9FZ67=GS1.1.1718831214.3.1.1718831425.0.0.0; aceSession=0yfWl2P/D7ORjF/KU+tXmZiIvhYnZwWyjN5OaI7oGe96pjYNY6g9MtrrzqUz+GvUAXXdK4AxlVTDQbY4yqkGWZ38Bh5lykaVBlVUTEzlvOf/D6nB1fgoEv3pdir3U9lyQXHZx//l/6Ci7dvCZN+Vnd/KRs9XiztURT2dAwzonqdg+EBJoiFENHNqZSMfI208; incap_ses_1479_1661922=2iKaViTk8ybI/LCevHaGFNc9c2YAAAAAwVBjHjlrua3KhkPy7X5cCg==; incap_ses_545_1662004=Ctf5UIX26C5n4D8atDqQB5RHc2YAAAAA++FsvaaFm7plNSetUWYd5A==; visid_incap_1662004=jCXY/8G9TkyGWB9ouS4kh5RHc2YAAAAAQUIPAAAAAABzBwVzDUoy/Mw2EoSWN+LG',
  'Referer': 'https://engage.metmuseum.org/admission/?promocode=52356',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)