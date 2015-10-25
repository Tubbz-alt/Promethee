from django.contrib import admin

from .models import Project, ProjectActivity, ProjectLanguage





class ProjectActivityAdmin( admin.ModelAdmin ): 
	fieldsets = [
		(None,{'fields':['value', 'intensity']})
	]	
	list_display = ['value']
	
class ProjectLanguageAdmin( admin.ModelAdmin ): 
	fieldsets = [
		(None,{'fields':['value']})
	]	
	list_display = ['value']
	
class ProjectAdmin( admin.ModelAdmin ): 
	fieldsets = [
		(None,{'fields':['name', 'languages', 'activity', 'url', 'description']})
	]	
	list_display = ['name']
	#inlines = [ ProjectActivityAdmin, ProjectLanguageAdmin ]


# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectActivity, ProjectActivityAdmin)
admin.site.register(ProjectLanguage, ProjectLanguageAdmin)
