# Part of HG Custom Modules.
{
    "name": "Odoo 16 OCR",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "summary": "OCR",
    "website": "https://github.com/OCA/dms",
    "author": "SAI, Odoo Community Association (OCA)",
    "version": "16.0.1.0.0",
    "depends": ["base", "base_setup", "dms"],
    "application": True,
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "data": [
        "views/res_config_settings_views.xml",
        "views/dms_file.xml",
        "views/directory.xml",
    ],
    "images": [
        "static/description/icon.jpg",
    ],
    "auto_install": False,
    "installable": True,
}
