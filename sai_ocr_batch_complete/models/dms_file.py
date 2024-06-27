import requests

from odoo import api, fields, models, _

import time


class File(models.Model):
    _inherit = "dms.file"

    batch_processing = fields.Boolean()

    def action_send_ocr(self):
        self.ensure_one()
        if not self.batch_processing:
            return super().action_send_ocr()
        if not self.env.context.get("job_uuid") and not self.env.context.get(
            "test_queue_job_no_delay"
        ):
            description = _(
                "Send OCR with id {rec_id} to {file_name}"
            ).format(
                rec_id=self.id,
                file_name=self.name,
            )
            job = self.with_delay(description=description).action_send_ocr()
            return "Send OCR with uuid {}".format(job.uuid)
        else:
            return super(
                File, self.with_context(asset_batch_processing=True)
            ).action_send_ocr()


