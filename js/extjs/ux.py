from library import library
from fanstatic import Resource, GroupResource
import extjs

js = Resource(library, 'examples/ux/ux-all.js',
                  debug   = 'examples/ux/ux-all-debug.js',
                  depends = [extjs.js] )

css = Resource(library, 'examples/ux/css/ux-all.css',
                   depends = [extjs.css] )

all = GroupResource( [js, css] )

basic_with_ux = GroupResource( [extjs.basic, all] )