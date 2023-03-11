import markdown
import markdownify
import frontmatter
import json
import datetime
import pytz
import requests
from dateutil.tz import tzlocal
my_date = datetime.datetime.now(pytz.timezone('Asia/Bangkok'))
liv = requests.get('https://api.loopyt.com/ufatv')
text = json.loads(liv.text)


for value in text:
    #print(value)

    html_string = '''---
date: '''+str(my_date)+'''
description: "ดูบอลสด บ้านผลบอล '''+str(value['video'])+''' อัพเดทสัญญาณไวที่สุด ดูได้24ชม. ดูบอลออนไลน์ ดูบอลฟรี"
draft: false
images: ["/img/TV/'''+str(value['video'])+'''.jpg"]
lastmod: '''+str(my_date)+'''
publishDate: 2020-01-12 05:54:23.291856+07:00
series: []
liveID: "'''+str(value['id'])+'''"
liveName: "'''+str(value['video'])+'''"
slug: ''
summary: "ดูบอลสด ช่อง '''+str(value['video'])+'''  ที่ บ้านผลบอล อัพเดทสัญญาณไวที่สุด ดูได้24ชม. ดูบอลออนไลน์ ดูบอลฟรี"
title: "ดูบอลสด  บ้านผลบอล ช่อง '''+str(value['video'])+''' ดูบอลออนไลน์ ดูบอลฟรี"
---

# ดูบอลสด '''+str(value['video'])+''' ดูบอลออนไลน์ฟรี ที่บ้านผลบอล

{{< livesport >}}
'''

    print(value['video'])
    markdown_string = markdownify.markdownify(html_string, heading_style='ATX')
    with open('./content/football-live/liveplay/'+value['video']+'.md', 'w', encoding="utf-8") as f:
        f.write(markdown_string)


#updated_data = frontmatter.dumps(data)
#with open('./content/สรุปผลบอล/sample.md', 'w') as fx:
#    fx.write(updated_data)
# 2
#html_string = markdown.markdown(markdown_string)
#print(html_string)
#markdown_string = markdownify.markdownify(html_string)
#print(markdown_string)


#markdown_string = markdownify.markdownify(html_string, heading_style='ATX')


#with open('.content/สรุปผลบอล/sample.md', 'w') as f:
#    f.write(markdown_string)