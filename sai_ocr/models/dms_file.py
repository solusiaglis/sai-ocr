import requests

from odoo import api, fields, models, _

import time


class File(models.Model):
    _inherit = "dms.file"

    entitiy_id = fields.Char("Entitiy Id")
    send_response_json = fields.Char("Send Response JSON")
    send_ocr = fields.Boolean("Send OCR", compute="_compute_send_ocr")
    receive_ocr = fields.Boolean("Receive OCR", compute="_compute_receive_ocr")
    receive_response_json = fields.Char("Receive Response JSON")
    ocr_share_url = fields.Char("OCR share url")

    @api.depends("send_response_json")
    def _compute_send_ocr(self):
        for rec in self:
            rec.send_ocr = False
            if not rec.send_response_json:
                rec.send_ocr = True

    @api.depends("send_response_json", "receive_response_json")
    def _compute_receive_ocr(self):
        for rec in self:
            rec.receive_ocr = False
            if rec.send_response_json and not rec.receive_response_json:
                rec.receive_ocr = True

    def process_send_ocr(self):
        xuser = self.env.user.company_id

        workspace_id = xuser.sai_workspace_id
        project_id = False

        # api_url = xuser.sai_api_url
        api_url = "https://go.v7labs.com/api"
        api_key = xuser.sai_api_key

        # url = f"{api_url}/workspaces/{workspace_id}/projects/{project_id}/entities"

        headers = {"X-API-KEY": api_key}
        for rec in self:
            if not rec.send_response_json:

                if rec.directory_id.ocr_model_type == "journal":
                    project_id = xuser.sai_journal_project_id
                if rec.directory_id.ocr_model_type == "bill":
                    project_id = xuser.sai_bill_project_id
                if rec.directory_id.ocr_model_type == "invoice":
                    project_id = xuser.sai_invoice_project_id

                if project_id:
                    rec.ocr_share_url = rec.get_base_url() + rec._get_share_url()

                    xfile_url = rec.ocr_share_url
                    if xfile_url:

                        payload = {
                            "fields": {
                                "invoice": { 
                                    "file_name": rec.name,
                                    "file_url": xfile_url,
                                }
                            }
                        }

                        url = f"{api_url}/workspaces/{workspace_id}/projects/{project_id}/entities"

                        try:
                            response = requests.post(url, json=payload, headers=headers, timeout=30)
                            response.raise_for_status()  # Raises an exception for HTTP errors
                            if response.status == 200:
                                rec.entitiy_id = response.json()["id"]
                                rec.send_response_json = response.json()
                                print(response.json())  # Or handle the response data as needed

                        except requests.exceptions.RequestException as e:
                            print(f"An error occurred: {e}")

    def action_send_ocr(self):
        for rec in self:
            rec.process_send_ocr()

    def process_receive_ocr(self):
        xuser = self.env.user.company_id

        workspace_id = xuser.sai_workspace_id
        project_id = xuser.sai_invoice_project_id

        # api_url = xuser.sai_api_url
        api_url = "https://go.v7labs.com/api"
        api_key = xuser.sai_api_key

        headers = {"X-API-KEY": api_key}

        for rec in self:
            if not rec.receive_response_json:
                entitiy_id = rec.entitiy_id
                property_id = "line-items"

                url = f"{api_url}/workspaces/{workspace_id}/projects/{project_id}/entities/{entitiy_id}/properties/{property_id}/ground_truth"

                payload = { "ground_truth": True }
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "X-API-KEY": api_key
                }

                try:
                    response = requests.put(url, json=payload, headers=headers, timeout=30)
                    response.raise_for_status()  # Raises an exception for HTTP errors
                    if response.json()["status"] == "complete":
                        rec.receive_response_json = response.json()
                        print(response.json())  # Or handle the response data as needed
                       
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred: {e}")

    def action_receive_ocr(self):
        for rec in self:
            rec.process_receive_ocr()

    def action_create_journal(self):
        return

    def action_create_bill(self):
        return

    def action_create_invoice(self):
        return
