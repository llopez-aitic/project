# Copyright 2015-2017 Tecnativa - Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    def toggle_active(self):
        super(ProjectProject, self).toggle_active()
        body = ''
        if self.active is False:
            body = 'Proyecto archivado'
            self.message_post(
                body=body,
                subject='Estado de proyecto',
                message_type="notification",
                subtype="mail.mt_comment")




