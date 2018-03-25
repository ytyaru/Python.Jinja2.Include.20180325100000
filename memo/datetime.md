# 現在日時を出す

template.md
```markdown
現在時刻は {{ '{0:%Y-%m-%d %H:%M:%S}'.format(now) }} です。
```

main.py
```python
from jinja2 import Template, Environment, FileSystemLoader, meta
import pathlib
import datetime

path_tpl = (pathlib.Path(__file__).parent.parent / 'res/templates').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl)))
template = env.get_template('md/now.md')

now = datetime.datetime.now()
res = template.render(now=now)
print(res)
```

## 問題点

* `now`の名前が予約されてしまう
* `now`の名前を使うことを知っていなければならない
* 書式について知らねばならない
    * python構文
        * `{0:書式}.format(now)`
    * datetime書式
        * '%Y-%m-%d %H:%M:%S'
* 冗長
    * `{{ %Y-%m-%d %H:%M:%S }}`のようにしたい 
        * `%`はjinjaが予約しているため使えない？
            * `jinja2.exceptions.TemplateSyntaxError: unexpected '%'`
    * `{{year}}`, `{{month}}`, などひとつずつやっていたら数が多すぎる
        * `{{year}}-{{month}}-{{day}}`のように冗長になる
            * ゼロ埋めしているものとしていないもの
            * 曜日
                * 数値
                * 単語
                    * 短縮
                    * 英語
                    * 日本語

結局、`{{ '{0:%Y-%m-%d %H:%M:%S}'.format(now) }}`が一番マシ。

`f''`にしたいのに。

