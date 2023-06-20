class User:
    def __init__(
        self,
        is_authenticated,
        is_active,
        is_foundation_farm_admin,
        is_commercial_farmers_admin,
        is_field_finance_admin,
        is_malawi_admin,
    ) -> None:
        self.is_authenticated = is_authenticated
        self.is_active = is_active
        self.is_foundation_farm_admin = is_foundation_farm_admin
        self.is_commercial_farmers_admin = is_commercial_farmers_admin
        self.is_field_finance_admin = is_field_finance_admin
        self.is_malawi_admin = is_malawi_admin
        # self.is_active = is_active
