#RSS 피드에서 내용 읽기(웹사이트 내용 읽기)

import feedparser

myFeed = feedparser.parse("http://feeds.mashable.com/Mashable") #매셔블 피드를 메모리에 로드
print('Feed Title :', myFeed['feed']['title']) #피드 제목
print('Number of posts :', len(myFeed.entries)) #포스트 수 
post = myFeed.entries[0]
print('Post Title :',post.title)
content = post.content[0].value #원본 HTML 콘텐츠에 액세스 한다.
print('Raw content :\n',content)
