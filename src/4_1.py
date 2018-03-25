# テンプレファイルから変数を取得したい。
# が、デフォルトでそんな機能はないっぽい。
# どんなキーを渡せばいいか不明なのは困る。

from jinja2 import Template, Environment, FileSystemLoader, meta
import pathlib
import datetime

path_tpl = (pathlib.Path(__file__).parent.parent / 'res/templates').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl )))

template = env.get_template('md/copyright.md')
with pathlib.Path(template.filename).open() as f:
    ast = env.parse(f.read())
    tpl_vars = meta.find_undeclared_variables(ast)
    print(tpl_vars)

now = datetime.datetime.now()
# jinja2.exceptions.TemplateSyntaxError: unexpected '%'
#context = {'now': now, '%Y': f'{now:%Y}'}
context = {'now': now, 'year': f'{now:%Y}'}
res = template.render(**context)
print(res)
#print(f'{now:%Y-%m-%d %H:%M:%S}')

