from odoo import fields, models, api
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offers'

    price= fields.Float(string="Price")
    status= fields.Selection ([('accepted','Accepted'), ('refused','Refused')], string='Status')
    partner_id=fields.Many2one('res.partner', string='Customer')
    property_id=fields.Many2one('estate.property', string='Property')
    validity= fields.Integer(string="Validity")
    deadline= fields.Date(string="Deadline", compute= '_compute_deadline', inverse="_inverse_deadline")

    @api.model
    def _set_create_date(self):
        return fields.Date.today()
    
    creation_date= fields.Date(string="Creation Date", default=_set_create_date)

    @api.depends("validity", "deadline")
    def _compute_deadline(self):
         for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline= rec.creation_date + timedelta(days= rec.validity)
            else:
                rec.deadline= False
    def _inverse_deadline(self):
        for rec in self:
            rec.validity= (rec.deadline - rec.creation_date).days
