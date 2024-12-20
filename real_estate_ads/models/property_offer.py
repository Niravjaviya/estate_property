from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offers'

    price= fields.Float(string="Price")
    status= fields.Selection ([('accepted','Accepted'), ('refused','Refused')], string='Status')
    partner_id=fields.Many2one('res.partner', string='Customer')
    property_id=fields.Many2one('estate.property', string='Property')
    validity= fields.Integer(string="Validity")
    deadline= fields.Date(string="Deadline", compute= '_compute_deadline', inverse="_inverse_deadline")
    creation_date= fields.Date(string="Creation Date")

    # _sql_constraints = [
    #     ('check_validity', 'check(validity>0)', 'Deadline can not be before creation date')
    # ]

    @api.depends("validity", "creation_date")
    def _compute_deadline(self):
         for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline= rec.creation_date + timedelta(days= rec.validity)
            else:
                rec.deadline= False
    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity= (rec.deadline - rec.creation_date).days
            else:
                rec.validity= False

    
    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
        return super(PropertyOffer, self).create(vals)

    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                if rec.deadline <= rec.creation_date:
                     raise ValidationError(self.env._("Deadline can not be before creation date"))

