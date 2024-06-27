import requests

from odoo import api, fields, models, _

import time


class File(models.Model):
    _inherit = "dms.file"

    def action_send_ocr(self):
        if not self.env.context.get("test_queue_job_no_delay", False):
            results = []
            log_error = ""
            for record in self:
                description = _(
                    "Send OCR with id {rec_id} to {file_name}"
                ).format(
                    rec_id=record.id,
                    file_name=record.name,
                )
                record.with_delay(description=description).action_send_ocr()
            return results, log_error

