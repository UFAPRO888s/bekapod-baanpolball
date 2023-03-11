import markdown
import markdownify
import frontmatter
import json
import datetime
import pytz
from dateutil.tz import tzlocal
my_date = datetime.datetime.now(pytz.timezone('Asia/Bangkok'))
with open('./data/Legea.json', 'r') as f:
  data = json.load(f)

for value in data:
    #print(value)

    html_string = '''---
date: '''+str(my_date)+'''
description: "สรุปผลบอล '''+str(value['title'])+''' หลังจบการแข่งขัน ที่บ้านผลบอล เว็บเผยแพร่ข้อมูลการแข่งขันฟุตบอลที่เชื่อถือได้ และ อัพเดทไวที่สุด"
draft: false
images: ["https://images.fotmob.com/image_resources/logo/leaguelogo/'''+str(value['id'])+'''.png"]
lastmod: '''+str(my_date)+'''
publishDate: 2020-01-12 05:54:23.291856+07:00
series: []
legeaID: "'''+str(value['id'])+'''"
legeaName: "'''+str(value['title'])+'''"
slug: ''
summary: "สรุปผลบอล ลีก '''+str(value['title'])+''' หลังจบการแข่งขัน ที่บ้านผลบอล เว็บเผยแพร่ข้อมูลการแข่งขันฟุตบอลที่เชื่อถือได้ และ อัพเดทไวที่สุด"
title: "สรุปผลบอล ลีก '''+str(value['title'])+''' อัพเดทล่าสุด '''+str(my_date.strftime("%d/%m/%Y"))+''' "
---

# สรุปผลบอล '''+str(value['title'])+'''
อัพเดท '''+str(my_date.strftime("%d/%m/%Y"))+''' โดย บ้านผลบอล

'''

    print(value['slug'])
    markdown_string = markdownify.markdownify(html_string, heading_style='ATX')
    with open('./content/สรุปผลบอล/'+value['slug']+'.md', 'w', encoding="utf-8") as f:
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