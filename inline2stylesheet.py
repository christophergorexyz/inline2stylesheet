#!/usr/bin/python
from HTMLParser import HTMLParser
from os.path import exists
from optparse import OptionParser

class inline2stylesheet(HTMLParser):
    """this class extends the HTMLParser to extract the css
    from the style attributes of html elements, and output
    them in a generated css file"""
    stylesDict = {}
    tagNest = []

    def handle_starttag(self, tag, attrs):
        self.tagNest.append(tag)
        if(not len(attrs)): return
        attrDict = dict(attrs)
        if(not attrDict.has_key('style')): return
        styleString = attrDict['style']
        styleList = [rule.strip() for rule in styleString.split(';') if rule.strip()!='']
        styleList.sort()
        styleKey = ";\n\t".join(styleList)
        if(not self.stylesDict.has_key(styleKey)):
            self.stylesDict[styleKey] = []
        if(not self.stylesDict[styleKey].count(styleString)):
            self.stylesDict[styleKey].append(styleString);

    def handle_endtag(self, tag):
        self.tagNest.pop();

    def printStyles(self):
        for key in self.stylesDict.keys():
            print key

    def output(self, fileName="out.css"):
        if not exists(fileName):
            index = 0;
            with open(fileName, 'w') as f:
                try:
                    for key in self.stylesDict.keys():
                        index += 1
                        rule = ".class" + str(index) + "{\n\t" + key + ";\n}\n"
                        f.write(rule)
                except IOError as e:
                    print "IOError, couldn't read file " + fileName
                finally:
                    f.close()

if __name__=="__main__":
    optParser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="write output to the specified file")
    (options, args) = parser.parse_args()

    f = file('index.html')
    p = inline2stylesheet()
    p.feed(f.read())
    p.output()
