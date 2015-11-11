# -*- coding: utf-8 -*-
from django.db import models, migrations
from facilities.models import Facility

def  create_export_excel_view(apps, schema_editor):
    from django.db import connection
    cursor = connection.cursor()
    sql = """
        CREATE MATERIALIZED VIEW facilities_excel_export AS
        SELECT facilities_facility.id as id,
        facilities_facility.name as name, facilities_facility.code as code,
        facilities_facility.registration_number, facilities_facility.number_of_beds as beds,
        facilities_facility.number_of_cots as cots, common_ward.name as ward_name,
        common_county.name as county, common_constituency.name as constituency,
        facilities_facilitytype.name as facility_type_name, facilities_kephlevel.name as keph_level,
        facilities_owner.name as owner_name, facilities_regulatingbody.name as regulatory_body_name,
        facilities_facilitystatus.name as operation_status
         FROM facilities_facility
        LEFT JOIN facilities_kephlevel ON facilities_kephlevel.id = facilities_facility.keph_level_id
        LEFT JOIN facilities_owner ON facilities_owner.id = facilities_facility.owner_id
        LEFT JOIN facilities_facilitytype ON facilities_facilitytype.id = facilities_facility.facility_type_id
        LEFT JOIN facilities_regulatingbody ON facilities_regulatingbody.id = facilities_facility.regulatory_body_id
        LEFT JOIN facilities_facilitystatus ON facilities_facilitystatus.id = facilities_facility.operation_status_id
        LEFT JOIN common_ward ON  common_ward.id = facilities_facility.ward_id
        LEFT JOIN common_constituency ON  common_constituency.id = common_ward.constituency_id
        LEFT JOIN common_county ON  common_county.id = common_constituency.county_id;
        """
    cursor = cursor.execute(sql)


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', 'set_facility_code_sequence_min_value'),
    ]

    operations = [
        migrations.RunPython(create_export_excel_view),
    ]
