from __future__ import unicode_literals
from frappe import _
def get_data():
    config = [
        {
            "label": _("Customer"),
            "items": [
                {
                    "type": "doctype",
                    "name": "invoice",
                    "label": "Invoice",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "maintain customer",
                    "label": "Maintain Customer",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "customer contra",
                    "label": "Customer Contra",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "customer refund",
                    "label": "Customer Refund",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "customer payment",
                    "label": "Customer Payment",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "customer debit note",
                    "label": "Customer Debit Note",
                    "onboard": 6,
                },
                {
                    "type": "doctype",
                    "name": "customer credit note",
                    "label": "Customer Credit Note",
                    "onboard": 7,
                },
            ]
        },
        {
            "label": _("Supplier"),
            "items": [
                {
                    "type": "doctype",
                    "name": "supplier invoice",
                    "label": "Supplier Invoice",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "maintain supplier",
                    "label": "Maintain Supplier",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "supplier contra",
                    "label": "Supplier Contra",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "supplier refund",
                    "label": "Supplier Refund",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "supplier payment",
                    "label": "Supplier Payment",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "supplier debit note",
                    "label": "Supplier Debit Note",
                    "onboard": 6,
                },
                {
                    "type": "doctype",
                    "name": "supplier credit note",
                    "label": "Supplier Credit Note",
                    "onboard": 7,
                },
            ]

        },
        {
            "label": _("Sales"),
            "items": [
                {
                    "type": "doctype",
                    "name": "sql sales order",
                    "label": "Sales Order",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "sql quotation",
                    "label": "Quotation",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "delivery order",
                    "label": "Delivery Order",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "invoice",
                    "label": "Invoice",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "cash sales",
                    "label": "Cash Sales",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "credit note",
                    "label": "Credit Note",
                    "onboard": 6,
                },
                
            ]
        },
        {
            "label": _("Purchase"),
            "items": [
                {
                    "type": "doctype",
                    "name": "sql purchase order",
                    "label": "Purchase Order",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "purchase request",
                    "label": "Purchase Request",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "goods received",
                    "label": "Goods Received",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "sql purchase invoice",
                    "label": "Purchase Invoice",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "cash purchase",
                    "label": "Cash Purchase",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "purchase debit note",
                    "label": "Purchase Debit Note",
                    "onboard": 6,
                },
                {
                    "type": "doctype",
                    "name": "purchase returned",
                    "label": "Purchase Returned",
                    "onboard": 7,
                },
            ]

        },
        {
            "label": _("Stock"),
            "items": [
                {
                    "type": "doctype",
                    "name": "stock received",
                    "label": "Stock Received",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "maintain stock group",
                    "label": "Maintain Stock Group",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "maintain stock item",
                    "label": "Maintain Stock Item",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "stock issue",
                    "label": "Stock Issue",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "stock adjustment",
                    "label": "Stock Adjustment",
                    "onboard": 5,
                },
            ]

        }

    ]
    return config