from django.db import models


def default_dashboard_settings():
    return {
        "hospital_name": "MADAN BHANDARI HOSPITAL & TRAUMA CENTER",
        "company_name": "D-Code Technology Pvt. Ltd.",
        "theme_color": "blue",
        "auto_refresh_seconds": 30,
        "marquee_text": "Powered by D-Code Technology Pvt. Ltd.",
        "show_footer": True,
        "hospital_logo": "",
        "company_logo": "",
    }


class DashboardSetting(models.Model):
    key = models.CharField(max_length=100, unique=True, default="main")
    value = models.JSONField(default=default_dashboard_settings)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key