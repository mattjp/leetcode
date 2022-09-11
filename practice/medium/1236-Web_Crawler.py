# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    
    def get_hostname(self, url):
        return url.replace('http://', '').split('/', 1)[0]
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.get_hostname(startUrl)
        
        urls = htmlParser.getUrls(startUrl)
        
        urls = list(filter(lambda u: self.get_hostname(u) == hostname, urls))
        
        queue = collections.deque(urls)
        output = [startUrl]
        cache = set([startUrl])
        
        while queue:
            url = queue.popleft()
            
            if url in cache:
                continue
            
            output.append(url)
            cache.add(url)
            
            urls = htmlParser.getUrls(url)
            urls = list(filter(
                lambda u: u not in cache and self.get_hostname(u) == hostname, urls
            ))
            
            queue.extend(urls)
            
        return output
