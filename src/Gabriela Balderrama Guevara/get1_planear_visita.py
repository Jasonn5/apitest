import requests

url = "https://www.metmuseum.org/es/plan-your-visit/met-cloisters"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es,es-419;q=0.9,es-BO;q=0.8,en;q=0.7',
  'cookie': 'NEXT_LOCALE=es; _tt_enable_cookie=1; _ttp=rXUKc6hGjw0gmYQ0KCRP7hck6eV; __qca=P0-1408517380-1718669624395; QuantumMetricUserID=16331a686c58e39cb1af178bfb5ae36d; visid_incap_1661922=ZvdQWKm0Ry2kpJEfhdHH5Y7RcGYAAAAAQUIPAAAAAABPHST5qmOHekwHF8kBKm7f; _gid=GA1.2.880578771.1718799889; visid_incap_2349797=fPAuI7IPRViXfRQFtzLTbF7QcmYAAAAAQUIPAAAAAABBDXkDwUQhHA1pOBOyU79Q; _parsely_session={%22sid%22:5%2C%22surl%22:%22https://www.metmuseum.org/es/art/collection?_gl=1*1gufp6t*_gcl_au*MzYzODAyMTM2LjE3MTg2Njk2MjIuNzA3MzgyNzA2LjE3MTg4MDA1MjAuMTcxODgwMDUyMA..*_ga*MTM0Nzg4MDMzNy4xNzE4NjY5NjIy*_ga_Y0W8DGNBTB*MTcxODgxMzI3OS40LjEuMTcxODgxMzI4NC4wLjAuMA..%22%2C%22sref%22:%22%22%2C%22sts%22:1718828266791%2C%22slts%22:1718818688959}; _parsely_visitor={%22id%22:%22pid=1571cc55-9dc8-404d-8087-28eab0ba4248%22%2C%22session_count%22:5%2C%22last_session_ts%22:1718828266791}; QuantumMetricSessionID=221a5da8b9d3d0619b068493c1e93d35; shell#lang=en; __RequestVerificationToken=RneuBxNMapMKvPaDLkQNfn_h8iJ_MgEok8Ek_q3PTfvl4v-IB4XkD8hdMFmvSqVYf7fXujqwsTAbffs0dReROr6HTvQ1; website#lang=es; incap_ses_1452_1661922=Y64iOSGaywYrW089YYomFAFBc2YAAAAAWjcvWgjn3TOj2KndCd2ALg==; _ga_N7V713MEFB=GS1.1.1718829690.2.0.1718829690.60.0.0; incap_ses_789_1661922=9HVPRZEgZXeNOB/XZhfzCnlDc2YAAAAAJVHcThSgPNMIjaXWIWMTCg==; visid_incap_1662004=7/SSF2vBRz6FQyTp7BsndgxGc2YAAAAAQUIPAAAAAAAw3vUCoJeBDgtBKFMYzEDp; incap_ses_545_1662004=rU1ybE6MURtjej4atDqQBw1Gc2YAAAAANHHW5oHMBbfFdYZm2NXlOg==; nlbi_2349797=cx8zWG0RhD69UfnKzMiLaQAAAACqUFEA8xPbBLnutR/n8XAm; incap_ses_545_2349797=GI8OLpqF7zBksUAatDqQB2tIc2YAAAAAhWEzUfkqqgclnx1LHmKrJQ==; aceSession=vISqwK3HizMbE/dFokxoS/FKE4xbf6QGXVJZdoAjqRmK7cS9fH/RMpT+thw07FAThA3XwAjmolfkbGJmilHdRLARpDccGysst4LJyksjoZMrgFzoWCsmDr0LFQ8dQZPVC5GeyFcVKMVaO/olZrQEzbIu+cY0ZpE911bfxIZONYMB0GnTsM/3cHaj6SYRmb8I; incap_ses_1471_1661922=1nF+DPHhgwM+xlV5xwpqFE5Mc2YAAAAAL2K1703FiMZEcsRdxh0+Ew==; incap_ses_1695_1661922=m0naR1x4mSTMLYSintmFF1VNc2YAAAAAA5i5OlEo6DzhWgWXVw6hNQ==; nlbi_2349797_2147483392=q6FABZlT91ubrNDSzMiLaQAAAAAECrIuJSFjNOTNmr7QR8CV; _gcl_au=1.1.363802136.1718669622.1758972157.1718832374.1718832489; _ga_L6ZCHWX6DZ=GS1.1.1718831214.3.1.1718832832.0.0.0; _ga_80QRY9FZ67=GS1.1.1718831214.3.1.1718832832.0.0.0; incap_ses_1698_1661922=a9iAC2SrJDULGC6UE4KQF8dOc2YAAAAADOvHnhgmQ+a0MKEFXnNB/A==; incap_ses_1694_1661922=amJuNn7yOXLbzCoBGUyCF89Oc2YAAAAAUtNvzGxWd2mtNBeXUjONqA==; incap_ses_1455_1661922=VzsRcaO88UPt/g8r3TIxFM9Oc2YAAAAAYajdvAe1U1aO51JUBaHWYg==; incap_ses_1474_1661922=ZTs2RVHnxzfwpBxnQ7N0FM5Oc2YAAAAAiWfPJ12o694i4WMbZxJx/g==; incap_ses_787_1661922=WwPlE6xRoymOft7ca/zrCs9Oc2YAAAAAP18uwwwlCpqmtNZIObxJvw==; incap_ses_1254_1661922=43E5GwE5c2CV+/ghcBpnEc9Oc2YAAAAAELIzy8kWiUv7T4DsMwE1fw==; incap_ses_1241_1661922=/tYsXe+RbyYOeMLCAes4EdBOc2YAAAAAAjwXaytcnUsUOXb+F9XG9w==; incap_ses_1312_1661922=ih/TQAhlBDdGYYohHyk1EtBOc2YAAAAANerGP/nlUvJPbcEVSPk9fQ==; metNotificationBanner=visited; incap_ses_1476_1661922=0WQJUNeZckn3LFayQM57FCtPc2YAAAAAPfML1RKErTPGqs37sCiJPQ==; incap_ses_1697_1661922=UqD9OfzppC4uvXzvlPSMFytPc2YAAAAAZ/2BcM07LGmEkuqoFFl9VA==; incap_ses_1454_1661922=4xNtAG5BhXvjwQeIXqUtFCxPc2YAAAAA1Lmj6A+1W7No3gvQoJ8yxQ==; _hjSession_3360071=eyJpZCI6IjhhODhjNDQ4LTMzNDktNGI5Yi04MTkxLWNlYjMxYWI4ODRlOSIsImMiOjE3MTg4MzI5NDQzNTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; incap_ses_1477_1661922=9YtcUFC8k2OxGT1Vv1t/FERPc2YAAAAAq+ynI+A4xWp+KaCF9rKaXg==; _hjSessionUser_3360071=eyJpZCI6IjI5ZTcyMjg2LWM3NmUtNTRlZS1hMzdlLWUxOTU1YzgwZDEyMCIsImNyZWF0ZWQiOjE3MTg4MzI5NDQzNTcsImV4aXN0aW5nIjp0cnVlfQ==; incap_ses_1239_1661922=/5OLGANdyAEuHlcmAtAxEY9Pc2YAAAAAdkdCeA7xUd4kkolUcxu2+g==; incap_ses_1696_1661922=XrNnJFXlRErUMgxLFmeJF49Pc2YAAAAAbJMSaH0NEiqT3bKKMlV1UQ==; incap_ses_1693_1661922=DIvbY2MCfhEbXKldmr5+F5BPc2YAAAAA+fhu6wMi33wSP87if7KvZA==; incap_ses_1470_1661922=Wph8MPCwLioL14TUSH1mFJFPc2YAAAAA/O5JtvR9ShdHe/btcmHvJQ==; incap_ses_1479_1661922=hTcKUOOf4wqnPMKevHaGFJFPc2YAAAAAZtojIFK4K0f043UiJYTsSQ==; incap_ses_1240_1661922=syAKLq+hSHsDgHYgg101EZxPc2YAAAAA2ajhmq826QFwz3tRTSPszg==; incap_ses_1478_1661922=hvjcX7XISUqy9TL8PemCFKFPc2YAAAAATzwrDB0X3n2Uq6abnG1g2w==; incap_ses_297_1661922=Uiq0UGg3OF4w4I4nAigfBLhPc2YAAAAAc+TsZCwaEujBtTlxTQ6d9Q==; incap_ses_784_1661922=dbr+aNmx/icetN/r9lPhCrhPc2YAAAAAVyk8fhSEiSHadmCbyiXpzQ==; incap_ses_1453_1661922=SupAMeGnEDmzL5Th3xcqFNFPc2YAAAAAm/TtK26Pz1ysXNkVkYCLbg==; incap_ses_786_1661922=k9+yJlC1c14YA/Q37W7oCtJPc2YAAAAA9rO7sCkDFHwqdc8516suqw==; incap_ses_8073_1661922=wANaNYqEXURItMWI0Q4JcNJPc2YAAAAAANYgkLU0A8U8sv1byiKtyA==; incap_ses_1298_1661922=Jjb1FHnfSULCz6ofMmwDEtNPc2YAAAAAkjao1gyu3i13OfK8wuQCJQ==; _gat_UA-72292701-1=1; visid_incap_1661977=KnJS2DmaSca5n4t1nc1ObVFQc2YAAAAAQUIPAAAAAACNA5MHaUC8VPJWdYmzaDzD; _ga_Y0W8DGNBTB=GS1.1.1718828266.6.1.1718833233.0.0.0; _ga=GA1.2.1347880337.1718669622; incap_ses_545_1661977=d810VfxdNHuzFkgatDqQB1FQc2YAAAAAKAi+GPMPHDkbDL5jNy1s1w==; aceSession=0yfWl2P/D7ORjF/KU+tXmZiIvhYnZwWyjN5OaI7oGe96pjYNY6g9MtrrzqUz+GvUAXXdK4AxlVTDQbY4yqkGWZ38Bh5lykaVBlVUTEzlvOf/D6nB1fgoEv3pdir3U9lyQXHZx//l/6Ci7dvCZN+Vnd/KRs9XiztURT2dAwzonqdg+EBJoiFENHNqZSMfI208; incap_ses_1479_1661922=2iKaViTk8ybI/LCevHaGFNc9c2YAAAAAwVBjHjlrua3KhkPy7X5cCg==; incap_ses_545_1662004=Ctf5UIX26C5n4D8atDqQB5RHc2YAAAAA++FsvaaFm7plNSetUWYd5A==; visid_incap_1662004=jCXY/8G9TkyGWB9ouS4kh5RHc2YAAAAAQUIPAAAAAABzBwVzDUoy/Mw2EoSWN+LG; __RequestVerificationToken=Vb6KbryQyOFp6_6_5mvb7XBGaY7yYBjlDcxSi41ojXLfsDJViQD_sDA1pId4E72hT-GGFn1Z3BpqzInyhqaHAcxy5yU1; shell#lang=en',
  'if-none-match': 'W/"mda31h9xb4yiw"',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22q%5C%22%3A%5C%22art%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3Fq%3Dart%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?q=art',
  'rsc': '1',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)