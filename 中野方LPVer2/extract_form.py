import urllib.request
import json
import re

url = "https://docs.google.com/forms/d/e/1FAIpQLSc1ePxAJ-hKhNt_00InS2mvkjBJ6n_2iuIqTa9RzTGrznNGBw/viewform?pli=1"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (.*?);</script>', html, re.DOTALL)
    if match:
        data = match.group(1)
        data_list = json.loads(data)
        questions = data_list[1][1]
        for q in questions:
            title = q[1]
            try:
                # 質問項目によっては配列の構造が異なるためチェック
                entry_id = q[4][0][0]
                print(f"Title: {title}, Entry: entry.{entry_id}")
            except Exception as e:
                pass
except Exception as e:
    print(f"Error: {e}")
