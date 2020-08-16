import wordcloud

w = wordcloud.WordCloud()
w.generate("红楼梦.txt")
w.to_file("红楼梦词云.png")
