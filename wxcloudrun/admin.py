from django.contrib import admin
from wxcloudrun import models
from wxcloudrun.models import datasmodel
from django.utils.safestring import mark_safe

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class commodityResource(resources.ModelResource):

    def __init__(self):
        super(commodityResource, self).__init__()

        field_list = models.datasmodel._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        print("after_import")

    def after_import_instance(self, instance, new, **kwargs):
        print("after_import_instance")

    class Meta:
        model = models.datasmodel
        skip_unchanged = True
        report_skipped = True
        fields = ('id','nickName','avatarUrl','_e8549b99_d7ea_3464_bc63_4ba2dcc23b51',"_05a53093_58e6_39b1_a837_02f3f663009f", "_4359099b_358d_3585_a012_d975a6cf2abd",'_0c929b5a_8e29_34da_8c61_3704437d8c16','_c3fbe1d4_2042_3425_a3c8_02ad8e7a670f','_634f177c_4ebc_36da_81c0_e2e82a7737db','_f4073b8e_d8d5_35c9_8727_3e2a2a88c0c5','_f7404e95_9d18_3664_967f_ce709a4e8317','_1cba0acb_7071_3ecc_b703_9612ffd2c404','_d9dfc62a_9761_3540_9e4c_7f88536361ca','_99cfff26_fb91_307a_af20_601c5957eb0d','_14d8d11b_d640_35ff_93de_abd4f246d172','_fe0254d2_b85e_3c8b_9faf_f892b31c528d','_854c1c71_483f_30c5_8e3e_f3766309b292','_26870961_e853_372f_9048_feebda2d3bcb','_c9a6bff6_9167_3d57_8215_4971b9f62883','_efe660d8_9d5e_3d77_9bed_13d882685acf','_136e6862_a481_37a0_910a_02fdd998c633','_586837ae_ca05_35e6_81ca_2d131dbe363c','_0ac9ba39_22ea_3707_a727_6cf6d68cbcae','_f93ff9e0_33f7_312b_8f76_51419d9e83bc','_76ef99fd_225d_3bb2_84df_3c604cf35380','_223d79fd_0454_3c87_a74e_b562759f7e1a','_7df178f5_74fb_365d_b557_ca12fbfbcb6c')




# admin.site.register(models.publicmodel)
@admin.register(models.datasmodel)  # 自已注册的admin
class DatamodelAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ('id','nickName','头像','_e8549b99_d7ea_3464_bc63_4ba2dcc23b51',"_05a53093_58e6_39b1_a837_02f3f663009f", "_4359099b_358d_3585_a012_d975a6cf2abd",'_0c929b5a_8e29_34da_8c61_3704437d8c16','_c3fbe1d4_2042_3425_a3c8_02ad8e7a670f','_634f177c_4ebc_36da_81c0_e2e82a7737db','_f4073b8e_d8d5_35c9_8727_3e2a2a88c0c5','_f7404e95_9d18_3664_967f_ce709a4e8317','_1cba0acb_7071_3ecc_b703_9612ffd2c404','_d9dfc62a_9761_3540_9e4c_7f88536361ca','_99cfff26_fb91_307a_af20_601c5957eb0d','_14d8d11b_d640_35ff_93de_abd4f246d172','_fe0254d2_b85e_3c8b_9faf_f892b31c528d','_854c1c71_483f_30c5_8e3e_f3766309b292','_26870961_e853_372f_9048_feebda2d3bcb','_c9a6bff6_9167_3d57_8215_4971b9f62883','_efe660d8_9d5e_3d77_9bed_13d882685acf','_136e6862_a481_37a0_910a_02fdd998c633','_586837ae_ca05_35e6_81ca_2d131dbe363c','_0ac9ba39_22ea_3707_a727_6cf6d68cbcae','_f93ff9e0_33f7_312b_8f76_51419d9e83bc','_76ef99fd_225d_3bb2_84df_3c604cf35380','_223d79fd_0454_3c87_a74e_b562759f7e1a','_7df178f5_74fb_365d_b557_ca12fbfbcb6c')
    # list_editable = ('id','_e8549b99_d7ea_3464_bc63_4ba2dcc23b51',"_05a53093_58e6_39b1_a837_02f3f663009f", "_4359099b_358d_3585_a012_d975a6cf2abd",'_0c929b5a_8e29_34da_8c61_3704437d8c16','_c3fbe1d4_2042_3425_a3c8_02ad8e7a670f','_634f177c_4ebc_36da_81c0_e2e82a7737db','_f4073b8e_d8d5_35c9_8727_3e2a2a88c0c5','_f7404e95_9d18_3664_967f_ce709a4e8317','_1cba0acb_7071_3ecc_b703_9612ffd2c404','_d9dfc62a_9761_3540_9e4c_7f88536361ca','_99cfff26_fb91_307a_af20_601c5957eb0d','_14d8d11b_d640_35ff_93de_abd4f246d172','_fe0254d2_b85e_3c8b_9faf_f892b31c528d','_854c1c71_483f_30c5_8e3e_f3766309b292','_26870961_e853_372f_9048_feebda2d3bcb','_c9a6bff6_9167_3d57_8215_4971b9f62883','_efe660d8_9d5e_3d77_9bed_13d882685acf','_136e6862_a481_37a0_910a_02fdd998c633','_586837ae_ca05_35e6_81ca_2d131dbe363c','_0ac9ba39_22ea_3707_a727_6cf6d68cbcae','_f93ff9e0_33f7_312b_8f76_51419d9e83bc','_76ef99fd_225d_3bb2_84df_3c604cf35380','_223d79fd_0454_3c87_a74e_b562759f7e1a','_7df178f5_74fb_365d_b557_ca12fbfbcb6c')
    list_per_page = 10
    resource_class = commodityResource

    def 头像(self,request):
        # return request.avatarUrl
        html_img=f"<img src={request.avatarUrl} width='50px' height='50px' />"
        return mark_safe(html_img)
admin.site.site_header = '后台管理系统'  # 设置header
admin.site.site_title = '后台管理系统'  # 设置title
admin.site.index_title = '后台管理系统'
admin.site.empty_value_display = "空"
