from datetime import datetime

from django.db import models

class datasmodel(models.Model):
    id = models.CharField (verbose_name='序号',max_length=128, db_index=True, primary_key=True)
    nickName = models.CharField(verbose_name='微信名',max_length=200, null=True, blank=True)
    avatarUrl = models.CharField(verbose_name='头像链接',max_length=200, null=True, blank=True)
    _e8549b99_d7ea_3464_bc63_4ba2dcc23b51 = models.TextField(verbose_name='性别', null=True, blank=True)
    _05a53093_58e6_39b1_a837_02f3f663009f = models.TextField (verbose_name='年龄', null=True, blank=True)
    _4359099b_358d_3585_a012_d975a6cf2abd = models.TextField (verbose_name='居住区域', null=True, blank=True)
    _0c929b5a_8e29_34da_8c61_3704437d8c16 = models.TextField (verbose_name='居住时间', null=True, blank=True)
    _c3fbe1d4_2042_3425_a3c8_02ad8e7a670f = models.TextField (verbose_name='月收入', null=True, blank=True)
    _634f177c_4ebc_36da_81c0_e2e82a7737db = models.TextField (verbose_name='文化程度', null=True, blank=True)
    _f4073b8e_d8d5_35c9_8727_3e2a2a88c0c5 = models.TextField (verbose_name='职业', null=True, blank=True)

    _f7404e95_9d18_3664_967f_ce709a4e8317 = models.TextField (verbose_name='最具有精神价值的地方', null=True, blank=True)
    _1cba0acb_7071_3ecc_b703_9612ffd2c404 = models.TextField (verbose_name='最具有休闲娱乐价值的地方', null=True, blank=True)
    _d9dfc62a_9761_3540_9e4c_7f88536361ca = models.TextField (verbose_name='最具有美学价值的地方', null=True, blank=True)
    _99cfff26_fb91_307a_af20_601c5957eb0d = models.TextField (verbose_name='最具有地方感的地方', null=True, blank=True)
    _14d8d11b_d640_35ff_93de_abd4f246d172 = models.TextField (verbose_name='最具有社会关系价值的地方', null=True, blank=True)
    _fe0254d2_b85e_3c8b_9faf_f892b31c528d = models.TextField (verbose_name='最具有文化遗产价值的地方', null=True, blank=True)
    _854c1c71_483f_30c5_8e3e_f3766309b292 = models.TextField (verbose_name='最具有教育价值的地方', null=True, blank=True)
    _26870961_e853_372f_9048_feebda2d3bcb = models.TextField (verbose_name='让您产生不愉快心理的地方', null=True, blank=True)
    _c9a6bff6_9167_3d57_8215_4971b9f62883 = models.TextField (verbose_name='让您感到不安全的地方', null=True, blank=True)

    _efe660d8_9d5e_3d77_9bed_13d882685acf = models.TextField (verbose_name='让您感到不安全的地方', null=True, blank=True)

    _136e6862_a481_37a0_910a_02fdd998c633 = models.TextField (verbose_name='精神价值方面', null=True, blank=True)
    _586837ae_ca05_35e6_81ca_2d131dbe363c = models.TextField (verbose_name='休闲娱乐价值', null=True, blank=True)
    _0ac9ba39_22ea_3707_a727_6cf6d68cbcae = models.TextField (verbose_name='美学价值', null=True, blank=True)
    _f93ff9e0_33f7_312b_8f76_51419d9e83bc = models.TextField (verbose_name='地方感价值', null=True, blank=True)
    _76ef99fd_225d_3bb2_84df_3c604cf35380 = models.TextField (verbose_name='社会关系价值', null=True, blank=True)
    _223d79fd_0454_3c87_a74e_b562759f7e1a = models.TextField (verbose_name='文化遗产价值', null=True, blank=True)
    _7df178f5_74fb_365d_b557_ca12fbfbcb6c = models.TextField (verbose_name='教育价值', null=True, blank=True)

    class Meta:
        verbose_name = '信息详情'  # 这里命名为中文名称，但显示时会在后面出现一个s
        verbose_name_plural = '信息列表'  # 配合verbose使用去除s

# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名
