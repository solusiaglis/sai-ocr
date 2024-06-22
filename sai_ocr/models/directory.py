from odoo import _, api, fields, models, tools

class DmsDirectory(models.Model):
    _inherit = "dms.directory"

    ocr_model_type = fields.Selection(
        selection=[
            ("journal", _("Journal")),
            ("bill", _("Bill")),
            ("invoice", _("Invoice")),
            ("others", _("Others")),
        ],
        default="others",
        required=True,
        help="""This setting to recognize the type of the folder to
        process into OCR model.""",
    )

