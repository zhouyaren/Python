import html_downloader,url_manager
import html_parser
import html_outputer

#爬虫调度程序的代码
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d:%s" %(count,new_url))
                count += 1
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.pars(new_url,html_cont)
                self.output.collect_data(new_data)
                self.urls.add_new_urls(new_urls)

                if count == 5:
                    break
            except:
                print("craw failed")
        self.output.output_html()


if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)