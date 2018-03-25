# テンプレファイルから変数を取得したい。
# が、デフォルトでそんな機能はないっぽい。
# どんなキーを渡せばいいか不明なのは困る。

from jinja2 import Template, Environment, FileSystemLoader, meta
import pathlib
#from jinja2 import Template, Environment, FileSystemLoader, contextfunction, meta
#from jinja2 import Template, Environment, FileSystemLoader, runtime
"""
@contextfunction
def get_context(context):
    print('AAAAAAAAAAAAAAAA')
    #print(context.Name)
    #print(context.get_all())
    return context
"""
path_tpl = (pathlib.Path(__file__).parent.parent / 'res/templates').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl )))

template = env.get_template('py/class.py')
#print(dir(template))
#print(template.filename)
with pathlib.Path(template.filename).open() as f:
    ast = env.parse(f.read())
    tpl_vars = meta.find_undeclared_variables(ast)
    print(tpl_vars)


#ast = env.parse('{{ Name }} is A.')
#tpl_vars = meta.find_undeclared_variables(ast)
#print(tpl_vars)

#print(template.blocks)
#print(type(template.module))
#print(dir(template.module))
#template.globals['context'] = get_context
#template.globals['callable'] = callable
res = template.render(Name='A')
print(res)
#print(template.context)
#print(res.context)

#print(res)
#print(dir(template))
#print(dir(template.module))
#print(template.render(IncludeFileName='main'))

