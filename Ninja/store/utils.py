class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_selected' not in kwargs:
            context['cat_selected'] = None
        return context
