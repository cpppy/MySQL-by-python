# 基于内容的网页推荐

根据浏览器记录，爬取每个网页的中文部分，分词，统计，TF-IDF加权，用KNN的思想计算所关注网站（比如csdn博客）当天更新的博客的得分
根据得分，推荐得分较高的文章

posting what I insterested in
 
1.get your visiting history in browser
2.get the text in this html 
3.use jieba to deal with the text to word lists
4.use mysql to restore the words and its' rates in different classify
5.use machine-learning model to get a result which can decide the kind of web page you interested in
