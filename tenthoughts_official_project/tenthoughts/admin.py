from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from tenthoughts.models import SubmitedArticles, UserArticles, UserProf, Article, Group


class UserArticlesResource(resources.ModelResource):

        class Meta:
                model = UserArticles

class UserArticlesAdmin(ImportExportActionModelAdmin):
    resource_class = UserArticlesResource
    pass

admin.site.register(SubmitedArticles)
admin.site.register(UserArticles, UserArticlesAdmin)
admin.site.register(Article)
admin.site.register(Group)
admin.site.register(UserProf)
