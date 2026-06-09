class LegacyHMISRouter:
    """
    Route legacy_hmis app models to the legacy HMIS database.
    Route all other apps to the default PatPortal database.
    """

    legacy_app_labels = {"common"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.legacy_app_labels:
            return "common"

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.legacy_app_labels:
            return "common"

        return None

    def allow_relation(self, obj1, obj2, **hints):
        obj1_is_legacy = obj1._meta.app_label in self.legacy_app_labels
        obj2_is_legacy = obj2._meta.app_label in self.legacy_app_labels

        if obj1_is_legacy or obj2_is_legacy:
            return obj1_is_legacy and obj2_is_legacy

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.legacy_app_labels:
            return False

        return db == "default"