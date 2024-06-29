import requests

from odoo import api, fields, models, _

import time


class File(models.Model):
    _inherit = "dms.file"

    def process_send_ocr(self):
        for rec in self:
            if not rec.env.context.get("job_uuid") and not rec.env.context.get(
                "test_queue_job_no_delay"
            ):
                description = _(
                    "Send OCR with id {rec_id} to {file_name}"
                ).format(
                    rec_id=rec.id,
                    file_name=rec.name,
                )

                job_send = rec.with_delay(description=description).process_send_ocr()

                # job1 = rec.delayable().process_send_ocr()
                # job2 = rec.delayable().process_receive_ocr()

                # job1.on_done(job2) \
                # .set(priority=30) \
                # .set(description=_(description)) \
                # .delay()
                
                return "Send OCR with uuid {}".format(job_send.uuid)
            else:
                return super().process_send_ocr()
            

    def process_receive_ocr(self):
        for rec in self:
            if not rec.env.context.get("job_uuid") and not rec.env.context.get(
                "test_queue_job_no_delay"
            ):
                description = _(
                    "Receive OCR with id {rec_id} to {file_name}"
                ).format(
                    rec_id=rec.id,
                    file_name=rec.name,
                )

                job_received = rec.with_delay(description=description).process_receive_ocr()

                return "Send OCR with uuid {}".format(job_received.uuid)
            else:
                return super().process_receive_ocr()


