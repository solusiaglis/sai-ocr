from odoo import fields, models

MONTH_SELECTION = [
    ("1", "January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April"),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "August"),
    ("9", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]

ONBOARDING_STEP_STATES = [
    ("not_done", "Not done"),
    ("just_done", "Just done"),
    ("done", "Done"),
]
DASHBOARD_ONBOARDING_STATES = ONBOARDING_STEP_STATES + [("closed", "Closed")]


class ResCompany(models.Model):
    _inherit = "res.company"

    sai_api_url = fields.Char(string="API Url")
    sai_api_key = fields.Char(string="API Key")
    sai_workspace_id = fields.Char(string="Workspace Id")
    sai_journal_project_id = fields.Char(string="Journal Project Id")
    sai_bill_project_id = fields.Char(string="Bill Project Id")
    sai_invoice_project_id = fields.Char(string="Invoice Project Id")
