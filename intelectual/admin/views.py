# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class HomeAdminView(TemplateView):
	template_name = "admin/admin.html"
