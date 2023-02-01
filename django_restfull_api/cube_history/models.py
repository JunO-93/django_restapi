from django.db import models

# Create your models here.
class data(models.Model):    
    
    id = models.CharField(max_length=100, primary_key=True)
    character_name = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)
    cube_type = models.CharField(max_length=100)
    item_upgrade_result = models.CharField(max_length=100)
    miracle_time_flag = models.CharField(max_length=100)
    item_equip_part = models.CharField(max_length=100)
    item_level = models.CharField(max_length=100)
    target_item = models.CharField(max_length=100)
    potential_option_grade = models.CharField(max_length=100)
    additional_potential_option_grade = models.CharField(max_length=100, default='')
    before_potential_options_grade_1 = models.CharField(max_length=100, default='', null=True)
    before_potential_options_value_1 = models.CharField(max_length=100, default='', null=True)
    before_potential_options_grade_2 = models.CharField(max_length=100, default='', null=True)
    before_potential_options_value_2 = models.CharField(max_length=100, default='', null=True)  
    before_potential_options_grade_3 = models.CharField(max_length=100, default='', null=True)
    before_potential_options_value_3 = models.CharField(max_length=100, default='', null=True)
    before_additional_potential_options_grade_1 = models.CharField(max_length=100, default='' , null=True)
    before_additional_potential_options_value_1 = models.CharField(max_length=100, default='' , null=True)
    before_additional_potential_options_grade_2 = models.CharField(max_length=100, default='' , null=True)
    before_additional_potential_options_value_2 = models.CharField(max_length=100, default='' , null=True)
    before_additional_potential_options_grade_3 = models.CharField(max_length=100, default='' , null=True)
    before_additional_potential_options_value_3 = models.CharField(max_length=100, default='' , null=True)
    after_potential_options_grade_1 = models.CharField(max_length=100, default='', null=True)
    after_potential_options_value_1 = models.CharField(max_length=100, default='', null=True)
    after_potential_options_grade_2 = models.CharField(max_length=100, default='', null=True)
    after_potential_options_value_2 = models.CharField(max_length=100, default='', null=True)
    after_potential_options_grade_3 = models.CharField(max_length=100, default='', null=True)
    after_potential_options_value_3 = models.CharField(max_length=100, default='', null=True)
    after_additional_potential_options_grade_1 = models.CharField(max_length=100, default='' , null=True)
    after_additional_potential_options_value_1 = models.CharField(max_length=100, default='' , null=True)
    after_additional_potential_options_grade_2 = models.CharField(max_length=100, default='' , null=True)
    after_additional_potential_options_value_2 = models.CharField(max_length=100, default='' , null=True)
    after_additional_potential_options_grade_3 = models.CharField(max_length=100, default='' , null=True)
    after_additional_potential_options_value_3 = models.CharField(max_length=100, default='' , null=True)

    def __str__(self) -> str:
        return self.character_name