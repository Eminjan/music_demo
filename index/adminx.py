#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import xadmin

from .models import Song,Dynamic,Label,Comment
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '音乐网站后台管理系统'
    site_footer = '音乐网站 By:Eminjan'
    # menu_style = "accordion"


class LabelAdmin(object):
    list_display = ['label_id','label_name']
    list_filter = ['label_name']
    list_per_page = 15
    list_display_links = ['label_id','label_name']
    list_editable = ['label_name']
    model_icon = 'glyphicon glyphicon-tags'


class SongAdmin(object):
    list_display = ['song_id','song_name','song_singer','song_time','song_type','fav_nums','song_release']
    search_fields = ['song_name','song_singer','song_languages']
    list_filter = ['song_name','song_singer','fav_nums','song_release']
    list_editable = ['song_name','fav_nums','song_release']
    ordering = ['-fav_nums']
    list_per_page = 20
    list_display_links = ['song_id','song_name']
    model_icon = 'glyphicon glyphicon-music'


class DynamicAdmin(object):
    list_display = ['dynamic_id','song','dynamic_plays','dynamic_search','dynamic_down']
    list_filter = ['dynamic_plays','dynamic_search','dynamic_down']
    list_editable = ['dynamic_plays','dynamic_search','dynamic_down']
    list_per_page = 20
    list_display_links = ['dynamic_id','song']
    model_icon = 'glyphicon glyphicon-retweet'


class CommentAdmin(object):
    list_display = ['comment_id','comment_user','song','comment_date']
    list_editable = ['comment_date']
    list_per_page = 20
    list_display_links = ['comment_id','comment_user']
    model_icon = 'fa fa-comments-o'

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(Label,LabelAdmin)
xadmin.site.register(Song,SongAdmin)
xadmin.site.register(Dynamic,DynamicAdmin)
xadmin.site.register(Comment,CommentAdmin)
