# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:57:12 2024

@author: ksn71
"""

import feedparser

myFeed=feedparser.parse("http://feeds.mashable.com/Mashable")

print('피드제목 :', myFeed['feed']['title'])
print('포스트 수:',len(myFeed.entries))

post=myFeed.entries[0]
print("포스트 제목:", post.title)

content=post.content[0].value
print('콘텐츠 원본:\n',content)