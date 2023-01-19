from rest_framework import serializers
from cube_history.models import data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = ('id', 'character_name','create_date','cube_type', 'item_upgrade_result'
                  ,'miracle_time_flag', 'item_equip_part','item_level', 'target_item',
                  'potential_option_grade', 'additional_potential_option_grade',
                  'before_potential_options_grade_1', 'before_potential_options_value_1',
                  'before_potential_options_grade_2', 'before_potential_options_value_2',
                  'before_potential_options_grade_3', 'before_potential_options_value_3',
                  'after_potential_options_grade_1', 'after_potential_options_value_1',
                  'after_potential_options_grade_2', 'after_potential_options_value_2',
                  'after_potential_options_grade_3', 'after_potential_options_value_3',
                  )