from urllib.request import urlopen
import xmltodict


def rss_pull(request):
    xmltodict._process_namespace = True
    file = urlopen(request)
    data = file.read()
    file.close()
    rssData = xmltodict.parse(data)
    rssData= rssData['rss']
    print(rssData)
    print(rssData['channel']['description'])


rss_pull("https://sdp.cstj.qc.ca/feed/")