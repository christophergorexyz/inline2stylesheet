#!/usr/bin/python
from HTMLParser import HTMLParser
class inline2stylesheet(HTMLParser):
    stylesDict = {}
    tagNest = []
    def handle_starttag(self, tag, attrs):
        self.tagNest.append(tag)
        if(len(attrs) <= 0): return
        attrDict = dict(attrs)
        if(not attrDict.has_key('style')): return
        styleString = attrDict['style']
        styleList = [rule.strip() for rule in styleString.split(';') if rule.strip()!='']
        styleList.sort();
    def handle_endtag(self, tag):
        self.tagNest.pop();
if __name__=="__main__":
    f = file('index.html')
    p = inline2stylesheet()
    p.feed(f.read());
