import sys
sys.path.append('nested');
import bar
print(bar.foo()) # 'bar'
print(bar.bar()) # 'foo'