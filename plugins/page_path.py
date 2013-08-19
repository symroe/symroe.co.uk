def preBuild(site):

    from django.template.loader import add_to_builtins
    add_to_builtins('extras.templatetags')
    add_to_builtins('extras.markdown')
    
    
def preBuildPage(site, page, context, data):
    """

    """
    context['path'] = page.path

    return context, data