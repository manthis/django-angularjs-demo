from __future__ import unicode_literals

from django.db import models


class CensusLearnSql(models.Model):
    id = models.IntegerField(
        primary_key=True,
        blank=True,
        null=False
    )
    age = models.IntegerField(
        blank=True,
        null=True
    )
    class_of_worker = models.CharField(
        db_column='class of worker',
        max_length=1000,
        blank=True,
        null=True
    )
    industry_code = models.CharField(
        db_column='industry code',
        max_length=1000,
        blank=True,
        null=True
    )
    occupation_code = models.CharField(
        db_column='occupation code',
        max_length=1000,
        blank=True,
        null=True
    )
    education = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    wage_per_hour = models.CharField(
        db_column='wage per hour',
        max_length=1000,
        blank=True,
        null=True
    )
    last_education = models.CharField(
        db_column='last education',
        max_length=1000,
        blank=True,
        null=True
    )
    marital_status = models.CharField(
        db_column='marital status',
        max_length=1000,
        blank=True,
        null=True
    )
    major_industry_code = models.CharField(
        db_column='major industry code',
        max_length=1000,
        blank=True,
        null=True
    )
    major_occupation_code = models.CharField(
        db_column='major occupation code',
        max_length=1000,
        blank=True,
        null=True
    )
    mace = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    hispanice = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    sex = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    member_of_labor = models.CharField(
        db_column='member of labor',
        max_length=1000,
        blank=True,
        null=True
    )
    reason_for_unemployment = models.CharField(
        db_column='reason for unemployment',
        max_length=1000,
        blank=True,
        null=True
    )
    fulltime = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    capital_gain = models.CharField(
        db_column='capital gain',
        max_length=1000,
        blank=True,
        null=True
    )
    capital_loss = models.CharField(
        db_column='capital loss',
        max_length=1000,
        blank=True,
        null=True
    )
    dividends = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    income_tax_liability = models.CharField(
        db_column='income tax liability',
        max_length=1000,
        blank=True,
        null=True
    )
    previous_residence_region = models.CharField(
        db_column='previous residence region',
        max_length=1000,
        blank=True,
        null=True
    )
    previous_residence_state = models.CharField(
        db_column='previous residence state',
        max_length=1000,
        blank=True,
        null=True
    )
    household_with_family = models.CharField(
        db_column='household-with-family',
        max_length=1000,
        blank=True,
        null=True
    )
    household_simple = models.CharField(
        db_column='household-simple',
        max_length=1000,
        blank=True,
        null=True
    )
    weight = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    msa_change = models.CharField(
        db_column='msa-change',
        max_length=1000,
        blank=True,
        null=True
    )
    reg_change = models.CharField(
        db_column='reg-change',
        max_length=1000,
        blank=True,
        null=True
    )
    within_reg_change = models.CharField(
        db_column='within-reg-change',
        max_length=1000,
        blank=True,
        null=True
    )
    lived_here = models.CharField(
        db_column='lived-here',
        max_length=1000,
        blank=True,
        null=True
    )
    migration_prev_res_in_sunbelt = models.CharField(
        db_column='migration prev res in sunbelt',
        max_length=1000,
        blank=True,
        null=True
    )
    num_persons_worked_for_employer = models.CharField(
        db_column='num persons worked for employer',
        max_length=1000,
        blank=True,
        null=True
    )
    family_members_under_118 = models.CharField(
        db_column='family members under 118',
        max_length=1000,
        blank=True,
        null=True
    )
    father_birth_country = models.CharField(
        db_column='father birth country',
        max_length=1000,
        blank=True,
        null=True
    )
    mother_birth_country = models.CharField(
        db_column='mother birth country',
        max_length=1000,
        blank=True,
        null=True
    )
    birth_country = models.CharField(
        db_column='birth country',
        max_length=1000,
        blank=True,
        null=True
    )
    citizenship = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    own_business_or_self_employed = models.CharField(
        db_column='own business or self employed',
        max_length=1000,
        blank=True,
        null=True
    )
    fill_questionnaire_for_veteran_s_admin = models.CharField(
        db_column="fill questionnaire for veteran's admin",
        max_length=1000,
        blank=True,
        null=True
    )
    veterans_benefits = models.CharField(
        db_column='veterans benefits',
        max_length=1000,
        blank=True,
        null=True
    )
    weeks_worked_in_year = models.CharField(
        db_column='weeks worked in year',
        max_length=1000,
        blank=True,
        null=True
    )
    year = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    salary_range = models.CharField(
        db_column='salary range',
        max_length=1000,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'census_learn_sql'
