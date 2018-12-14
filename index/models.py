from datetime import datetime
from django.db import models

# Create your models here.

class Label(models.Model):
    """
    歌曲分类列表 label
    """
    # 由于Django建数据库表的时候为数据表自动生成id字段并设置成自增和主键，所以我们不需要手动添加
    # 默认情况下id就是主键
    label_id = models.AutoField(primary_key=True,verbose_name='序号')
    label_name = models.CharField(max_length=10,verbose_name='分类标签')

    def __str__(self):
        return self.label_name

    class Meta:
        """
        设置Admin界面的显示标题
        """
        verbose_name = "歌曲分类"
        verbose_name_plural = verbose_name


class Song(models.Model):
    """
    歌曲信息表
    """
    song_id = models.AutoField(primary_key=True,verbose_name='序号')
    song_name = models.CharField(max_length=100,verbose_name='歌名')
    song_singer = models.CharField(max_length=50,verbose_name='歌手')
    song_time = models.CharField(max_length=10,verbose_name='时长')
    song_album = models.CharField(max_length=50,verbose_name='专辑')
    song_languages = models.CharField(max_length=20,verbose_name='语种')
    song_type = models.CharField(max_length=20,verbose_name='类型')
    song_release = models.CharField(verbose_name='发行时间',max_length=50)
    song_img =  models.CharField(verbose_name='封面图',max_length=100)
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    song_lyrics = models.CharField(max_length=50,verbose_name='歌词',default='暂无歌词')
    song_file = models.CharField(max_length=500,verbose_name='歌曲文件')
    label = models.ForeignKey(Label,on_delete=models.CASCADE,verbose_name='歌名分类')

    def __str__(self):
        return self.song_name

    class Meta:
        """
        设置Admin界面的显示标题
        """
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name


class Dynamic(models.Model):
    """
    歌曲动态列表
    """
    dynamic_id = models.AutoField(primary_key=True,verbose_name='序号')
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')
    dynamic_plays = models.IntegerField(verbose_name='播放次数',default=0)
    dynamic_search = models.IntegerField(verbose_name='搜索次数',default=0)
    dynamic_down =models.IntegerField(verbose_name='下载次数',default=0)

    class Meta:
        """
        设置Admin界面的显示标题
        """
        verbose_name = "歌曲动态"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    歌曲点评列表 comment
    """
    comment_id = models.AutoField(primary_key=True,verbose_name='序号')
    comment_text = models.CharField(max_length=500,verbose_name='内容')
    comment_user = models.CharField(max_length=20,verbose_name='用户')
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')
    comment_date = models.CharField(verbose_name='日期',max_length=50)

    class Meta:
        """
        设置Admin界面的显示标题
        """
        verbose_name = '歌曲评论'
        verbose_name_plural = verbose_name