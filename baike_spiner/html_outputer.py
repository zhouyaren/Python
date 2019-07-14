import sys
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.txt','w')


        #ascii
        for data in self.datas:

            fout.write("url:%s\n"%data['url'])
            fout.write("title:%s\n"%data['title'].encode('gbk', 'ignore').decode("gbk", "ignore"))
            fout.write("summary:%s\n" %data['summary'].encode('gbk', 'ignore').decode("gbk", "ignore"))
            fout.write('\n')
            fout.write('\n')
            #print(data['title'],data['summary'])

        fout.close()