from fanstatic import Library, Resource, GroupResource

extjs = Library('extjs', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

# adapter
extjs_adapter_ext = Resource(extjs, 'adapter/ext/ext-base.js',
                      debug='adapter/ext/ext-base-debug.js')


# extjs ui
extjs_js = Resource(extjs, 'ext-all.js', depends=[extjs_adapter_ext],
                              debug='ext-all-debug-w-comments.js')

extjs_css = Resource(extjs, 'resources/css/ext-all.css')

extjs_basic = GroupResource( [extjs_adapter_ext, extjs_js, extjs_css] )


# ux
extjs_ux_js = Resource(extjs, 'examples/ux/ux-all.js',
                       debug   = 'examples/ux/ux-all-debug.js',
                       depends = [extjs_js] )

extjs_ux_css = Resource(extjs, 'examples/ux/css/ux-all.css',
                        depends = [extjs_css] )

extjs_ux = GroupResource( [extjs_ux_js, extjs_ux_css] )

extjs_with_ux = GroupResource( [extjs_basic, extjs_ux] )


# themes
themes = [ 'gray', 'access' ]   # what about vista?

def add_theme(theme):
    resource_name = 'extjs_theme_%s' % theme
    css_name = '%s_css' % resource_name
    
    css = Resource(extjs, 'resources/css/xtheme-%s.css' % theme,
                    depends = [extjs_css] )

    globals()[resource_name] = css

for theme in themes:
    add_theme(theme)


# individual packages (if you don't want to use the -all files)
# TODO
