from django.db import models
# from django_pandas.managers import DataFrameManager
#
#
# class Client(models.Model):
#     # ClientID = models.TextField(unique = True)
#     ClientName = models.TextField(null=True)
#     CreatedOn = models.DateField(null=True)
#     ShortName = models.TextField(unique=True)
#
#
# class Staging(models.Model):
#     # sr_no = models.IntegerField(unique = True, null = True)
#     recruiter = models.TextField(null=True)
#     client = models.TextField(null=True)
#     position = models.TextField(null=True, validators=[alnum])
#     reqt_date = models.TextField(null=True)
#     date_cv_submitted = models.DateField(null=True)
#     candidate_name = models.TextField(null=True)
#     current_status = models.IntegerField(null=True)
#     current_status_desc = models.TextField(null=True)
#     interview_date = models.DateField(blank=True, null=True)
#     remarks = models.TextField(null=True)
#     skills = models.TextField(null=True)
#     current_org = models.TextField(null=True)
#     qualification = models.TextField(null=True)
#     total_exp = models.TextField(null=True)
#     current_location = models.TextField(null=True)
#     contact_details_mobile = models.IntegerField(null=True, validators=[phone_len])
#     contact_details_phone2 = models.IntegerField(null=True, validators=[phone_len])
#     email = models.EmailField(null=True)
#     current_salary = models.TextField(null=True)
#     expected_salary_percentage = models.TextField(null=True)
#     expected_salary_amt = models.TextField(null=True)
#     notice_period = models.TextField(null=True)
#     Int_Tele_Date = models.DateField(blank=True, null=True)
#     Int_Tele_Result = models.TextField(blank=True, null=True)
#     Int_P1_Date = models.DateField(blank=True, null=True)
#     Int_P1_Result = models.TextField(null=True)
#     Int_p2_Date = models.DateField(null=True)
#     Int_p2_Result = models.TextField(null=True)
#     Int_p3_Date = models.DateField(blank=True, null=True)
#     Int_p3_Result = models.TextField(blank=True, null=True)
#     Int_Final_Date = models.DateField(blank=True, null=True)
#     Int_Final_Result = models.TextField(null=True)
#     Int_HR_Date = models.DateField(blank=True, null=True)
#     Int_HR_Result = models.TextField(null=True)
#     offer_date = models.DateField(blank=True, null=True)
#     offer_amt = models.TextField(blank=True, null=True)
#     joining_date = models.DateField(blank=True, null=True)
#     vacancy_code = models.TextField(null=True)
#     applicant_code = models.TextField(null=True)
#     DOB = models.DateField(blank=True, null=True)
#     preferred_company = models.TextField(null=True)
#     preferred_location = models.TextField(null=True)
#     week_number = models.IntegerField(null=True)
#     wk_year = models.IntegerField(null=True)
#     reason = models.TextField(null=True)
#     def savedata(self):
#         self.save()
#     objects = DataFrameManager()
#
#
#
#
# class GoodRecords(models.Model):
#     # sr_no = models.IntegerField(unique = True)
#     recruiter = models.ForeignKey('user.User', on_delete=models.RESTRICT)
#     client = models.ForeignKey('Client', on_delete=models.RESTRICT)
#     position = models.TextField(null=True)
#     reqt_date = models.DateField(null=True)
#     date_cv_submitted = models.DateField(null=True)
#     candidate_name = models.TextField(null=True)
#     current_status = models.IntegerField(null=True)
#     current_status_desc = models.TextField(null=True)
#     interview_date = models.DateField(blank=True, null=True)
#     remarks = models.TextField(blank=True, null=True)
#     skills = models.TextField(null=True)
#     current_org = models.TextField(null=True)
#     qualification = models.TextField(null=True)
#     total_exp = models.FloatField(null=True)
#     current_location = models.TextField(null=True)
#     contact_details_mobile = models.IntegerField(null=True)
#     contact_details_phone2 = models.IntegerField(null=True)
#     email = models.EmailField(null=True)
#     current_salary = models.FloatField(null=True)
#     expected_salary_percentage = models.IntegerField(null=True)
#     expected_salary_amt = models.FloatField(null=True)
#     notice_period = models.FloatField(null=True)
#     Int_Tele_Date = models.DateField(blank=True, null=True)
#     Int_Tele_Result = models.TextField(blank=True, null=True)
#     Int_P1_Date = models.DateField(blank=True, null=True)
#     Int_P1_Result = models.TextField(blank=True, null=True)
#     Int_p2_Date = models.DateField(blank=True, null=True)
#     Int_p2_Result = models.TextField(blank=True, null=True)
#     Int_p3_Date = models.DateField(blank=True, null=True)
#     Int_p3_Result = models.TextField(blank=True, null=True)
#     Int_Final_Date = models.DateField(blank=True, null=True)
#     Int_Final_Result = models.TextField(blank=True, null=True)
#     Int_HR_Date = models.DateField(blank=True, null=True)
#     Int_HR_Result = models.TextField(blank=True, null=True)
#     offer_date = models.DateField(blank=True, null=True)
#     offer_amt = models.FloatField(blank=True, null=True)
#     joining_date = models.DateField(blank=True, null=True)
#     vacancy_code = models.TextField(blank=True, null=True)
#     applicant_code = models.TextField(blank=True, null=True)
#     DOB = models.DateField(blank=True, null=True)
#     preferred_company = models.TextField(blank=True, null=True)
#     preferred_location = models.TextField(blank=True, null=True)
#     week_number = models.IntegerField(blank=True, null=True)
#     wk_year = models.IntegerField(blank=True, null=True)
#
#     objects = DataFrameManager()
#
#
# class BadRecords(models.Model):
#     # sr_no = models.IntegerField(unique = True)
#     recruiter = models.ForeignKey('user.User', on_delete=models.RESTRICT)
#     client = models.ForeignKey('Client', on_delete=models.RESTRICT)
#     position = models.TextField(null=True)
#     reqt_date = models.DateField(null=True)
#     date_cv_submitted = models.DateField(null=True)
#     candidate_name = models.TextField(null=True)
#     current_status = models.IntegerField(null=True)
#     current_status_desc = models.TextField(null=True)
#     interview_date = models.DateField(blank=True, null=True)
#     remarks = models.TextField(blank=True, null=True)
#     skills = models.TextField(null=True)
#     current_org = models.TextField(null=True)
#     qualification = models.TextField(null=True)
#     total_exp = models.FloatField(null=True)
#     current_location = models.TextField(null=True)
#     contact_details_mobile = models.IntegerField(null=True)
#     contact_details_phone2 = models.IntegerField(null=True)
#     email = models.EmailField(null=True)
#     current_salary = models.FloatField(null=True)
#     expected_salary_percentage = models.IntegerField(null=True)
#     expected_salary_amt = models.FloatField(null=True)
#     notice_period = models.FloatField(null=True)
#     Int_Tele_Date = models.DateField(blank=True, null=True)
#     Int_Tele_Result = models.TextField(blank=True, null=True)
#     Int_P1_Date = models.DateField(blank=True, null=True)
#     Int_P1_Result = models.TextField(blank=True, null=True)
#     Int_p2_Date = models.DateField(blank=True, null=True)
#     Int_p2_Result = models.TextField(blank=True, null=True)
#     Int_p3_Date = models.DateField(blank=True, null=True)
#     Int_p3_Result = models.TextField(blank=True, null=True)
#     Int_Final_Date = models.DateField(blank=True, null=True)
#     Int_Final_Result = models.TextField(blank=True, null=True)
#     Int_HR_Date = models.DateField(blank=True, null=True)
#     Int_HR_Result = models.TextField(blank=True, null=True)
#     offer_date = models.DateField(blank=True, null=True)
#     offer_amt = models.FloatField(blank=True, null=True)
#     joining_date = models.DateField(blank=True, null=True)
#     vacancy_code = models.TextField(blank=True, null=True)
#     applicant_code = models.TextField(blank=True, null=True)
#     DOB = models.DateField(blank=True, null=True)
#     preferred_company = models.TextField(blank=True, null=True)
#     preferred_location = models.TextField(blank=True, null=True)
#     week_number = models.IntegerField(blank=True, null=True)
#     wk_year = models.IntegerField(blank=True, null=True)
#     reason = models.TextField(blank=True, null=True)
#
#     objects = DataFrameManager()
