# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed =  True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Tblaccdemogoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddemoid = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblaccdemogoption'


class Tblaccdemograp(models.Model):
    flddemoid = models.CharField(primary_key=True, max_length=200)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    flddefault = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblaccdemograp'


class Tblacledger(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldledgerid = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblacledger'


class Tblactivity(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfrmname = models.CharField(max_length=100, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldactivity = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblactivity'


class Tbladjustment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldnetcost = models.FloatField(blank=True, null=True)
    fldsellpr = models.FloatField(blank=True, null=True)
    fldcompqty = models.FloatField(blank=True, null=True)
    fldcurrqty = models.FloatField(blank=True, null=True)
    fldreason = models.CharField(max_length=255, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbladjustment'


class Tbladvreceiptdetail(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillno = models.CharField(unique=True, max_length=250, blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    flddiscountamt = models.FloatField(blank=True, null=True)
    fldchargedamt = models.FloatField(blank=True, null=True)
    fldreceivedamt = models.FloatField(blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldchequeno = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldpatstate = models.CharField(max_length=75, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldcashpay = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=100, blank=True, null=True)
    fldverify = models.CharField(max_length=250, blank=True, null=True)
    fldinvoice = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbladvreceiptdetail'


class Tblagegroups(models.Model):
    fldgroup = models.CharField(primary_key=True, max_length=200)
    fldlower = models.FloatField(blank=True, null=True)
    fldhigher = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblagegroups'


class Tblanaesthesia(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblanaesthesia'


class Tblantipanel(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flditemname = models.CharField(max_length=200, blank=True, null=True)
    fldspecimen = models.CharField(max_length=250, blank=True, null=True)
    fldactive = models.CharField(max_length=50, blank=True, null=True)
    fldsensimax = models.FloatField(blank=True, null=True)
    fldsensimin = models.FloatField(blank=True, null=True)
    fldintermax = models.FloatField(blank=True, null=True)
    fldintermin = models.FloatField(blank=True, null=True)
    fldresismax = models.FloatField(blank=True, null=True)
    fldresismin = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblantipanel'


class Tblassetsentry(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldgroup = models.CharField(max_length=250, blank=True, null=True)
    fldspecs = models.CharField(max_length=250, blank=True, null=True)
    fldcode = models.CharField(max_length=250, blank=True, null=True)
    fldmanufacturer = models.CharField(max_length=250, blank=True, null=True)
    fldmodel = models.CharField(max_length=250, blank=True, null=True)
    fldserial = models.CharField(max_length=250, blank=True, null=True)
    fldledger = models.CharField(max_length=250, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldpurdate = models.DateTimeField(blank=True, null=True)
    fldqty = models.IntegerField(blank=True, null=True)
    fldunit = models.CharField(max_length=50, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    flddiscamt = models.FloatField(blank=True, null=True)
    fldditemamt = models.FloatField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcondition = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldrepairdate = models.DateTimeField(blank=True, null=True)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldpayment = models.CharField(max_length=50, blank=True, null=True)
    fldexpense = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblassetsentry'


class Tblassetsname(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldgroup = models.CharField(max_length=250, blank=True, null=True)
    fldledger = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblassetsname'


class Tblautoemail(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtousers = models.CharField(max_length=250, blank=True, null=True)
    fldcctype = models.CharField(max_length=50, blank=True, null=True)
    fldccusers = models.CharField(max_length=250, blank=True, null=True)
    fldfromhost = models.CharField(max_length=150, blank=True, null=True)
    fldfromuser = models.CharField(max_length=150, blank=True, null=True)
    fldfrompass = models.CharField(max_length=150, blank=True, null=True)
    fldsender = models.CharField(max_length=150, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldsubject = models.CharField(max_length=250, blank=True, null=True)
    fldcontent = models.CharField(max_length=250, blank=True, null=True)
    fldreport = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblautoemail'


class Tblautogroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldexitemtype = models.CharField(max_length=100, blank=True, null=True)
    fldcutoff = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldfollow = models.CharField(max_length=50, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldpayable = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblautogroup'


class Tblautoid(models.Model):
    fldtype = models.CharField(max_length=25)
    fldvalue = models.BigIntegerField(blank=True, null=True)
    fldid = models.AutoField(primary_key=True)
    fldfiscal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblautoid'


class Tblbillingset(models.Model):
    fldsetname = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tblbillingset'


class Tblbillitem(models.Model):
    fldbillitem = models.CharField(primary_key=True, max_length=200)
    flditemcateg = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbillitem'


class Tblbillrepoload(models.Model):
    fldbillno = models.CharField(primary_key=True, max_length=250)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbillrepoload'


class Tblbillsection(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsection = models.CharField(max_length=200, blank=True, null=True)
    fldcateg = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbillsection'


class Tblbillupload(models.Model):
    fldbillno = models.CharField(primary_key=True, max_length=250)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbillupload'


class Tblblood(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblblood'


class Tblbloodstore(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    fldtemp = models.CharField(max_length=150, blank=True, null=True)
    fldshelf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbloodstore'


class Tblbodyfluid(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfluid = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbodyfluid'


class Tblbulksale(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtarget = models.CharField(max_length=250, blank=True, null=True)
    fldbulktime = models.DateTimeField(blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldnetcost = models.FloatField(blank=True, null=True)
    fldqtydisp = models.FloatField(blank=True, null=True)
    fldqtyret = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblbulksale'


class Tblcashsources(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldvendor = models.CharField(max_length=150, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldcashamt = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcashsources'


class Tblcashvendor(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldvendor = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcashvendor'


class Tblcategorylist(models.Model):
    fldcategory = models.CharField(primary_key=True, max_length=250)
    fldpackage = models.CharField(max_length=250, blank=True, null=True)
    fldhiderank = models.IntegerField(blank=True, null=True)
    fldhideunit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcategorylist'


class Tblchemclass(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flclass = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblchemclass'


class Tblclaimcode(models.Model):
    fldclaimid = models.CharField(primary_key=True, max_length=150)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldptcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblclaimcode'


class Tblclinicentry(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldaccess = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblclinicentry'


class Tblcode(models.Model):
    fldcodename = models.CharField(primary_key=True, max_length=150)
    fldrecaddose = models.FloatField(blank=True, null=True)
    fldrecaddoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldrecadfreq = models.IntegerField(blank=True, null=True)
    fldrecpeddose = models.FloatField(blank=True, null=True)
    fldrecpeddoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldrecpedfreq = models.IntegerField(blank=True, null=True)
    fldchemclass = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldprn = models.CharField(max_length=25, blank=True, null=True)
    flddrugdetail = models.CharField(max_length=255, blank=True, null=True)
    fldhelppage = models.CharField(max_length=100, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldplasmaprotein = models.FloatField(blank=True, null=True)
    fldeliminhalflife = models.FloatField(blank=True, null=True)
    fldvoldistribution = models.FloatField(blank=True, null=True)
    fldeliminhepatic = models.FloatField(blank=True, null=True)
    fldeliminrenal = models.FloatField(blank=True, null=True)
    fldmechaction = models.CharField(max_length=255, blank=True, null=True)
    fldsensname = models.CharField(max_length=250, blank=True, null=True)
    fldrisklevel = models.CharField(max_length=100, blank=True, null=True)
    fldvaccine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcode'


class Tblcodebrady(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcodebrady'


class Tblcodehyper(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcodehyper'


class Tblcodehypo(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcodehypo'


class Tblcodelimit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcodename = models.CharField(max_length=200, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldmaxfreq = models.IntegerField(blank=True, null=True)
    fldmaxundose = models.FloatField(blank=True, null=True)
    fldmaxundoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldmaxdaladdose = models.FloatField(blank=True, null=True)
    fldmaxdaladdoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldmindaladdose = models.FloatField(blank=True, null=True)
    fldmindaladdoseunit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcodelimit'


class Tblcodetachy(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcodetachy'


class Tblcompaccess(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcompaccess'


class Tblcompatdrug(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcompatdrug'


class Tblcompatfluid(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcompatfluid'


class Tblcompexam(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldflag = models.IntegerField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcompexam'


class Tblcomplaints(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsymptom = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldflag = models.IntegerField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcomplaints'


class Tblconfinement(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flddeltime = models.DateTimeField(blank=True, null=True)
    fldpresent = models.CharField(max_length=250, blank=True, null=True)
    flddeltype = models.CharField(max_length=250, blank=True, null=True)
    flddelresult = models.CharField(max_length=250, blank=True, null=True)
    flddelphysician = models.CharField(max_length=25, blank=True, null=True)
    flddelnurse = models.CharField(max_length=250, blank=True, null=True)
    fldcomplication = models.CharField(max_length=250, blank=True, null=True)
    fldbloodloss = models.FloatField(blank=True, null=True)
    flddelwt = models.FloatField(blank=True, null=True)
    fldbabypatno = models.CharField(max_length=150, blank=True, null=True)
    fldcomment = models.TextField(blank=True, null=True)
    flddelassist = models.CharField(max_length=250, blank=True, null=True)
    flddelspot = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldbabyref = models.CharField(max_length=150, blank=True, null=True)
    flddeformity = models.CharField(max_length=150, blank=True, null=True)
    fldlabour = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblconfinement'


class Tblconsult(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldconsultname = models.CharField(max_length=250, blank=True, null=True)
    fldconsulttime = models.DateTimeField(blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldconsultid = models.CharField(max_length=150, blank=True, null=True)
    fldoutcome = models.CharField(max_length=25, blank=True, null=True)
    fldnotice = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblconsult'


class Tblcostbreak(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcostbreak'


class Tblcostgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcostgroup'


class Tblcronjob(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=50, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldscript = models.TextField(blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldstatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcronjob'


class Tblcurrency(models.Model):
    flditemunit = models.CharField(primary_key=True, max_length=50)
    fldconversion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcurrency'


class Tblcurrteleuser(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldteleuser = models.CharField(max_length=25, blank=True, null=True)
    fldentrytime = models.DateTimeField(blank=True, null=True)
    fldexittime = models.DateTimeField(blank=True, null=True)
    fldpresent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcurrteleuser'


class Tblcustcredit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    fldpercent = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustcredit'


class Tblcustdiscount(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    fldpercent = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustdiscount'


class Tbldelcomplication(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldelcomplication'


class Tbldeldeformity(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldeldeformity'


class Tbldelivery(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldelivery'


class Tbldellabour(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldellabour'


class Tbldemogoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddemoid = models.CharField(max_length=200, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldemogoption'


class Tbldemographic(models.Model):
    flddemoid = models.CharField(primary_key=True, max_length=200)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    flddefault = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldemographic'


class Tbldepartbedcharge(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddept = models.CharField(max_length=50, blank=True, null=True)
    fldoxyport = models.CharField(max_length=150, blank=True, null=True)
    fldventilator = models.CharField(max_length=150, blank=True, null=True)
    fldother = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldbedcharge = models.CharField(max_length=250, blank=True, null=True)
    fldconsultcharge = models.CharField(max_length=250, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldexititem = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldepartbedcharge'


class Tbldepartment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddept = models.CharField(max_length=50, blank=True, null=True)
    fldroom = models.CharField(max_length=50, blank=True, null=True)
    fldbedcharge = models.CharField(max_length=250, blank=True, null=True)
    fldround = models.CharField(max_length=250, blank=True, null=True)
    fldexititem = models.CharField(max_length=250, blank=True, null=True)
    fldcateg = models.CharField(max_length=150, blank=True, null=True)
    fldactive = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldhead = models.CharField(max_length=250, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldinterval = models.IntegerField(blank=True, null=True)
    fldstart = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldepartment'


class Tbldepartmentbed(models.Model):
    fldbed = models.CharField(primary_key=True, max_length=50)
    flddept = models.CharField(max_length=50, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldoxyport = models.CharField(max_length=150, blank=True, null=True)
    fldventilator = models.CharField(max_length=150, blank=True, null=True)
    fldother = models.CharField(max_length=150, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldepartmentbed'


class Tbldepconsult(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddept = models.CharField(max_length=50, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldselect = models.CharField(max_length=25, blank=True, null=True)
    fldmethod = models.CharField(max_length=25, blank=True, null=True)
    flddate = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldquota = models.IntegerField(blank=True, null=True)
    fldreason = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldepconsult'


class Tbldeptexam(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    flddept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldeptexam'


class Tbldeptexamoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    flddept = models.CharField(max_length=200, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldeptexamoption'


class Tbldeptgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=250, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldeptgroup'


class Tbldevices(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    fldlocat = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldevices'


class Tbldiagnogroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=250, blank=True, null=True)
    fldformat = models.CharField(max_length=150, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldcodeid = models.CharField(max_length=25, blank=True, null=True)
    fldcodenew = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldiagnogroup'


class Tbldietgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldietgroup'


class Tbldilutionfluid(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldilutionfluid'


class Tbldiscgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldiscgroup'


class Tbldischarge(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldoptions = models.TextField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldformat = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldischarge'


class Tbldiscount(models.Model):
    fldtype = models.CharField(primary_key=True, max_length=100)
    fldmode = models.CharField(max_length=100, blank=True, null=True)
    fldpercent = models.FloatField(blank=True, null=True)
    fldamount = models.FloatField(blank=True, null=True)
    fldcredit = models.FloatField(blank=True, null=True)
    fldlimit = models.CharField(max_length=100, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldreference = models.CharField(max_length=150, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldinvoice = models.CharField(max_length=25, blank=True, null=True)
    fldlab = models.FloatField(blank=True, null=True)
    fldradio = models.FloatField(blank=True, null=True)
    fldproc = models.FloatField(blank=True, null=True)
    fldequip = models.FloatField(blank=True, null=True)
    fldservice = models.FloatField(blank=True, null=True)
    fldother = models.FloatField(blank=True, null=True)
    fldmedicine = models.FloatField(blank=True, null=True)
    fldsurgical = models.FloatField(blank=True, null=True)
    fldextra = models.FloatField(blank=True, null=True)
    fldregist = models.FloatField(blank=True, null=True)
    fldyear = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldreserved = models.CharField(max_length=50, blank=True, null=True)
    fldgrouping = models.CharField(max_length=200, blank=True, null=True)
    fldcashincredit = models.FloatField(blank=True, null=True)
    fldcrdlab = models.FloatField(blank=True, null=True)
    fldcrdradio = models.FloatField(blank=True, null=True)
    fldcrdproc = models.FloatField(blank=True, null=True)
    fldcrdequip = models.FloatField(blank=True, null=True)
    fldcrdservice = models.FloatField(blank=True, null=True)
    fldcrdother = models.FloatField(blank=True, null=True)
    fldcrdmedicine = models.FloatField(blank=True, null=True)
    fldcrdsurgical = models.FloatField(blank=True, null=True)
    fldcrdextra = models.FloatField(blank=True, null=True)
    fldforce = models.CharField(max_length=100, blank=True, null=True)
    fldonline = models.CharField(max_length=100, blank=True, null=True)
    fldoffspring = models.CharField(max_length=100, blank=True, null=True)
    fldfixdepart = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldiscount'


class Tbldosageforms(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flforms = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldosageforms'


class Tbldrug(models.Model):
    flddrug = models.CharField(primary_key=True, max_length=200)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    fldstrength = models.FloatField(blank=True, null=True)
    fldstrunit = models.CharField(max_length=25, blank=True, null=True)
    fldroute = models.CharField(max_length=20, blank=True, null=True)
    fldhelppage = models.CharField(max_length=100, blank=True, null=True)
    fldciyear = models.FloatField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldrug'


class Tbldrugproblems(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldmedicine = models.CharField(max_length=250, blank=True, null=True)
    fldcondition = models.CharField(max_length=250, blank=True, null=True)
    fldrecommend = models.CharField(max_length=250, blank=True, null=True)
    fldlevel = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbldrugproblems'


class Tblduebilldetail(models.Model):
    fldbillno = models.CharField(primary_key=True, max_length=250)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblduebilldetail'


class Tblduebilling(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    fldbillitem = models.CharField(max_length=250, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)
    fldtaxper = models.FloatField(blank=True, null=True)
    flddiscper = models.FloatField(blank=True, null=True)
    fldditemamt = models.FloatField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldalert = models.IntegerField(blank=True, null=True)
    fldextracol = models.CharField(max_length=250, blank=True, null=True)
    fldextrarow = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblduebilling'


class Tblelectrolyte(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=50, blank=True, null=True)
    fldsalt = models.CharField(max_length=250, blank=True, null=True)
    fldmg = models.FloatField(blank=True, null=True)
    fldmmol = models.FloatField(blank=True, null=True)
    fldmeq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblelectrolyte'


class Tblenclock(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldlocktype = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblenclock'


class Tblencounter(models.Model):
    fldencounterval = models.CharField(primary_key=True, max_length=150)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldadmitlocat = models.CharField(max_length=100, blank=True, null=True)
    fldcurrlocat = models.CharField(max_length=100, blank=True, null=True)
    flddoa = models.DateTimeField(blank=True, null=True)
    flddod = models.DateTimeField(blank=True, null=True)
    fldheight = models.CharField(max_length=10, blank=True, null=True)
    fldcashdeposit = models.FloatField(blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldcashcredit = models.FloatField(blank=True, null=True)
    fldcharity = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldadmission = models.CharField(max_length=25, blank=True, null=True)
    fldfollowdate = models.DateTimeField(blank=True, null=True)
    fldreferto = models.CharField(max_length=250, blank=True, null=True)
    fldregdate = models.DateTimeField(blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldvisit = models.CharField(max_length=50, blank=True, null=True)
    fldvalidity = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldregistid = models.CharField(max_length=150, blank=True, null=True)
    fldadmitid = models.CharField(max_length=150, blank=True, null=True)
    fldfollow = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblencounter'


class TblencounterLog(models.Model):
    fldsno = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldadmitlocat = models.CharField(max_length=100, blank=True, null=True)
    fldcurrlocat = models.CharField(max_length=100, blank=True, null=True)
    flddoa = models.DateTimeField(blank=True, null=True)
    flddod = models.DateTimeField(blank=True, null=True)
    fldheight = models.CharField(max_length=10, blank=True, null=True)
    fldcashdeposit = models.FloatField(blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldcashcredit = models.FloatField(blank=True, null=True)
    fldcharity = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldadmission = models.CharField(max_length=25, blank=True, null=True)
    fldfollowdate = models.DateTimeField(blank=True, null=True)
    fldreferto = models.CharField(max_length=250, blank=True, null=True)
    fldregdate = models.DateTimeField(blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldvisit = models.CharField(max_length=50, blank=True, null=True)
    fldvalidity = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcurrtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblencounter_log'


class Tblentry(models.Model):
    fldstockno = models.BigIntegerField(primary_key=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldbatch = models.CharField(max_length=50, blank=True, null=True)
    fldexpiry = models.DateTimeField(blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldstatus = models.IntegerField(blank=True, null=True)
    fldsellpr = models.FloatField(blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcode = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldpast = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblentry'


class Tblentrybackup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldbatch = models.CharField(max_length=50, blank=True, null=True)
    fldexpiry = models.DateTimeField(blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldstatus = models.IntegerField(blank=True, null=True)
    fldsellpr = models.FloatField(blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcode = models.CharField(max_length=50, blank=True, null=True)
    fldentrytime = models.DateTimeField(blank=True, null=True)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblentrybackup'


class Tblethnicgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=250, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblethnicgroup'


class Tblevents(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblevents'


class Tblexam(models.Model):
    fldexamid = models.CharField(primary_key=True, max_length=200)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    fldcritical = models.FloatField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexam'


class Tblexamcomment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldmax = models.FloatField(blank=True, null=True)
    fldmin = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexamcomment'


class Tblexamgeneral(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldinput = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=250, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.CharField(max_length=250, blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexamgeneral'


class Tblexamlimit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldminimum = models.FloatField(blank=True, null=True)
    fldmaximum = models.FloatField(blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldnormal = models.FloatField(blank=True, null=True)
    fldhigh = models.FloatField(blank=True, null=True)
    fldlow = models.FloatField(blank=True, null=True)
    fldunit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexamlimit'


class Tblexamoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexamoption'


class Tblexamquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsubexam = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexamquali'


class Tblextra(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldextraid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextra'


class Tblextrabrand(models.Model):
    fldbrandid = models.CharField(primary_key=True, max_length=250)
    fldextraid = models.CharField(max_length=200, blank=True, null=True)
    fldbrand = models.CharField(max_length=50, blank=True, null=True)
    fldpackvol = models.FloatField(blank=True, null=True)
    fldvolunit = models.CharField(max_length=25, blank=True, null=True)
    fldmanufacturer = models.CharField(max_length=200, blank=True, null=True)
    flddepart = models.CharField(max_length=200, blank=True, null=True)
    flddetail = models.CharField(max_length=255, blank=True, null=True)
    fldstandard = models.CharField(max_length=25, blank=True, null=True)
    fldmaxqty = models.FloatField(blank=True, null=True)
    fldminqty = models.FloatField(blank=True, null=True)
    fldleadtime = models.IntegerField(blank=True, null=True)
    fldtaxcode = models.CharField(max_length=150, blank=True, null=True)
    fldactive = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextrabrand'


class Tblextradosing(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=25, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    fldfreq = models.CharField(max_length=25, blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    flddosetime = models.DateTimeField(blank=True, null=True)
    flddosecode = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextradosing'


class Tblextrapayers(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpayername = models.CharField(max_length=250, blank=True, null=True)
    fldpayeradd = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextrapayers'


class Tblextrapayitems(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextrapayitems'


class Tblextrareceipt(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpayername = models.CharField(max_length=250, blank=True, null=True)
    fldpayeradd = models.CharField(max_length=250, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldpayamount = models.FloatField(blank=True, null=True)
    fldpaytype = models.CharField(max_length=50, blank=True, null=True)
    fldchequeno = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldusername = models.CharField(max_length=250, blank=True, null=True)
    flduserpost = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextrareceipt'


class Tblextrasetting(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    flddiscpercent = models.FloatField(blank=True, null=True)
    fldcashmode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblextrasetting'


class Tblfileshare(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldshared = models.CharField(max_length=25, blank=True, null=True)
    fldperid = models.BigIntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfileshare'


class Tblfiscal(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfiscal = models.CharField(max_length=250, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldpatname = models.CharField(max_length=250, blank=True, null=True)
    fldpan = models.CharField(max_length=250, blank=True, null=True)
    flddate = models.DateTimeField(blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    flddiscountamt = models.FloatField(blank=True, null=True)
    fldtaxable = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    fldtotamt = models.FloatField(blank=True, null=True)
    fldsync = models.CharField(max_length=50, blank=True, null=True)
    fldprinted = models.CharField(max_length=50, blank=True, null=True)
    fldactive = models.CharField(max_length=50, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldpunch = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfiscal'


class Tblfiscalid(models.Model):
    fldindex = models.CharField(primary_key=True, max_length=250)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldlabel = models.CharField(max_length=100, blank=True, null=True)
    fldfrom = models.DateTimeField(blank=True, null=True)
    fldend = models.DateTimeField(blank=True, null=True)
    fldvalue = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfiscalid'


class Tblfisclosing(models.Model):
    fldindex = models.CharField(primary_key=True, max_length=250)
    fldfrom = models.DateTimeField(blank=True, null=True)
    fldend = models.DateTimeField(blank=True, null=True)
    fldpatbilling = models.CharField(max_length=150, blank=True, null=True)
    fldpatbilldetail = models.CharField(max_length=150, blank=True, null=True)
    fldtempbilldetail = models.CharField(max_length=150, blank=True, null=True)
    fldpatlabtest = models.CharField(max_length=150, blank=True, null=True)
    fldpatlabsubtest = models.CharField(max_length=150, blank=True, null=True)
    fldpatientexam = models.CharField(max_length=150, blank=True, null=True)
    fldpatientsubexam = models.CharField(max_length=150, blank=True, null=True)
    fldpatradiotest = models.CharField(max_length=150, blank=True, null=True)
    fldpatradiosubtest = models.CharField(max_length=150, blank=True, null=True)
    fldpatdosing = models.CharField(max_length=150, blank=True, null=True)
    fldpatreport = models.CharField(max_length=150, blank=True, null=True)
    fldstate = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfisclosing'


class Tblfoodcontent(models.Model):
    fldfoodid = models.CharField(primary_key=True, max_length=250)
    fldfood = models.CharField(max_length=150, blank=True, null=True)
    fldsource = models.CharField(max_length=250, blank=True, null=True)
    fldformat = models.CharField(max_length=150, blank=True, null=True)
    fldfoodtype = models.CharField(max_length=50, blank=True, null=True)
    fldfoodcode = models.CharField(max_length=100, blank=True, null=True)
    fldfluid = models.FloatField(blank=True, null=True)
    fldenergy = models.FloatField(blank=True, null=True)
    fldprotein = models.FloatField(blank=True, null=True)
    fldproteincont = models.CharField(max_length=250, blank=True, null=True)
    fldsugar = models.FloatField(blank=True, null=True)
    fldsugarcont = models.CharField(max_length=250, blank=True, null=True)
    fldlipid = models.FloatField(blank=True, null=True)
    fldlipidcont = models.CharField(max_length=250, blank=True, null=True)
    fldmineral = models.FloatField(blank=True, null=True)
    fldfibre = models.FloatField(blank=True, null=True)
    fldcalcium = models.FloatField(blank=True, null=True)
    fldphosphorous = models.FloatField(blank=True, null=True)
    fldiron = models.FloatField(blank=True, null=True)
    fldcarotene = models.FloatField(blank=True, null=True)
    fldthiamine = models.FloatField(blank=True, null=True)
    fldriboflavin = models.FloatField(blank=True, null=True)
    fldniacin = models.FloatField(blank=True, null=True)
    fldpyridoxine = models.FloatField(blank=True, null=True)
    fldfreefolic = models.FloatField(blank=True, null=True)
    fldtotalfolic = models.FloatField(blank=True, null=True)
    fldvitaminc = models.FloatField(blank=True, null=True)
    fldprep = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfoodcontent'


class Tblfoodgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemname = models.CharField(max_length=200, blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    fldprep = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfoodgroup'


class Tblfoodlist(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfood = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfoodlist'


class Tblfoodmix(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    fldtitle = models.CharField(max_length=200, blank=True, null=True)
    fldstatus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfoodmix'


class Tblfoodtype(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfoodtype = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblfoodtype'


class Tblforcediscount(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddisctype = models.CharField(max_length=100, blank=True, null=True)
    flddepart = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblforcediscount'


class Tblgenviolence(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldviotype = models.CharField(max_length=250, blank=True, null=True)
    fldviocause = models.CharField(max_length=250, blank=True, null=True)
    flddisability = models.CharField(max_length=250, blank=True, null=True)
    fldservice = models.CharField(max_length=250, blank=True, null=True)
    fldperpname = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=100, blank=True, null=True)
    fldperpsex = models.CharField(max_length=25, blank=True, null=True)
    fldperpage = models.FloatField(blank=True, null=True)
    fldcommtype = models.CharField(max_length=250, blank=True, null=True)
    fldcommcause = models.CharField(max_length=250, blank=True, null=True)
    fldcommability = models.CharField(max_length=250, blank=True, null=True)
    fldcommservice = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldviolref = models.CharField(max_length=150, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgenviolence'


class Tblgnupg(models.Model):
    fldkeyid = models.CharField(primary_key=True, max_length=250)
    fldkeyname = models.CharField(max_length=250, blank=True, null=True)
    fldfingerprint = models.CharField(max_length=255, blank=True, null=True)
    fldpublic = models.TextField(blank=True, null=True)
    fldprivate = models.TextField(blank=True, null=True)
    fldpublink = models.CharField(max_length=250, blank=True, null=True)
    fldprilink = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgnupg'


class Tblgroupexam(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=200, blank=True, null=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgroupexam'


class Tblgroupproc(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=200, blank=True, null=True)
    fldprocname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgroupproc'


class Tblgroupradio(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=200, blank=True, null=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldtesttype = models.CharField(max_length=50, blank=True, null=True)
    fldptsex = models.CharField(max_length=100, blank=True, null=True)
    fldactive = models.CharField(max_length=100, blank=True, null=True)
    fldquota = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgroupradio'


class Tblgrouptest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroupname = models.CharField(max_length=200, blank=True, null=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldtesttype = models.CharField(max_length=50, blank=True, null=True)
    fldactive = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgrouptest'


class Tblhaicasereports(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=250, blank=True, null=True)
    fldentity = models.CharField(max_length=250, blank=True, null=True)
    fldenrollbsi = models.CharField(max_length=250, blank=True, null=True)
    fldenrolluti = models.CharField(max_length=250, blank=True, null=True)
    fldutieventdate = models.DateTimeField(blank=True, null=True)
    fldbsieventdate = models.DateTimeField(blank=True, null=True)
    flduticlassify = models.CharField(max_length=250, blank=True, null=True)
    fldbsiclassify = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblhaicasereports'


class Tblhaidenominators(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddate = models.DateTimeField(blank=True, null=True)
    fldward = models.CharField(max_length=250, blank=True, null=True)
    fldweight = models.CharField(max_length=250, blank=True, null=True)
    fldcentral = models.IntegerField(blank=True, null=True)
    fldperipheral = models.IntegerField(blank=True, null=True)
    fldurinary = models.IntegerField(blank=True, null=True)
    fldtotal = models.IntegerField(blank=True, null=True)
    fldsource = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    dhis = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblhaidenominators'


class Tblhistory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldoptions = models.TextField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldformat = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblhistory'


class Tblhmissetting(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldvarval = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblhmissetting'


class Tblhospitals(models.Model):
    fldhospcode = models.CharField(primary_key=True, max_length=50)
    fldhospname = models.CharField(max_length=250, blank=True, null=True)
    fldaddress = models.CharField(max_length=250, blank=True, null=True)
    fldpality = models.CharField(max_length=250, blank=True, null=True)
    fldprovince = models.CharField(max_length=250, blank=True, null=True)
    flddistrict = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldlatitude = models.FloatField(blank=True, null=True)
    fldlongitude = models.FloatField(blank=True, null=True)
    fldcontact = models.CharField(max_length=250, blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldorgunit = models.CharField(max_length=250, blank=True, null=True)
    fldward = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblhospitals'


class Tblincompatdrug(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblincompatdrug'


class Tblincompatfluid(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblincompatfluid'


class Tblinjection(models.Model):
    fldinjection = models.CharField(primary_key=True, max_length=255)
    fldlabel = models.CharField(max_length=250, blank=True, null=True)
    fldreconst = models.CharField(max_length=255, blank=True, null=True)
    fldreconstroom = models.FloatField(blank=True, null=True)
    fldreconstcool = models.FloatField(blank=True, null=True)
    flddilution = models.CharField(max_length=255, blank=True, null=True)
    flddilutionroom = models.FloatField(blank=True, null=True)
    flddilutioncool = models.FloatField(blank=True, null=True)
    fldrateadmin = models.CharField(max_length=250, blank=True, null=True)
    fldsiteadmin = models.CharField(max_length=250, blank=True, null=True)
    fldrouteadmin = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblinjection'


class Tblinvid(models.Model):
    fldinvcode = models.CharField(primary_key=True, max_length=25)
    fldinvsub = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblinvid'


class Tblirdactivity(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldfrmname = models.CharField(max_length=100, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldactivity = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblirdactivity'


class Tbljobrecord(models.Model):
    fldindex = models.CharField(primary_key=True, max_length=250)
    fldfrmname = models.CharField(max_length=100, blank=True, null=True)
    fldfrmlabel = models.CharField(max_length=250, blank=True, null=True)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldentrytime = models.DateTimeField(blank=True, null=True)
    fldexittime = models.DateTimeField(blank=True, null=True)
    fldpresent = models.IntegerField(blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbljobrecord'


class Tbljournal(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddebitcateg = models.CharField(max_length=250, blank=True, null=True)
    flddebitlfno = models.CharField(max_length=250, blank=True, null=True)
    fldcreditcateg = models.CharField(max_length=250, blank=True, null=True)
    fldcreditlfno = models.CharField(max_length=250, blank=True, null=True)
    fldamt = models.FloatField(blank=True, null=True)
    flddate = models.DateTimeField(blank=True, null=True)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldreference = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbljournal'


class Tblkey(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    key1 = models.CharField(max_length=250, blank=True, null=True)
    key2 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblkey'


class Tbllabchemical(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    flditem = models.CharField(max_length=255, blank=True, null=True)
    fldamt = models.FloatField(blank=True, null=True)
    fldunit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbllabchemical'


class Tbllabel(models.Model):
    fldlabel = models.CharField(primary_key=True, max_length=225)
    flddrug = models.CharField(max_length=200, blank=True, null=True)
    fldroute = models.CharField(max_length=20, blank=True, null=True)
    fldopinfo = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    fldipinfo = models.CharField(max_length=255, blank=True, null=True)
    fldasepinfo = models.CharField(max_length=255, blank=True, null=True)
    fldmedinfo = models.TextField(blank=True, null=True)
    fldsubroute = models.CharField(max_length=50, blank=True, null=True)
    fldfinalstr = models.FloatField(blank=True, null=True)
    fldopfont = models.CharField(max_length=200, blank=True, null=True)
    fldosmolality = models.FloatField(blank=True, null=True)
    fldenergy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbllabel'


class Tbllocallabel(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldengcode = models.CharField(max_length=150, blank=True, null=True)
    fldengdire = models.CharField(max_length=255, blank=True, null=True)
    fldfont = models.CharField(max_length=255, blank=True, null=True)
    fldlocaldire = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbllocallabel'


class Tbllock(models.Model):
    fldlock = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tbllock'


class Tblmacaccess(models.Model):
    fldhostmac = models.CharField(primary_key=True, max_length=250)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostpass = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcompname = models.CharField(max_length=250, blank=True, null=True)
    fldaccess = models.CharField(max_length=50, blank=True, null=True)
    fldiptype = models.CharField(max_length=50, blank=True, null=True)
    fldcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmacaccess'


class Tblmanufacturer(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmanufacturer'


class Tblmasterdept(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldmaster = models.CharField(max_length=250, blank=True, null=True)
    fldgroup = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmasterdept'


class Tblmedadveffect(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedadveffect'


class Tblmedbrand(models.Model):
    fldbrandid = models.CharField(primary_key=True, max_length=250)
    flddrug = models.CharField(max_length=200, blank=True, null=True)
    flddosageform = models.CharField(max_length=50, blank=True, null=True)
    fldbrand = models.CharField(max_length=50, blank=True, null=True)
    fldmanufacturer = models.CharField(max_length=200, blank=True, null=True)
    flddetail = models.CharField(max_length=255, blank=True, null=True)
    fldstandard = models.CharField(max_length=25, blank=True, null=True)
    fldpackvol = models.FloatField(blank=True, null=True)
    fldvolunit = models.CharField(max_length=25, blank=True, null=True)
    fldmaxqty = models.FloatField(blank=True, null=True)
    fldminqty = models.FloatField(blank=True, null=True)
    fldleadtime = models.IntegerField(blank=True, null=True)
    fldpreservative = models.CharField(max_length=250, blank=True, null=True)
    fldnarcotic = models.CharField(max_length=10, blank=True, null=True)
    fldtabbreak = models.CharField(max_length=10, blank=True, null=True)
    flddeflabel = models.CharField(max_length=10, blank=True, null=True)
    fldactive = models.CharField(max_length=10, blank=True, null=True)
    fldtaxcode = models.CharField(max_length=150, blank=True, null=True)
    fldpacksize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedbrand'


class Tblmedcategory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flclass = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedcategory'


class Tblmedcontraindication(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedcontraindication'


class Tblmedgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldmedgroup = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedgroup'


class Tblmedhepatic(models.Model):
    medid = models.BigAutoField(primary_key=True)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    fldcondition = models.CharField(max_length=50, blank=True, null=True)
    fldoutput = models.CharField(max_length=255, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedhepatic'


class Tblmedimage(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldname = models.CharField(max_length=250, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flddet = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedimage'


class Tblmedinteraction(models.Model):
    medid = models.BigAutoField(primary_key=True)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    fldcondition = models.CharField(max_length=150, blank=True, null=True)
    fldoutput = models.CharField(max_length=255, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedinteraction'


class Tblmedinventory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldcode = models.CharField(unique=True, max_length=250, blank=True, null=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldencname = models.CharField(max_length=250, blank=True, null=True)
    fldcollect = models.DateTimeField(blank=True, null=True)
    fldexpiry = models.DateTimeField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedinventory'


class Tblmedmonitor(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedmonitor'


class Tblmedpregnancy(models.Model):
    medid = models.BigAutoField(primary_key=True)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    fldcondition = models.CharField(max_length=50, blank=True, null=True)
    fldoutput = models.CharField(max_length=255, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedpregnancy'


class Tblmedregimen(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldroute = models.CharField(max_length=25, blank=True, null=True)
    fldbrandid = models.CharField(max_length=150, blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    fldfreq = models.CharField(max_length=50, blank=True, null=True)
    fldday = models.IntegerField(blank=True, null=True)
    fldqty = models.IntegerField(blank=True, null=True)
    fldusage = models.CharField(max_length=150, blank=True, null=True)
    flduser = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedregimen'


class Tblmedrenal(models.Model):
    medid = models.BigAutoField(primary_key=True)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    fldgfrfrom = models.FloatField(blank=True, null=True)
    fldgfrto = models.FloatField(blank=True, null=True)
    fldoutput = models.CharField(max_length=255, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmedrenal'


class Tblmessagelog(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldwindow = models.CharField(max_length=50, blank=True, null=True)
    fldtarget = models.CharField(max_length=150, blank=True, null=True)
    fldmesstext = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmessagelog'


class Tblmiscategory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldparam = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmiscategory'


class Tblmonitor(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=25, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldevery = models.IntegerField(blank=True, null=True)
    fldunit = models.CharField(max_length=25, blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmonitor'


class Tblmunicipals(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpality = models.CharField(max_length=250, blank=True, null=True)
    flddistrict = models.CharField(max_length=250, blank=True, null=True)
    fldprovince = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmunicipals'


class Tblnewkey(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    key1 = models.CharField(max_length=250, blank=True, null=True)
    key2 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnewkey'


class Tblnodiscount(models.Model):
    flditemname = models.CharField(primary_key=True, max_length=250)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnodiscount'


class Tblnurdosing(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flddoseno = models.BigIntegerField(blank=True, null=True)
    fldvalue = models.FloatField(blank=True, null=True)
    fldunit = models.CharField(max_length=150, blank=True, null=True)
    fldfromtime = models.DateTimeField(blank=True, null=True)
    fldtotime = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnurdosing'


class Tblnutrition(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldfluid = models.FloatField(blank=True, null=True)
    fldprotein = models.FloatField(blank=True, null=True)
    fldlipid = models.FloatField(blank=True, null=True)
    flddextrose = models.FloatField(blank=True, null=True)
    fldnne = models.FloatField(blank=True, null=True)
    fldsodium = models.FloatField(blank=True, null=True)
    fldpotassium = models.FloatField(blank=True, null=True)
    fldvitamin = models.FloatField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnutrition'


class Tblobstetrics(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldgravida = models.IntegerField(blank=True, null=True)
    fldparity = models.IntegerField(blank=True, null=True)
    fldbortion = models.IntegerField(blank=True, null=True)
    fldlive = models.IntegerField(blank=True, null=True)
    fldlast = models.DateTimeField(blank=True, null=True)
    fldexpect = models.DateTimeField(blank=True, null=True)
    fldgestation = models.IntegerField(blank=True, null=True)
    fldpresent = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=250, blank=True, null=True)
    fldpast = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    flddelref = models.CharField(max_length=150, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblobstetrics'


class Tblofficedocs(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldextension = models.CharField(max_length=10, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblofficedocs'


class Tblonlinebook(models.Model):
    fldbookingval = models.CharField(primary_key=True, max_length=150)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldethniccode = models.CharField(max_length=50, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldptadmindate = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    fldconsultdate = models.DateTimeField(blank=True, null=True)
    fldadmitlocat = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldstate = models.CharField(max_length=25, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldpayreference = models.CharField(max_length=250, blank=True, null=True)
    fldhospital = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldremotemail = models.CharField(max_length=250, blank=True, null=True)
    fldhashcode = models.CharField(max_length=250, blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblonlinebook'


class Tblopvisit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldconsultname = models.CharField(max_length=250, blank=True, null=True)
    fldconsulttime = models.DateTimeField(blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldemerid = models.CharField(max_length=150, blank=True, null=True)
    fldoutcome = models.CharField(max_length=25, blank=True, null=True)
    fldnotice = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblopvisit'


class Tblorganism(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldorganism = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblorganism'


class Tblpackgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpackgroup = models.CharField(max_length=250, blank=True, null=True)
    fldpackage = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpackgroup'


class Tblpackschedule(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldtime = models.CharField(max_length=50, blank=True, null=True)
    fldfromtime = models.DateTimeField(blank=True, null=True)
    fldtotime = models.DateTimeField(blank=True, null=True)
    fldday = models.CharField(max_length=50, blank=True, null=True)
    flddaysvalue = models.CharField(max_length=250, blank=True, null=True)
    fldmonth = models.CharField(max_length=50, blank=True, null=True)
    fldmonthsvalue = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpackschedule'


class Tblpacsupload(models.Model):
    fldhash = models.CharField(primary_key=True, max_length=250)
    fldsave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpacsupload'


class Tblpataccgeneral(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldinput = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=250, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.CharField(max_length=250, blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldnewdate = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpataccgeneral'


class Tblpatbillcounts(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatbillcounts'


class Tblpatbilldetail(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillno = models.CharField(unique=True, max_length=250, blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    fldtaxgroup = models.CharField(max_length=150, blank=True, null=True)
    flddiscountamt = models.FloatField(blank=True, null=True)
    flddiscountgroup = models.CharField(max_length=150, blank=True, null=True)
    fldchargedamt = models.FloatField(blank=True, null=True)
    fldreceivedamt = models.FloatField(blank=True, null=True)
    fldcurdeposit = models.FloatField(blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldchequeno = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldprevdeposit = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatbilldetail'


class Tblpatbilling(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    flditemno = models.BigIntegerField(blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)
    fldtaxper = models.FloatField(blank=True, null=True)
    flddiscper = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    flddiscamt = models.FloatField(blank=True, null=True)
    fldditemamt = models.FloatField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldparent = models.BigIntegerField(blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldtarget = models.CharField(max_length=50, blank=True, null=True)
    fldpayto = models.CharField(max_length=25, blank=True, null=True)
    fldrefer = models.CharField(max_length=25, blank=True, null=True)
    fldsample = models.CharField(max_length=50, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldcurrlocat = models.CharField(max_length=100, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldreason = models.CharField(max_length=250, blank=True, null=True)
    fldretbill = models.CharField(max_length=250, blank=True, null=True)
    fldretqty = models.FloatField(blank=True, null=True)
    fldalert = models.IntegerField(blank=True, null=True)
    fldextracol = models.CharField(max_length=250, blank=True, null=True)
    fldextrarow = models.CharField(max_length=250, blank=True, null=True)
    fldclaimid = models.CharField(max_length=250, blank=True, null=True)
    fldclaimstate = models.CharField(max_length=250, blank=True, null=True)
    fldextradata = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcashincredit = models.FloatField(blank=True, null=True)
    fldsubsidy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatbilling'


class Tblpatcharity(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcharitytype = models.CharField(max_length=150, blank=True, null=True)
    fldcharityamt = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatcharity'


class Tblpatdevice(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flddevicetype = models.CharField(max_length=250, blank=True, null=True)
    flddevicepath = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatdevice'


class Tblpatdoseremote(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flddoseno = models.BigIntegerField(blank=True, null=True)
    fldqtydisp = models.FloatField(blank=True, null=True)
    fldqtyret = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatdoseremote'


class Tblpatdosing(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    fldroute = models.CharField(max_length=150, blank=True, null=True)
    flditem = models.CharField(max_length=255, blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    fldfreq = models.CharField(max_length=25, blank=True, null=True)
    flddays = models.FloatField(blank=True, null=True)
    fldqtydisp = models.FloatField(blank=True, null=True)
    fldqtyret = models.FloatField(blank=True, null=True)
    fldprescriber = models.CharField(max_length=255, blank=True, null=True)
    fldregno = models.CharField(max_length=255, blank=True, null=True)
    fldlevel = models.CharField(max_length=50, blank=True, null=True)
    flddirection = models.CharField(max_length=250, blank=True, null=True)
    flddispmode = models.CharField(max_length=150, blank=True, null=True)
    fldorder = models.CharField(max_length=50, blank=True, null=True)
    fldcurval = models.CharField(max_length=50, blank=True, null=True)
    fldstarttime = models.DateTimeField(blank=True, null=True)
    fldendtime = models.DateTimeField(blank=True, null=True)
    fldfixname = models.CharField(max_length=250, blank=True, null=True)
    fldfixrate = models.FloatField(blank=True, null=True)
    fldtaxper = models.FloatField(blank=True, null=True)
    flddiscper = models.FloatField(blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    flduserid_order = models.CharField(max_length=25, blank=True, null=True)
    fldtime_order = models.DateTimeField(blank=True, null=True)
    fldcomp_order = models.CharField(max_length=50, blank=True, null=True)
    fldsave_order = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldlabel = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    flduserid_disp = models.CharField(max_length=25, blank=True, null=True)
    fldtime_disp = models.DateTimeField(blank=True, null=True)
    fldcomp_disp = models.CharField(max_length=50, blank=True, null=True)
    fldcashincredit = models.FloatField(blank=True, null=True)
    fldextracol = models.CharField(max_length=250, blank=True, null=True)
    fldextrarow = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatdosing'


class Tblpatevents(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=255, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    fldfirstuserid = models.CharField(max_length=25, blank=True, null=True)
    fldfirsttime = models.DateTimeField(blank=True, null=True)
    fldfirstcomp = models.CharField(max_length=50, blank=True, null=True)
    fldfirstsave = models.IntegerField(blank=True, null=True)
    fldseconduserid = models.CharField(max_length=25, blank=True, null=True)
    fldsecondtime = models.DateTimeField(blank=True, null=True)
    fldsecondcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsecondsave = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=100, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatevents'


class Tblpatexamsubtable(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.BigIntegerField(blank=True, null=True)
    fldsubexamid = models.BigIntegerField(blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    fldvariable = models.CharField(max_length=200, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldcolm2 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm3 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm4 = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatexamsubtable'


class Tblpatfindings(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldcode = models.CharField(max_length=255, blank=True, null=True)
    fldcodeid = models.CharField(max_length=255, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcodenew = models.CharField(max_length=25, blank=True, null=True)
    fldflag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatfindings'


class Tblpatgeneral(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldinput = models.CharField(max_length=250, blank=True, null=True)
    fldgroupid = models.BigIntegerField(blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldnewdate = models.DateTimeField(blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatgeneral'


class Tblpatgenshare(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemid = models.BigIntegerField(blank=True, null=True)
    fldcategory = models.CharField(max_length=200, blank=True, null=True)
    fldusertype = models.CharField(max_length=200, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldreport = models.CharField(max_length=250, blank=True, null=True)
    fldmixper = models.FloatField(blank=True, null=True)
    fldchange = models.FloatField(blank=True, null=True)
    fldchreason = models.CharField(max_length=250, blank=True, null=True)
    fldactive = models.CharField(max_length=25, blank=True, null=True)
    fldshareamt = models.FloatField(blank=True, null=True)
    fldtdsper = models.FloatField(blank=True, null=True)
    fldsharenet = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatgenshare'


class Tblpathocategory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flclass = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpathocategory'


class Tblpathoexam(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldparenttype = models.CharField(max_length=25, blank=True, null=True)
    fldexamcategory = models.CharField(max_length=100, blank=True, null=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldrelation = models.CharField(max_length=25, blank=True, null=True)
    fldvalquali = models.CharField(max_length=250, blank=True, null=True)
    fldvalquanti = models.FloatField(blank=True, null=True)
    fldexamtype = models.CharField(max_length=50, blank=True, null=True)
    fldbaserate = models.FloatField(blank=True, null=True)
    fldnegrate = models.FloatField(blank=True, null=True)
    fldhitrate = models.FloatField(blank=True, null=True)
    fldfalserate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpathoexam'


class Tblpathosymp(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldparenttype = models.CharField(max_length=25, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldrelation = models.CharField(max_length=25, blank=True, null=True)
    fldvalquali = models.CharField(max_length=250, blank=True, null=True)
    fldvalquanti = models.FloatField(blank=True, null=True)
    fldsympfreq = models.CharField(max_length=25, blank=True, null=True)
    fldbaserate = models.FloatField(blank=True, null=True)
    fldnegrate = models.FloatField(blank=True, null=True)
    fldhitrate = models.FloatField(blank=True, null=True)
    fldfalserate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpathosymp'


class Tblpathotest(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldparenttype = models.CharField(max_length=25, blank=True, null=True)
    fldtestcategory = models.CharField(max_length=100, blank=True, null=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldrelation = models.CharField(max_length=25, blank=True, null=True)
    fldvalquali = models.CharField(max_length=250, blank=True, null=True)
    fldvalquanti = models.FloatField(blank=True, null=True)
    fldtesttype = models.CharField(max_length=50, blank=True, null=True)
    fldtestunit = models.CharField(max_length=25, blank=True, null=True)
    fldbaserate = models.FloatField(blank=True, null=True)
    fldnegrate = models.FloatField(blank=True, null=True)
    fldhitrate = models.FloatField(blank=True, null=True)
    fldfalserate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpathotest'


class Tblpatientbook(models.Model):
    fldbookingval = models.CharField(primary_key=True, max_length=150)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldptadmindate = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    fldconsultdate = models.DateTimeField(blank=True, null=True)
    fldadmitlocat = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldstate = models.CharField(max_length=25, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldpayreference = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldremotemail = models.CharField(max_length=250, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)
    fldethniccode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientbook'


class Tblpatientdate(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldhead = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientdate'


class Tblpatientdicom(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    fldkeyword = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientdicom'


class Tblpatientexam(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldserial = models.IntegerField(blank=True, null=True)
    fldserialval = models.CharField(max_length=250, blank=True, null=True)
    fldinput = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=250, blank=True, null=True)
    fldhead = models.CharField(max_length=250, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldrepquali = models.TextField(blank=True, null=True)
    fldrepquanti = models.FloatField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    fldrepdate = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientexam'


class Tblpatientimage(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    fldkeyword = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientimage'


class Tblpatientinfo(models.Model):
    fldpatientval = models.CharField(primary_key=True, max_length=150)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldethniccode = models.CharField(max_length=250, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldptadmindate = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    flddiscount = models.CharField(max_length=150, blank=True, null=True)
    fldadmitfile = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldencrypt = models.IntegerField(blank=True, null=True)
    fldpassword = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldrank = models.CharField(max_length=250, blank=True, null=True)
    fldunit = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldupuser = models.CharField(max_length=25, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientinfo'


class TblpatientinfoLog(models.Model):
    fldsno = models.BigAutoField(primary_key=True)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldethniccode = models.CharField(max_length=250, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldptadmindate = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    flddiscount = models.CharField(max_length=150, blank=True, null=True)
    fldadmitfile = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldencrypt = models.IntegerField(blank=True, null=True)
    fldpassword = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldrank = models.CharField(max_length=250, blank=True, null=True)
    fldunit = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldupuser = models.CharField(max_length=25, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcurrtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblpatientinfo_log'


class Tblpatientpass(models.Model):
    fldpatientval = models.CharField(primary_key=True, max_length=150)
    fldpass = models.CharField(max_length=250, blank=True, null=True)
    fldfromdate = models.DateTimeField(blank=True, null=True)
    fldtodate = models.DateTimeField(blank=True, null=True)
    fldusercode = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientpass'


class Tblpatientstudy(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldpatcode = models.CharField(max_length=250, blank=True, null=True)
    fldstudycode = models.CharField(max_length=150, blank=True, null=True)
    fldconsentautodata = models.CharField(max_length=50, blank=True, null=True)
    fldstatusautodata = models.CharField(max_length=50, blank=True, null=True)
    fldconsentinterview = models.CharField(max_length=50, blank=True, null=True)
    fldstatusinterview = models.CharField(max_length=50, blank=True, null=True)
    fldconsentformpic = models.TextField(blank=True, null=True)
    fldconsentformlink = models.CharField(max_length=250, blank=True, null=True)
    fldiintervireformpic = models.TextField(blank=True, null=True)
    fldinterviewformlink = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientstudy'


class Tblpatientsubexam(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldheadid = models.BigIntegerField(blank=True, null=True)
    fldsubtexam = models.CharField(max_length=200, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.TextField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldparent = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatientsubexam'


class Tblpatimagedata(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    fldkeyword = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatimagedata'


class Tblpatlabsubtable(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldsubtestid = models.BigIntegerField(blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    fldvariable = models.CharField(max_length=200, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldcolm2 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm3 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm4 = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatlabsubtable'


class Tblpatlabsubtest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldsubtest = models.CharField(max_length=200, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.TextField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldparent = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatlabsubtest'


class Tblpatlabtest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.CharField(max_length=250, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldgroupid = models.BigIntegerField(blank=True, null=True)
    fldsampleid = models.CharField(max_length=250, blank=True, null=True)
    fldsampletype = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.TextField(blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    fldtestunit = models.CharField(max_length=25, blank=True, null=True)
    fldstatus = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldrefername = models.CharField(max_length=250, blank=True, null=True)
    fldcondition = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    flvisible = models.CharField(max_length=50, blank=True, null=True)
    fldtest_type = models.CharField(max_length=50, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    flduserid_sample = models.CharField(max_length=25, blank=True, null=True)
    fldtime_sample = models.DateTimeField(blank=True, null=True)
    fldcomp_sample = models.CharField(max_length=50, blank=True, null=True)
    fldsave_sample = models.IntegerField(blank=True, null=True)
    flduptime_sample = models.DateTimeField(blank=True, null=True)
    flduserid_start = models.CharField(max_length=25, blank=True, null=True)
    fldtime_start = models.DateTimeField(blank=True, null=True)
    fldcomp_start = models.CharField(max_length=50, blank=True, null=True)
    fldsave_start = models.IntegerField(blank=True, null=True)
    flduptime_start = models.DateTimeField(blank=True, null=True)
    flduserid_report = models.CharField(max_length=25, blank=True, null=True)
    fldtime_report = models.DateTimeField(blank=True, null=True)
    fldcomp_report = models.CharField(max_length=50, blank=True, null=True)
    fldsave_report = models.IntegerField(blank=True, null=True)
    flduptime_report = models.DateTimeField(blank=True, null=True)
    flduserid_verify = models.CharField(max_length=25, blank=True, null=True)
    fldtime_verify = models.DateTimeField(blank=True, null=True)
    fldcomp_verify = models.CharField(max_length=50, blank=True, null=True)
    fldsave_verify = models.IntegerField(blank=True, null=True)
    flduptime_verify = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldflag = models.IntegerField(blank=True, null=True)
    fldupuser_report = models.CharField(max_length=25, blank=True, null=True)
    fldupuser_verify = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatlabtest'


class Tblpatmeditem(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldcode = models.CharField(max_length=150, blank=True, null=True)
    flditem = models.CharField(max_length=255, blank=True, null=True)
    fldpatinfo = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=150, blank=True, null=True)
    flduserid_order = models.CharField(max_length=25, blank=True, null=True)
    fldtime_order = models.DateTimeField(blank=True, null=True)
    fldcomp_order = models.CharField(max_length=50, blank=True, null=True)
    fldsave_order = models.IntegerField(blank=True, null=True)
    fldorder = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatmeditem'


class Tblpatplanning(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldplancategory = models.CharField(max_length=150, blank=True, null=True)
    fldproblem = models.CharField(max_length=250, blank=True, null=True)
    fldsubjective = models.TextField(blank=True, null=True)
    fldobjective = models.TextField(blank=True, null=True)
    fldassess = models.TextField(blank=True, null=True)
    fldplan = models.TextField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatplanning'


class Tblpatradiosubtable(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.BigIntegerField(blank=True, null=True)
    fldsubexamid = models.BigIntegerField(blank=True, null=True)
    fldtype = models.CharField(max_length=150, blank=True, null=True)
    fldvariable = models.CharField(max_length=200, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldcolm2 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm3 = models.CharField(max_length=250, blank=True, null=True)
    fldcolm4 = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatradiosubtable'


class Tblpatradiosubtest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldsubtest = models.CharField(max_length=200, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.TextField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldparent = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatradiosubtest'


class Tblpatradiotest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.CharField(max_length=250, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldgroupid = models.BigIntegerField(blank=True, null=True)
    fldsampletype = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.TextField(blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldrefername = models.CharField(max_length=250, blank=True, null=True)
    fldcondition = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    flvisible = models.CharField(max_length=50, blank=True, null=True)
    fldnewdate = models.DateTimeField(blank=True, null=True)
    fldpacstudy = models.CharField(max_length=255, blank=True, null=True)
    fldtest_type = models.CharField(max_length=50, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    flduserid_report = models.CharField(max_length=25, blank=True, null=True)
    fldtime_report = models.DateTimeField(blank=True, null=True)
    fldcomp_report = models.CharField(max_length=50, blank=True, null=True)
    fldsave_report = models.IntegerField(blank=True, null=True)
    flduptime_report = models.DateTimeField(blank=True, null=True)
    flduserid_verify = models.CharField(max_length=25, blank=True, null=True)
    fldtime_verify = models.DateTimeField(blank=True, null=True)
    fldcomp_verify = models.CharField(max_length=50, blank=True, null=True)
    fldsave_verify = models.IntegerField(blank=True, null=True)
    flduptime_verify = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldsampleid = models.CharField(max_length=250, blank=True, null=True)
    fldupuser_verify = models.CharField(max_length=25, blank=True, null=True)
    fldupuser_report = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatradiotest'


class Tblpatreport(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldflag = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)
    fldhashcode = models.CharField(max_length=250, blank=True, null=True)
    flvisible = models.CharField(max_length=50, blank=True, null=True)
    fldextension = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatreport'


class Tblpatserialimage(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldmode = models.CharField(max_length=250, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldtitle = models.CharField(max_length=250, blank=True, null=True)
    fldkeyword = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatserialimage'


class Tblpatsubgeneral(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemid = models.BigIntegerField(blank=True, null=True)
    fldchapter = models.CharField(max_length=200, blank=True, null=True)
    fldreportquali = models.CharField(max_length=250, blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    fldreport = models.TextField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatsubgeneral'


class Tblpatsubs(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpatno = models.CharField(max_length=50, blank=True, null=True)
    fldpatlen = models.IntegerField(blank=True, null=True)
    fldencid = models.CharField(max_length=50, blank=True, null=True)
    fldenclen = models.IntegerField(blank=True, null=True)
    fldbooking = models.CharField(max_length=50, blank=True, null=True)
    fldbooklen = models.IntegerField(blank=True, null=True)
    fldhospcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatsubs'


class Tblpattiming(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtype = models.CharField(max_length=250, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldbillitem = models.CharField(max_length=250, blank=True, null=True)
    fldfirstreport = models.CharField(max_length=250, blank=True, null=True)
    fldfirstuserid = models.CharField(max_length=25, blank=True, null=True)
    fldfirsttime = models.DateTimeField(blank=True, null=True)
    fldfirstcomp = models.CharField(max_length=50, blank=True, null=True)
    fldfirstsave = models.IntegerField(blank=True, null=True)
    fldsecondreport = models.CharField(max_length=250, blank=True, null=True)
    fldseconduserid = models.CharField(max_length=25, blank=True, null=True)
    fldsecondtime = models.DateTimeField(blank=True, null=True)
    fldsecondcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsecondsave = models.IntegerField(blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpattiming'


class Tblpatusershares(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldbillid = models.BigIntegerField(blank=True, null=True)
    fldsharetype = models.CharField(max_length=25, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldshareuser = models.CharField(max_length=25, blank=True, null=True)
    fldsharename = models.CharField(max_length=250, blank=True, null=True)
    fldtotalper = models.FloatField(blank=True, null=True)
    flduserper = models.FloatField(blank=True, null=True)
    flduseramt = models.FloatField(blank=True, null=True)
    fldusertax = models.FloatField(blank=True, null=True)
    fldactive = models.CharField(max_length=25, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpatusershares'


class Tblpayment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldpayamount = models.FloatField(blank=True, null=True)
    fldpaytype = models.CharField(max_length=50, blank=True, null=True)
    fldchequeno = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldpaidby = models.CharField(max_length=250, blank=True, null=True)
    fldpaidbypost = models.CharField(max_length=250, blank=True, null=True)
    fldrecvby = models.CharField(max_length=250, blank=True, null=True)
    fldrecvbypost = models.CharField(max_length=250, blank=True, null=True)
    fldrecvbycontact = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpayment'


class Tblpersonal(models.Model):
    perid = models.BigAutoField(primary_key=True)
    fldcateg = models.CharField(max_length=50, blank=True, null=True)
    fldblob = models.TextField(blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    fldextension = models.CharField(max_length=10, blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpersonal'


class Tblpersonimage(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcateg = models.CharField(max_length=250, blank=True, null=True)
    fldname = models.CharField(max_length=250, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    fldxyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpersonimage'


class Tblpreduebilling(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    fldbillitem = models.CharField(max_length=250, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)
    fldtaxper = models.FloatField(blank=True, null=True)
    flddiscper = models.FloatField(blank=True, null=True)
    fldditemamt = models.FloatField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldalert = models.IntegerField(blank=True, null=True)
    fldextracol = models.CharField(max_length=250, blank=True, null=True)
    fldextrarow = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpreduebilling'


class Tblprepatbilling(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    flditemno = models.BigIntegerField(blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemrate = models.FloatField(blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)
    fldtaxper = models.FloatField(blank=True, null=True)
    flddiscper = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    flddiscamt = models.FloatField(blank=True, null=True)
    fldditemamt = models.FloatField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldparent = models.BigIntegerField(blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldtarget = models.CharField(max_length=50, blank=True, null=True)
    fldpayto = models.CharField(max_length=25, blank=True, null=True)
    fldrefer = models.CharField(max_length=25, blank=True, null=True)
    fldsample = models.CharField(max_length=50, blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    flddisctype = models.CharField(max_length=150, blank=True, null=True)
    fldacledger = models.CharField(max_length=250, blank=True, null=True)
    fldcurrlocat = models.CharField(max_length=100, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldreason = models.CharField(max_length=250, blank=True, null=True)
    fldretbill = models.CharField(max_length=250, blank=True, null=True)
    fldretqty = models.FloatField(blank=True, null=True)
    fldalert = models.IntegerField(blank=True, null=True)
    fldextracol = models.CharField(max_length=250, blank=True, null=True)
    fldextrarow = models.CharField(max_length=250, blank=True, null=True)
    fldclaimid = models.CharField(max_length=250, blank=True, null=True)
    fldclaimstate = models.CharField(max_length=250, blank=True, null=True)
    fldextradata = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprepatbilling'


class Tblprocedure(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprocedure'


class Tblprocedureshare(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsharetype = models.CharField(max_length=100, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldusertype = models.CharField(max_length=150, blank=True, null=True)
    fldmaxshare = models.FloatField(blank=True, null=True)
    flditemshare = models.FloatField(blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    flditemtax = models.FloatField(blank=True, null=True)
    flddefault = models.CharField(max_length=150, blank=True, null=True)
    fldactive = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprocedureshare'


class Tblprocedureuser(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprocedureuser'


class Tblprocname(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldprocname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprocname'


class Tblproductgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldmedgroup = models.CharField(max_length=150, blank=True, null=True)
    fldroute = models.CharField(max_length=25, blank=True, null=True)
    flditem = models.CharField(max_length=255, blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    flddoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldfreq = models.CharField(max_length=50, blank=True, null=True)
    fldday = models.IntegerField(blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldstart = models.IntegerField(blank=True, null=True)
    fldadvice = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblproductgroup'


class Tblpurchase(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpurtype = models.CharField(max_length=25, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldmrp = models.FloatField(blank=True, null=True)
    flsuppcost = models.FloatField(blank=True, null=True)
    fldcasdisc = models.FloatField(blank=True, null=True)
    fldcasbonus = models.FloatField(blank=True, null=True)
    fldqtybonus = models.FloatField(blank=True, null=True)
    fldcarcost = models.FloatField(blank=True, null=True)
    fldnetcost = models.FloatField(blank=True, null=True)
    fldmargin = models.FloatField(blank=True, null=True)
    fldsellprice = models.FloatField(blank=True, null=True)
    fldtotalqty = models.FloatField(blank=True, null=True)
    fldreturnqty = models.FloatField(blank=True, null=True)
    fldtotalcost = models.FloatField(blank=True, null=True)
    fldpurdate = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    fldpurorder = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpurchase'


class Tblpurchasebill(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldpurtype = models.CharField(max_length=25, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    flddebit = models.FloatField(blank=True, null=True)
    fldcredit = models.FloatField(blank=True, null=True)
    fldtotaltax = models.FloatField(blank=True, null=True)
    fldlastdisc = models.FloatField(blank=True, null=True)
    fldpurdate = models.DateTimeField(blank=True, null=True)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldadjust = models.FloatField(blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldpurorder = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpurchasebill'


class Tblpurorder(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldrate = models.FloatField(blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldverify = models.CharField(max_length=150, blank=True, null=True)
    fldverify_time = models.DateTimeField(blank=True, null=True)
    fldconfirm = models.CharField(max_length=150, blank=True, null=True)
    fldconfirm_time = models.DateTimeField(blank=True, null=True)
    fldrecvref = models.CharField(max_length=250, blank=True, null=True)
    fldrecvuserid = models.CharField(max_length=25, blank=True, null=True)
    fldrecvtime = models.DateTimeField(blank=True, null=True)
    flddelivery = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblpurorder'


class Tblradio(models.Model):
    fldexamid = models.CharField(primary_key=True, max_length=200)
    fldcaption = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    fldcritical = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblradio'


class Tblradiocomment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldmax = models.FloatField(blank=True, null=True)
    fldmin = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblradiocomment'


class Tblradiolimit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldminimum = models.FloatField(blank=True, null=True)
    fldmaximum = models.FloatField(blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldnormal = models.FloatField(blank=True, null=True)
    fldhigh = models.FloatField(blank=True, null=True)
    fldlow = models.FloatField(blank=True, null=True)
    fldunit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblradiolimit'


class Tblradiooption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblradiooption'


class Tblradioquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsubexam = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblradioquali'


class Tblreconstfluid(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblreconstfluid'


class Tblreferlist(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldlocation = models.CharField(max_length=250, blank=True, null=True)
    fldcode = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblreferlist'


class Tblregimen(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldroute = models.CharField(max_length=25, blank=True, null=True)
    fldcodename = models.CharField(max_length=150, blank=True, null=True)
    flddisease = models.CharField(max_length=255, blank=True, null=True)
    flddosetype = models.CharField(max_length=25, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldgender = models.CharField(max_length=25, blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    flddoseunit = models.CharField(max_length=25, blank=True, null=True)
    fldfreq = models.CharField(max_length=50, blank=True, null=True)
    fldday = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblregimen'


class Tblrelations(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblrelations'


class Tblremotefollow(models.Model):
    fldencounterval = models.CharField(primary_key=True, max_length=150)
    flddept = models.CharField(max_length=50, blank=True, null=True)
    fldstart = models.DateTimeField(blank=True, null=True)
    fldend = models.DateTimeField(blank=True, null=True)
    flddata = models.IntegerField(blank=True, null=True)
    fldimage = models.IntegerField(blank=True, null=True)
    fldmedia = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=150, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblremotefollow'


class Tblremoteusers(models.Model):
    fldemail = models.CharField(primary_key=True, max_length=250)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    flddiscount = models.CharField(max_length=150, blank=True, null=True)
    fldadmitfile = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldencrypt = models.IntegerField(blank=True, null=True)
    fldpassword = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldhashcode = models.CharField(max_length=250, blank=True, null=True)
    fldvertime = models.DateTimeField(blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)
    fldethniccode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblremoteusers'


class Tblrepomapping(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=200, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblrepomapping'


class Tblreportgroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=250, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flditemname = models.CharField(unique=True, max_length=200, blank=True, null=True)
    fldactive = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblreportgroup'


class Tblreportlog(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldwindow = models.CharField(max_length=50, blank=True, null=True)
    fldfile = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblreportlog'


class Tblreportuser(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldname = models.CharField(max_length=150, blank=True, null=True)
    fldnamefont = models.CharField(max_length=250, blank=True, null=True)
    fldsigimage = models.TextField(blank=True, null=True)
    fldtitle = models.CharField(max_length=150, blank=True, null=True)
    flddetail = models.CharField(max_length=250, blank=True, null=True)
    flddefault = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblreportuser'


class Tblrequest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldfinalqty = models.FloatField(blank=True, null=True)
    fldurgent = models.CharField(max_length=50, blank=True, null=True)
    fldexpdate = models.DateTimeField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldremarks = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblrequest'


class Tblresearch(models.Model):
    fldstudycode = models.CharField(primary_key=True, max_length=150)
    fldstudyname = models.CharField(max_length=250, blank=True, null=True)
    fldstudylocat = models.CharField(max_length=250, blank=True, null=True)
    fldsamplesize = models.IntegerField(blank=True, null=True)
    fldstudystart = models.DateTimeField(blank=True, null=True)
    fldstudyend = models.DateTimeField(blank=True, null=True)
    fldstudysample = models.TextField(blank=True, null=True)
    fldstudycriteria = models.TextField(blank=True, null=True)
    fldircconsentpic = models.TextField(blank=True, null=True)
    fldircconsentlink = models.CharField(max_length=250, blank=True, null=True)
    fldconsentformpic = models.TextField(blank=True, null=True)
    fldconsentformlink = models.CharField(max_length=250, blank=True, null=True)
    fldiintervireformpic = models.TextField(blank=True, null=True)
    fldinterviewformlink = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblresearch'


class Tblsampletype(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsampletype = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsampletype'


class Tblschedule(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldtime = models.CharField(max_length=50, blank=True, null=True)
    fldfromtime = models.DateTimeField(blank=True, null=True)
    fldtotime = models.DateTimeField(blank=True, null=True)
    fldday = models.CharField(max_length=50, blank=True, null=True)
    flddaysvalue = models.CharField(max_length=250, blank=True, null=True)
    fldmonth = models.CharField(max_length=50, blank=True, null=True)
    fldmonthsvalue = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblschedule'


class Tblschemecategory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldpackage = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblschemecategory'


class Tblsensidrugs(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flclass = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsensidrugs'


class Tblservicecost(models.Model):
    flditemname = models.CharField(primary_key=True, max_length=250)
    flditemcode = models.CharField(max_length=100, blank=True, null=True)
    fldcode = models.CharField(max_length=50, blank=True, null=True)
    fldid = models.IntegerField(blank=True, null=True)
    fldbillitem = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flditemcost = models.FloatField(blank=True, null=True)
    flditemunit = models.CharField(max_length=50, blank=True, null=True)
    fldtarget = models.CharField(max_length=50, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldgroup = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.CharField(max_length=200, blank=True, null=True)
    fldtaxcode = models.CharField(max_length=150, blank=True, null=True)
    fldeditrate = models.IntegerField(blank=True, null=True)
    fldeditdisc = models.IntegerField(blank=True, null=True)
    fldpatentry = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldpayable = models.IntegerField(blank=True, null=True)
    fldhospitalshare = models.FloatField(blank=True, null=True)
    fldinstrumshare = models.FloatField(blank=True, null=True)
    flddepartshare = models.FloatField(blank=True, null=True)
    fldanesthshare = models.FloatField(blank=True, null=True)
    fldothershare = models.FloatField(blank=True, null=True)
    fldwaitday = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblservicecost'


class TblservicecostLog(models.Model):
    fldsno = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemcode = models.CharField(max_length=100, blank=True, null=True)
    fldcode = models.CharField(max_length=50, blank=True, null=True)
    fldid = models.IntegerField(blank=True, null=True)
    fldbillitem = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flditemcost = models.FloatField(blank=True, null=True)
    flditemunit = models.CharField(max_length=50, blank=True, null=True)
    fldtarget = models.CharField(max_length=50, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldgroup = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.CharField(max_length=200, blank=True, null=True)
    fldtaxcode = models.CharField(max_length=150, blank=True, null=True)
    fldeditrate = models.IntegerField(blank=True, null=True)
    fldeditdisc = models.IntegerField(blank=True, null=True)
    fldpatentry = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcurrtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblservicecost_log'


class Tblservicegroup(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=200, blank=True, null=True)
    flditemtype = models.CharField(max_length=100, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemqty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblservicegroup'


class Tblsettings(models.Model):
    fldindex = models.CharField(primary_key=True, max_length=250)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsettings'


class Tblsharepayment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldpayto = models.CharField(max_length=25, blank=True, null=True)
    fldfrom = models.DateTimeField(blank=True, null=True)
    fldto = models.DateTimeField(blank=True, null=True)
    fldshareamt = models.FloatField(blank=True, null=True)
    fldtdsper = models.FloatField(blank=True, null=True)
    fldsharenet = models.FloatField(blank=True, null=True)
    fldextra = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsharepayment'


class Tblsmslog(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldwindow = models.CharField(max_length=50, blank=True, null=True)
    fldtarget = models.CharField(max_length=150, blank=True, null=True)
    fldsmstext = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.TextField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldsmsdate = models.DateTimeField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsmslog'


class Tblsociallist(models.Model):
    fldptcode = models.CharField(primary_key=True, max_length=250)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldserviceid = models.CharField(max_length=150, blank=True, null=True)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldjoindate = models.DateTimeField(blank=True, null=True)
    fldenddate = models.DateTimeField(blank=True, null=True)
    fldactivity = models.CharField(max_length=25, blank=True, null=True)
    fldpatientval = models.CharField(unique=True, max_length=250, blank=True, null=True)
    flddisctype = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldcitizen = models.CharField(max_length=250, blank=True, null=True)
    fldidentify = models.CharField(max_length=250, blank=True, null=True)
    fldscheme = models.CharField(max_length=200, blank=True, null=True)
    fldservice = models.CharField(max_length=250, blank=True, null=True)
    fldreferhosp = models.CharField(max_length=250, blank=True, null=True)
    fldreferdist = models.CharField(max_length=250, blank=True, null=True)
    fldreferdate = models.DateTimeField(blank=True, null=True)
    fldsocialmode = models.CharField(max_length=250, blank=True, null=True)
    fldcreditlim = models.FloatField(blank=True, null=True)
    fldcreditdate = models.DateTimeField(blank=True, null=True)
    flddisclimit = models.FloatField(blank=True, null=True)
    flddiscdate = models.DateTimeField(blank=True, null=True)
    fldremark = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsociallist'


class Tblssfclaim(models.Model):
    fldclaimid = models.CharField(primary_key=True, max_length=150)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldptcode = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)
    fldscheme = models.CharField(max_length=100, blank=True, null=True)
    fldsubproduct = models.CharField(max_length=100, blank=True, null=True)
    fldwound = models.CharField(max_length=100, blank=True, null=True)
    fldinjury = models.CharField(max_length=100, blank=True, null=True)
    flddisable = models.CharField(max_length=100, blank=True, null=True)
    flddead = models.CharField(max_length=100, blank=True, null=True)
    fldaccident = models.CharField(max_length=100, blank=True, null=True)
    fldsickness = models.CharField(max_length=100, blank=True, null=True)
    flddischarge = models.CharField(max_length=100, blank=True, null=True)
    flddischsumm = models.CharField(max_length=100, blank=True, null=True)
    fldcancer = models.CharField(max_length=100, blank=True, null=True)
    fldhiv = models.CharField(max_length=100, blank=True, null=True)
    fldheart = models.CharField(max_length=100, blank=True, null=True)
    fldhighbp = models.CharField(max_length=100, blank=True, null=True)
    flddiabetes = models.CharField(max_length=100, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldemployer = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblssfclaim'


class Tblstafflist(models.Model):
    fldptcode = models.CharField(primary_key=True, max_length=250)
    fldptnamefir = models.CharField(max_length=150, blank=True, null=True)
    fldptnamelast = models.CharField(max_length=150, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldptaddvill = models.CharField(max_length=150, blank=True, null=True)
    fldptadddist = models.CharField(max_length=150, blank=True, null=True)
    fldptcontact = models.CharField(max_length=150, blank=True, null=True)
    fldptbirday = models.DateTimeField(blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldcitizen = models.CharField(max_length=250, blank=True, null=True)
    fldgovtaccount = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldbankaccount = models.CharField(max_length=250, blank=True, null=True)
    fldtaxpercent = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(unique=True, max_length=25, blank=True, null=True)
    flddept = models.CharField(max_length=250, blank=True, null=True)
    fldjoindate = models.DateTimeField(blank=True, null=True)
    fldenddate = models.DateTimeField(blank=True, null=True)
    fldcontype = models.CharField(max_length=200, blank=True, null=True)
    fldpost = models.CharField(max_length=200, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldrank = models.CharField(max_length=250, blank=True, null=True)
    fldunit = models.CharField(max_length=250, blank=True, null=True)
    fldidentify = models.CharField(max_length=250, blank=True, null=True)
    fldremark = models.CharField(max_length=250, blank=True, null=True)
    fldreligion = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldpatientval = models.CharField(max_length=250, blank=True, null=True)
    flddisctype = models.CharField(max_length=250, blank=True, null=True)
    fldptaddward = models.CharField(max_length=150, blank=True, null=True)
    fldptguardian = models.CharField(max_length=250, blank=True, null=True)
    fldrelation = models.CharField(max_length=250, blank=True, null=True)
    fldserviceid = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstafflist'


class Tblstockrate(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    flddrug = models.CharField(max_length=200, blank=True, null=True)
    flddrugcode = models.CharField(max_length=200, blank=True, null=True)
    fldpackvol = models.FloatField(blank=True, null=True)
    fldstockid = models.CharField(max_length=200, blank=True, null=True)
    fldrate = models.FloatField(blank=True, null=True)
    fldnullrate = models.IntegerField(blank=True, null=True)
    fldmaxqty = models.FloatField(blank=True, null=True)
    fldwaitday = models.IntegerField(blank=True, null=True)
    fldclaimtype = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstockrate'


class TblstockrateOld(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    flddrug = models.CharField(max_length=200, blank=True, null=True)
    fldpackvol = models.FloatField(blank=True, null=True)
    fldstockid = models.CharField(max_length=200, blank=True, null=True)
    fldrate = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    flddrugcode = models.CharField(max_length=200, blank=True, null=True)
    fldclaimtype = models.CharField(max_length=50, blank=True, null=True)
    fldnullrate = models.IntegerField(blank=True, null=True)
    fldmaxqty = models.FloatField(blank=True, null=True)
    fldwaitday = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstockrate_old'


class Tblstockreturn(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldcost = models.FloatField(blank=True, null=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldnewreference = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstockreturn'


class Tblstructexam(models.Model):
    fldheadcode = models.CharField(primary_key=True, max_length=250)
    fldclass = models.CharField(max_length=250, blank=True, null=True)
    fldsubclass = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    flditemid = models.IntegerField(blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldheadid = models.IntegerField(blank=True, null=True)
    fldhead = models.CharField(max_length=250, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    fldtesttype = models.CharField(max_length=50, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldreferencee = models.CharField(max_length=150, blank=True, null=True)
    fldclininfo = models.CharField(max_length=255, blank=True, null=True)
    fldlock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstructexam'


class Tblstructexamoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldhead = models.CharField(max_length=250, blank=True, null=True)
    fldheadcode = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldlock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstructexamoption'


class Tblsubexamquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsubexam = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsubexamquali'


class Tblsubradioquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldexamid = models.CharField(max_length=200, blank=True, null=True)
    fldsubexam = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsubradioquali'


class Tblsubsymptoms(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsymptom = models.CharField(max_length=250, blank=True, null=True)
    fldsubsymptom = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsubsymptoms'


class Tblsubtestquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldsubtest = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsubtestquali'


class Tblsupplier(models.Model):
    fldsuppname = models.CharField(primary_key=True, max_length=250)
    fldsuppaddress = models.CharField(max_length=250, blank=True, null=True)
    fldsupppan = models.CharField(max_length=250, blank=True, null=True)
    fldsuppledger = models.CharField(max_length=250, blank=True, null=True)
    fldsuppphone = models.CharField(max_length=250, blank=True, null=True)
    fldcontactname = models.CharField(max_length=250, blank=True, null=True)
    fldcontactphone = models.CharField(max_length=250, blank=True, null=True)
    fldstartdate = models.DateTimeField(blank=True, null=True)
    fldpaymentmode = models.CharField(max_length=25, blank=True, null=True)
    fldcreditday = models.FloatField(blank=True, null=True)
    fldactive = models.CharField(max_length=10, blank=True, null=True)
    fldpaiddebit = models.FloatField(blank=True, null=True)
    fldleftcredit = models.FloatField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldsuppemail = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsupplier'


class Tblsurgbrand(models.Model):
    fldbrandid = models.CharField(primary_key=True, max_length=250)
    fldsurgid = models.CharField(max_length=200, blank=True, null=True)
    fldbrand = models.CharField(max_length=50, blank=True, null=True)
    fldmanufacturer = models.CharField(max_length=200, blank=True, null=True)
    flddetail = models.CharField(max_length=255, blank=True, null=True)
    fldstandard = models.CharField(max_length=25, blank=True, null=True)
    fldmaxqty = models.FloatField(blank=True, null=True)
    fldminqty = models.FloatField(blank=True, null=True)
    fldleadtime = models.IntegerField(blank=True, null=True)
    fldtaxcode = models.CharField(max_length=150, blank=True, null=True)
    fldactive = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurgbrand'


class Tblsurgicalname(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsurgcateg = models.CharField(max_length=25, blank=True, null=True)
    fldsurgname = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurgicalname'


class Tblsurgicals(models.Model):
    fldsurgid = models.CharField(primary_key=True, max_length=200)
    fldsurgname = models.CharField(max_length=125, blank=True, null=True)
    fldsurgcateg = models.CharField(max_length=25, blank=True, null=True)
    fldsurgsize = models.CharField(max_length=25, blank=True, null=True)
    fldsurgtype = models.CharField(max_length=25, blank=True, null=True)
    fldsurgcode = models.CharField(max_length=25, blank=True, null=True)
    fldsurgdetail = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurgicals'


class Tblsurname(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurname'


class Tblsurveillance(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldgroup = models.CharField(max_length=250, blank=True, null=True)
    flddisease = models.CharField(max_length=250, blank=True, null=True)
    fldcodeid = models.CharField(max_length=250, blank=True, null=True)
    fldcodenew = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurveillance'


class Tblsuturetype(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsuturetype = models.CharField(max_length=250, blank=True, null=True)
    fldsuturecode = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsuturetype'


class Tblsymptoms(models.Model):
    fldsymptom = models.CharField(primary_key=True, max_length=250)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldsymdetail = models.CharField(max_length=250, blank=True, null=True)
    fldcode = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsymptoms'


class Tblsyndrobrady(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsyndrobrady'


class Tblsyndrohyper(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsyndrohyper'


class Tblsyndrohypo(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsyndrohypo'


class Tblsyndromes(models.Model):
    fldsyndrome = models.CharField(primary_key=True, max_length=250)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldsymcode = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsyndromes'


class Tblsyndrotachy(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    fldtype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsyndrotachy'


class Tblsysconst(models.Model):
    fldsysconst = models.CharField(primary_key=True, max_length=150)
    fldcategory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsysconst'


class Tblsystemlog(models.Model):
    fldindex = models.CharField(primary_key=True, max_length=250)
    flduser = models.CharField(max_length=25, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldlogin = models.CharField(max_length=50, blank=True, null=True)
    fldentrytime = models.DateTimeField(blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    flddevicepath = models.CharField(max_length=250, blank=True, null=True)
    fldversion = models.CharField(max_length=100, blank=True, null=True)
    fldmainserver = models.CharField(max_length=250, blank=True, null=True)
    fldreadserver = models.CharField(max_length=250, blank=True, null=True)
    fldfallserver = models.CharField(max_length=250, blank=True, null=True)
    fldftpserver = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsystemlog'


class Tbltabsettings(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcategory = models.CharField(max_length=250, blank=True, null=True)
    fldvalue = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltabsettings'


class Tbltaperdose(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flddoseno = models.BigIntegerField(blank=True, null=True)
    flddose = models.FloatField(blank=True, null=True)
    fldfreq = models.CharField(max_length=25, blank=True, null=True)
    flddays = models.FloatField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltaperdose'


class Tbltarget(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltarget'


class Tbltaxgroup(models.Model):
    fldgroup = models.CharField(primary_key=True, max_length=150)
    fldtaxper = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltaxgroup'


class Tbltelemedtalk(models.Model):
    fldtalkid = models.CharField(primary_key=True, max_length=250)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldpatientval = models.CharField(max_length=150, blank=True, null=True)
    fldhospital = models.CharField(max_length=250, blank=True, null=True)
    fldteleuser = models.CharField(max_length=25, blank=True, null=True)
    fldsms = models.IntegerField(blank=True, null=True)
    fldurgency = models.CharField(max_length=150, blank=True, null=True)
    fldvidroom = models.CharField(max_length=250, blank=True, null=True)
    fldvidpass = models.CharField(max_length=250, blank=True, null=True)
    fldvidserver = models.CharField(max_length=250, blank=True, null=True)
    fldrequest = models.TextField(blank=True, null=True)
    fldorduserid = models.CharField(max_length=25, blank=True, null=True)
    fldordtime = models.DateTimeField(blank=True, null=True)
    fldordcomp = models.CharField(max_length=50, blank=True, null=True)
    fldresponse = models.TextField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldcoment = models.CharField(max_length=250, blank=True, null=True)
    fldupuser = models.CharField(max_length=25, blank=True, null=True)
    flduptime = models.DateTimeField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltelemedtalk'


class Tbltelemeduser(models.Model):
    fldteleuser = models.CharField(primary_key=True, max_length=25)
    fldusername = models.CharField(max_length=250, blank=True, null=True)
    fldpass = models.CharField(max_length=250, blank=True, null=True)
    fldroot = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldcontact = models.CharField(max_length=150, blank=True, null=True)
    fldemail = models.CharField(max_length=250, blank=True, null=True)
    fldfromdate = models.DateTimeField(blank=True, null=True)
    fldtodate = models.DateTimeField(blank=True, null=True)
    fldusercode = models.CharField(max_length=250, blank=True, null=True)
    fldhospital = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldgovtaccount = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldbankaccount = models.CharField(max_length=250, blank=True, null=True)
    fldtaxpercent = models.FloatField(blank=True, null=True)
    fldcharge = models.FloatField(blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltelemeduser'


class Tbltelradiosubtest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsubtestno = models.BigIntegerField(blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.BigIntegerField(blank=True, null=True)
    fldparent = models.CharField(max_length=250, blank=True, null=True)
    fldsubtest = models.CharField(max_length=200, blank=True, null=True)
    fldindex = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldreport = models.TextField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltelradiosubtest'


class Tbltelradiotest(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestno = models.BigIntegerField(blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldtestid = models.CharField(max_length=250, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldgroupid = models.BigIntegerField(blank=True, null=True)
    fldsampletype = models.CharField(max_length=250, blank=True, null=True)
    fldsampleid = models.CharField(max_length=250, blank=True, null=True)
    fldreportquali = models.TextField(blank=True, null=True)
    fldreportquanti = models.FloatField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)
    fldstatus = models.CharField(max_length=250, blank=True, null=True)
    fldprint = models.IntegerField(blank=True, null=True)
    fldfilepath = models.CharField(max_length=250, blank=True, null=True)
    fldrefername = models.CharField(max_length=250, blank=True, null=True)
    fldcondition = models.CharField(max_length=250, blank=True, null=True)
    fldcomment = models.CharField(max_length=255, blank=True, null=True)
    flvisible = models.CharField(max_length=50, blank=True, null=True)
    fldnewdate = models.DateTimeField(blank=True, null=True)
    fldpacstudy = models.CharField(max_length=255, blank=True, null=True)
    fldpacseries = models.CharField(max_length=255, blank=True, null=True)
    fldpacsform = models.CharField(max_length=25, blank=True, null=True)
    fldtest_type = models.CharField(max_length=50, blank=True, null=True)
    fldbillno = models.CharField(max_length=250, blank=True, null=True)
    fldchk = models.IntegerField(blank=True, null=True)
    fldorder = models.IntegerField(blank=True, null=True)
    flduserid_report = models.CharField(max_length=25, blank=True, null=True)
    fldtime_report = models.DateTimeField(blank=True, null=True)
    fldcomp_report = models.CharField(max_length=50, blank=True, null=True)
    fldsave_report = models.IntegerField(blank=True, null=True)
    flduptime_report = models.DateTimeField(blank=True, null=True)
    fldupuser_report = models.CharField(max_length=25, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltelradiotest'


class Tbltempbilldetail(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    fldbillno = models.CharField(unique=True, max_length=250, blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    fldtaxamt = models.FloatField(blank=True, null=True)
    fldtaxgroup = models.CharField(max_length=150, blank=True, null=True)
    flddiscountamt = models.FloatField(blank=True, null=True)
    flddiscountgroup = models.CharField(max_length=150, blank=True, null=True)
    fldchargedamt = models.FloatField(blank=True, null=True)
    fldreceivedamt = models.FloatField(blank=True, null=True)
    fldcurdeposit = models.FloatField(blank=True, null=True)
    flddepoadjust = models.FloatField(blank=True, null=True)
    fldbilltype = models.CharField(max_length=25, blank=True, null=True)
    fldchequeno = models.CharField(max_length=250, blank=True, null=True)
    fldbankname = models.CharField(max_length=250, blank=True, null=True)
    fldprevdeposit = models.IntegerField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltempbilldetail'


class Tbltenderlist(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsuppname = models.CharField(max_length=250, blank=True, null=True)
    flditemtype = models.CharField(max_length=25, blank=True, null=True)
    fldfromdate = models.DateTimeField(blank=True, null=True)
    fldtodate = models.DateTimeField(blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldtotalqty = models.FloatField(blank=True, null=True)
    fldmaxcost = models.FloatField(blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltenderlist'


class Tbltest(models.Model):
    fldtestid = models.CharField(primary_key=True, max_length=200)
    fldcaption = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldsysconst = models.CharField(max_length=100, blank=True, null=True)
    fldspecimen = models.CharField(max_length=250, blank=True, null=True)
    fldcollection = models.CharField(max_length=250, blank=True, null=True)
    flddetail = models.TextField(blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldoption = models.CharField(max_length=50, blank=True, null=True)
    fldcritical = models.FloatField(blank=True, null=True)
    fldspecmcode = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltest'


class Tbltestcomment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldmax = models.FloatField(blank=True, null=True)
    fldmin = models.FloatField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldunit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestcomment'


class Tbltestcondition(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestcondition = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestcondition'


class Tbltestlimit(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldmethod = models.CharField(max_length=250, blank=True, null=True)
    fldminimum = models.FloatField(blank=True, null=True)
    fldmaximum = models.FloatField(blank=True, null=True)
    fldsensitivity = models.FloatField(blank=True, null=True)
    fldspecificity = models.FloatField(blank=True, null=True)
    fldptsex = models.CharField(max_length=10, blank=True, null=True)
    fldagegroup = models.CharField(max_length=25, blank=True, null=True)
    fldconvfactor = models.FloatField(blank=True, null=True)
    fldsinormal = models.FloatField(blank=True, null=True)
    fldsihigh = models.FloatField(blank=True, null=True)
    fldsilow = models.FloatField(blank=True, null=True)
    fldsiunit = models.CharField(max_length=25, blank=True, null=True)
    fldmetnormal = models.FloatField(blank=True, null=True)
    fldmethigh = models.FloatField(blank=True, null=True)
    fldmetlow = models.FloatField(blank=True, null=True)
    fldmetunit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestlimit'


class Tbltestmachine(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=250, blank=True, null=True)
    fldvendor = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestmachine'


class Tbltestmethod(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldmethod = models.CharField(max_length=150, blank=True, null=True)
    fldcateg = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestmethod'


class Tbltestoption(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldanswertype = models.CharField(max_length=50, blank=True, null=True)
    fldanswer = models.CharField(max_length=250, blank=True, null=True)
    fldscale = models.FloatField(blank=True, null=True)
    fldscalegroup = models.CharField(max_length=250, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)
    fldabnormal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestoption'


class Tbltestquali(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldtestid = models.CharField(max_length=200, blank=True, null=True)
    fldsubtest = models.CharField(max_length=200, blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    fldtanswertype = models.CharField(max_length=50, blank=True, null=True)
    flddetail = models.CharField(max_length=255, blank=True, null=True)
    fldindex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltestquali'


class Tbltransfer(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldstockno = models.BigIntegerField(blank=True, null=True)
    fldoldstockno = models.BigIntegerField(blank=True, null=True)
    fldstockid = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)
    fldqty = models.FloatField(blank=True, null=True)
    fldnetcost = models.FloatField(blank=True, null=True)
    fldsellpr = models.FloatField(blank=True, null=True)
    fldsav = models.IntegerField(blank=True, null=True)
    fldfromentrytime = models.DateTimeField(blank=True, null=True)
    fldfromuser = models.CharField(max_length=25, blank=True, null=True)
    fldfromcomp = models.CharField(max_length=50, blank=True, null=True)
    fldfromsav = models.IntegerField(blank=True, null=True)
    fldtoentrytime = models.DateTimeField(blank=True, null=True)
    fldtouser = models.CharField(max_length=25, blank=True, null=True)
    fldtocomp = models.CharField(max_length=50, blank=True, null=True)
    fldtosav = models.IntegerField(blank=True, null=True)
    fldreference = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldcomment = models.CharField(max_length=250, blank=True, null=True)
    fldlockcomp = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltransfer'


class Tbltriage(models.Model):
    flid = models.BigAutoField(primary_key=True)
    fldparent = models.CharField(max_length=255, blank=True, null=True)
    flddiagnotype = models.CharField(max_length=25, blank=True, null=True)
    fldchild = models.CharField(max_length=200, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldrelation = models.CharField(max_length=25, blank=True, null=True)
    fldvalquali = models.CharField(max_length=250, blank=True, null=True)
    fldvalquanti = models.FloatField(blank=True, null=True)
    flddiagnounit = models.CharField(max_length=100, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)
    fldbaserate = models.FloatField(blank=True, null=True)
    fldhitrate = models.FloatField(blank=True, null=True)
    fldfalserate = models.FloatField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltriage'


class Tbluser(models.Model):
    flduserid = models.CharField(primary_key=True, max_length=25)
    fldusername = models.CharField(max_length=250, blank=True, null=True)
    fldpass = models.CharField(max_length=250, blank=True, null=True)
    fldroot = models.CharField(max_length=250, blank=True, null=True)
    fldcategory = models.CharField(max_length=100, blank=True, null=True)
    fldcode = models.IntegerField(blank=True, null=True)
    fldfromdate = models.DateTimeField(blank=True, null=True)
    fldtodate = models.DateTimeField(blank=True, null=True)
    fldusercode = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=50, blank=True, null=True)
    fldfaculty = models.IntegerField(blank=True, null=True)
    fldpayable = models.IntegerField(blank=True, null=True)
    fldreferral = models.IntegerField(blank=True, null=True)
    fldopconsult = models.IntegerField(blank=True, null=True)
    fldipconsult = models.IntegerField(blank=True, null=True)
    fldsigna = models.IntegerField(blank=True, null=True)
    fldreport = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldonline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluser'


class Tbluseraccess(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldaccess = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluseraccess'


class Tblusercategory(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcategory = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblusercategory'


class Tblusercollection(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldcashier = models.CharField(max_length=150, blank=True, null=True)
    fldfrominvoice = models.CharField(max_length=250, blank=True, null=True)
    fldtoinvoice = models.CharField(max_length=250, blank=True, null=True)
    fldfromreceipt = models.CharField(max_length=250, blank=True, null=True)
    fldtoreceipt = models.CharField(max_length=250, blank=True, null=True)
    fldfromvouch = models.CharField(max_length=250, blank=True, null=True)
    fldtovouch = models.CharField(max_length=250, blank=True, null=True)
    fldbillamt = models.FloatField(blank=True, null=True)
    fldretinvoice = models.CharField(max_length=250, blank=True, null=True)
    fldretamt = models.FloatField(blank=True, null=True)
    fldrecvamt = models.FloatField(blank=True, null=True)
    flddenomination = models.TextField(blank=True, null=True)
    fldshift = models.CharField(max_length=50, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    flduserid_verify = models.CharField(max_length=25, blank=True, null=True)
    fldtime_verify = models.DateTimeField(blank=True, null=True)
    fldcomp_verify = models.CharField(max_length=50, blank=True, null=True)
    fldstatus = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblusercollection'


class Tbluserformaccess(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldcategory = models.CharField(max_length=50, blank=True, null=True)
    fldformname = models.CharField(max_length=250, blank=True, null=True)
    fldstatus = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluserformaccess'


class Tbluserimage(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldpic = models.TextField(blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    fldhostuser = models.CharField(max_length=250, blank=True, null=True)
    fldhostip = models.CharField(max_length=250, blank=True, null=True)
    fldhostname = models.CharField(max_length=250, blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldtype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluserimage'


class Tbluserpay(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    flditemname = models.CharField(max_length=250, blank=True, null=True)
    flditemtype = models.CharField(max_length=200, blank=True, null=True)
    flditemshare = models.FloatField(blank=True, null=True)
    flditemamt = models.FloatField(blank=True, null=True)
    flditemtax = models.FloatField(blank=True, null=True)
    fldactive = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluserpay'


class Tblusershare(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldsharetype = models.CharField(max_length=100, blank=True, null=True)
    flditemtype = models.CharField(max_length=150, blank=True, null=True)
    fldbillingmode = models.CharField(max_length=150, blank=True, null=True)
    flddepartname = models.CharField(max_length=50, blank=True, null=True)
    fldmaxshare = models.FloatField(blank=True, null=True)
    flditemshare = models.FloatField(blank=True, null=True)
    flditemtax = models.FloatField(blank=True, null=True)
    fldactive = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblusershare'


class Tblvaccdosing(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditem = models.CharField(max_length=250, blank=True, null=True)
    fldtype = models.CharField(max_length=100, blank=True, null=True)
    fldvalue = models.FloatField(blank=True, null=True)
    fldunit = models.CharField(max_length=150, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)
    fldbatch = models.CharField(max_length=250, blank=True, null=True)
    fldstockno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblvaccdosing'


class Tblvaccine(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    flditem = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblvaccine'


class Tblwebpayment(models.Model):
    fldid = models.BigAutoField(primary_key=True)
    fldbillno = models.CharField(unique=True, max_length=250, blank=True, null=True)
    fldencounterval = models.CharField(max_length=150, blank=True, null=True)
    flditemid = models.CharField(max_length=250, blank=True, null=True)
    fldlink = models.CharField(max_length=250, blank=True, null=True)
    fldvendor = models.CharField(max_length=150, blank=True, null=True)
    fldvendormode = models.CharField(max_length=150, blank=True, null=True)
    fldstate = models.CharField(max_length=150, blank=True, null=True)
    fldtransid = models.CharField(max_length=250, blank=True, null=True)
    fldtransamt = models.FloatField(blank=True, null=True)
    fldtranstoken = models.CharField(max_length=250, blank=True, null=True)
    fldfeeamt = models.FloatField(blank=True, null=True)
    fldrefund = models.IntegerField(blank=True, null=True)
    fldtransdate = models.DateTimeField(blank=True, null=True)
    fldpayerid = models.CharField(max_length=250, blank=True, null=True)
    fldpayername = models.CharField(max_length=250, blank=True, null=True)
    fldpayermobile = models.CharField(max_length=150, blank=True, null=True)
    fldpayeremail = models.CharField(max_length=150, blank=True, null=True)
    fldmerchid = models.CharField(max_length=250, blank=True, null=True)
    fldmerchname = models.CharField(max_length=250, blank=True, null=True)
    fldmerchmobile = models.CharField(max_length=150, blank=True, null=True)
    fldmerchemail = models.CharField(max_length=150, blank=True, null=True)
    flduserid = models.CharField(max_length=25, blank=True, null=True)
    fldtime = models.DateTimeField(blank=True, null=True)
    fldcomp = models.CharField(max_length=50, blank=True, null=True)
    fldsave = models.IntegerField(blank=True, null=True)
    fldhostmac = models.CharField(max_length=250, blank=True, null=True)
    xyz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblwebpayment'
