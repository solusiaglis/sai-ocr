# Part of HG Custom Modules.
{
    "name": "Odoo 16 OCR Queue Job",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "summary": "OCR",
    "website": "https://github.com/OCA/dms",
    "author": "SAI, Odoo Community Association (OCA)",
    "version": "16.0.1.0.0",
    "depends": ["sai_ocr", "queue_job"],
    "application": True,
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "data": [
        "data/queue_data.xml",
    ],
    "images": [
        "static/description/icon.jpg",
    ],
    "auto_install": False,
    "installable": True,
}
