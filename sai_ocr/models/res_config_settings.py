from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sai_api_url = fields.Char(
        string="API url", related="company_id.sai_api_url", readonly=False
    )
    sai_api_key = fields.Char(
        string="API Key", related="company_id.sai_api_key", readonly=False
    )
    sai_workspace_id = fields.Char(
        string="Workspace Id", related="company_id.sai_workspace_id", readonly=False
    )
    sai_journal_project_id = fields.Char(
        string="Journal Project Id",
        related="company_id.sai_journal_project_id",
        readonly=False,
    )
    sai_bill_project_id = fields.Char(
        string="Bill Project Id",
        related="company_id.sai_bill_project_id",
        readonly=False,
    )
    sai_invoice_project_id = fields.Char(
        string="Invoice Project Id",
        related="company_id.sai_invoice_project_id",
        readonly=False,
    )
