import requests
from bs4 import BeautifulSoup

url = "https://www.ratemyprofessors.com/search/professors/1256?q=*" # Example school ID
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "AWSALB=gJFSoy2iFfO8fssA7SCstSrt++DChnB0Mq2hmMhLnDoWJNfyOgAvwEHPCrXvVa2fSMYnLEIpP/YcDCA52dZjyv6yw8wkY2zgAKBm6Itcr/p3WPvr7q+iNnrS1OMXVqqPfxJ/GZswY2toPzfPx9V4LIF4ZvgVhTVmHGG5vACFLRNkYeU97LkiU0sJmAkrrw==; AWSALBCORS=gJFSoy2iFfO8fssA7SCstSrt++DChnB0Mq2hmMhLnDoWJNfyOgAvwEHPCrXvVa2fSMYnLEIpP/YcDCA52dZjyv6yw8wkY2zgAKBm6Itcr/p3WPvr7q+iNnrS1OMXVqqPfxJ/GZswY2toPzfPx9V4LIF4ZvgVhTVmHGG5vACFLRNkYeU97LkiU0sJmAkrrw==; RMP_AUTH_COOKIE_VERSION=v02; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+25+2026+21%3A40%3A41+GMT-0500+(Eastern+Standard+Time)&version=202512.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b9a542e6-bbb3-47c8-b035-252f4fac03a9&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0003%3A1%2CC0001%3A1%2CC0004%3A1&intType=1&geolocation=%3B&AwaitingReconsent=false; OptanonAlertBoxClosed=2026-02-26T02:40:40.810Z; userSchoolId=U2Nob29sLTIzMQ==; userSchoolLegacyId=231; userSchoolName=CUNY%20Queens%20College; cid=Ym8KWCnIV9-20260225"
}


response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    rating = soup.find("div", class_="RatingValue__Numerator-qw8sqy-2 duhvlP")

    print(rating.text)