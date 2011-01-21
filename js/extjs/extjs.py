from fanstatic import Resource, GroupResource
import adapter
from library import library

js = Resource(library, 'ext-all.js', depends=[adapter.ext],
              debug='ext-all-debug-w-comments.js')

css = Resource(library, 'resources/css/ext-all.css')

basic = GroupResource( [adapter.ext, js, css] )