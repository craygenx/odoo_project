from datetime import timedelta
from odoo import models, fields, api

class ToDoTask(models.Model):
    _name = 'to_do_task'
    _description = 'To-Do task'

    name = fields.Char(string='name', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    days_left = fields.Integer(string='Days Left', compute='_compute_days_left')

    @api.depends('deadline')
    def _compute_days_left(self):
        for task in self:
            if task.deadline:
                deadline_date = fields.Date.from_string(task.deadline)
                today_date = fields.Date.today()
                task.days_left = (deadline_date - today_date).days
            else:
                task.days_left = 0

    def send_emails(self):
        tasks = self.search([('deadline', '<=', fields.Date.today() + timedelta(days=3)),
                            ('deadline', '<=', fields.Date.today())])
        template = self.env.ref('custom_module.email_template_to_do_task_reminder')
        for task in tasks:
            self.env['mail.template'].browse(template.id).send_mail(task.id, force_send=True)