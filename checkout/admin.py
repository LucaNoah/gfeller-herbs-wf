from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        "order_number",
        "date",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    fields = (
        "order_number",
        "user_account",
        "date",
        "order_total",
        "delivery_cost",
        "grand_total",
        "email_address",
        "full_name",
        "delivery_address",
        "town_or_city",
        "zip_code",
        "state",
        "country",
    )

    list_display = (
        "order_number",
        "full_name",
        "date",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
