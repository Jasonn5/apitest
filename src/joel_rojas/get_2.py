import requests

url = "https://www.metmuseum.org/es/about-the-met/collection-areas"

payload = {}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9',
    'cookie': 'NEXT_LOCALE=es; _gcl_au=1.1.364420609.1718667784; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22https://metmuseum.github.io/%22%2C%22sts%22:1718667783719%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=b47cb1ee-617b-43b7-ad3f-782eae933bd2%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718667783719}; _gid=GA1.2.769310445.1718667784; _tt_enable_cookie=1; _ttp=wo5XxGrVjyP1GtZwL5iJJJxTcF6; __qca=P0-1305345197-1718667784439; QuantumMetricSessionID=5c950e393b76216aee36f1133ffa8cbb; QuantumMetricUserID=866ec944987055fae20920bafd5738b7; shell#lang=en; __RequestVerificationToken=YcaGmqXzmMvrraLQ0kPQ8Ys1xXPkidngWz2BC6yMktpGYfZILQ2LatXnFPS1WMMXJpCKNOvgGdfEQkiAeu0opfoua241; visid_incap_1661922=d0JxHJHiTFiFTCKoGq1rlDjMcGYAAAAAQUIPAAAAAAAgOULgzXwiES+jduGz3//M; incap_ses_1695_1661922=8m3IPyijmQjEmHigntmFFzjMcGYAAAAAUTOYlHKlHBpO2ktjykSFLw==; website#lang=es; incap_ses_298_1661922=iArUQ3QqRFVxoafKgLUiBDjMcGYAAAAAZISBXv3YrznW7Bk5SVN+wA==; incap_ses_786_1661922=neFgUwwfHXMZ+G427W7oCjnMcGYAAAAA0EzlIVRiaVRXS8kXJ09hvQ==; incap_ses_1477_1661922=yx+dHOFe91oTuVFTv1t/FDnMcGYAAAAAeqE9vnTacf64QJ7Mi0iHXg==; incap_ses_1354_1661922=8DjPQf23pjnh10gq5l/KEjnMcGYAAAAAreG1Pu6iNKoJFdneqRibGQ==; incap_ses_1693_1661922=gDFnLWmLQBmAVXVbmr5+FzrMcGYAAAAAwSoWFBuaNFJ/Ep55pro5cg==; incap_ses_1453_1661922=bkDoWWpI4TbhcCfg3xcqFDrMcGYAAAAAMQ5qI6S1TNg5bmo5nx70dw==; incap_ses_1698_1661922=7b/HFvAz9gVTH0WSE4KQF13McGYAAAAA6As+XfmwraWjxHqP7Iy5gQ==; incap_ses_789_1661922=FiK5PwAfGH355hHVZhfzCl7McGYAAAAAH64ma6395VxWkDiWV7xA6Q==; incap_ses_1472_1661922=+O3+KuMA6GaldRkcRphtFF3McGYAAAAAue/SDM+C8Rpaj7PbC81Ddg==; incap_ses_1478_1661922=e3flDafNBzNeIKP5PemCFF7McGYAAAAAxrtmJx2VQQHdKyN3W9zmLw==; incap_ses_1476_1661922=4imHW0H55XU/NROwQM57FF7McGYAAAAAL3ggxR3LHepDmVpAp1c7Nw==; incap_ses_1697_1661922=RXRZOEn0PGWYTJ7tlPSMF13McGYAAAAAaRLdYbnP2SwTpI4w+RpaAg==; incap_ses_1298_1661922=Cf3DRnN4fXcGee8dMmwDEl/McGYAAAAAmCgQ/k/HTvQcUAnG9LMjoQ==; incap_ses_1479_1661922=L21pSztJ8xzWstGcvHaGFGHMcGYAAAAAWSOIWM6Jp3yAjTI5NW8R0w==; aceSession=cUZKi7n8L1zJfUih7iA+9ERuJPjVGGVJ8WU170H+UflXCpiAhoM7bnXgo5JRIMnGWU6Qv/T2Bn+5+X1AHMr6PMtNk0keZGRR/Bf41gUU7CaD9LicbN0uYNbKWjW8ZnbI2e6lSSZraGlHakre2oYjg7L0lLw9+5vtOkFJkThRQld66HKN1X8mwYYOCUqpEY75; nlbi_2349797=ULxnciGQzS3Fkv1UzMiLaQAAAADvf29D0b7rUkobA6K2mJbN; visid_incap_2349797=YTtqM4sFSoGenFBmzeisVy/NcGYAAAAAQUIPAAAAAAAE+8I1VCFJGiH/Fi5RaKgc; incap_ses_672_2349797=UrdeO/bAj2lI9RnXh2xTCTDNcGYAAAAAEoP06Ay42K4JFOhsPVqBnA==; visid_incap_1661977=n+SaDrD5QkGHUVwU/BXjN9/NcGYAAAAAQUIPAAAAAAA2tI2yje/0ex3TQoz6j4hq; incap_ses_672_1661977=YRxNYwm58UlImRrXh2xTCd/NcGYAAAAAMyS3KCkR0dU6OW1iC1VRPA==; nlbi_2349797_2147483392=LvJRchrfs1M45lPhzMiLaQAAAACL96UK7ejwHIUu2ln/gAXX; _ga_L6ZCHWX6DZ=GS1.1.1718668594.1.1.1718668810.0.0.0; _ga_80QRY9FZ67=GS1.1.1718668594.1.1.1718668810.0.0.0; incap_ses_787_1661922=0cA1dxeydWqk/Erba/zrCkXOcGYAAAAAXBKuNZF7HzdPupastfZLqA==; incap_ses_1694_1661922=15IoAW7Y4UJXsUz/GEyCF0bOcGYAAAAAPi2WeKRLS9D8bvhIzxpeIQ==; incap_ses_1239_1661922=gRXpTNUoPGR35JwkAtAxEUbOcGYAAAAAmDw9MrVuKm6yUPFNFncO6w==; incap_ses_1473_1661922=IrWQEubLCmRY36rAxCVxFEfOcGYAAAAA2e7tJwbjHdferFvtfQbQ0Q==; incap_ses_1454_1661922=cOriEdsg9khopDKGXqUtFEjOcGYAAAAAb6RBfH2vUW/l/ijeBgcHfA==; incap_ses_1696_1661922=yvCedjDhmjkq+B1JFmeJF0fOcGYAAAAARssElaGs3dx+KrNg0qNo2A==; incap_ses_1471_1661922=eotyegbXhDdWNXV3xwpqFEjOcGYAAAAApEnH2zwyGAVirQXueJ3t8A==; incap_ses_297_1661922=52JjWgdI7AoFLAcmAigfBEjOcGYAAAAAmYV/HRoL9jRzCQEY2SBBiA==; incap_ses_784_1661922=3eonVFcHz007Ucvp9lPhCkjOcGYAAAAA6ivyri/E0WotmFAo1PyRKQ==; _ga=GA1.2.640236580.1718667784; _dc_gtm_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1718667783.1.1.1718668883.0.0.0; visid_incap_1661922=W8Y/YhoIR0K08gJsYMDXAO/McGYAAAAAQUIPAAAAAAAuOMvuITkg1vZlEHu4o4LG; visid_incap_2349797=jZ8GNybHS72jAxMsGL4C50/NcGYAAAAAQUIPAAAAAAAlcncTqfUtfBxdpEQjTc35',
    'priority': 'u=0, i',
    'referer': 'https://www.metmuseum.org/es/about-the-met/collection-areas',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
