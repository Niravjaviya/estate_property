from odoo import fields, models

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate property'

    name = fields.Char(string='Name', required= True)
    tag_ids= fields.Many2many('estate.property.tag', string='Property tag')
    type_id= fields.Many2one('estate.property.type', string='Property type')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availabity = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected price')
    selling_price = fields.Float(string='Selling price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection ([('north','North'), ('south','South'), ('east','East'), ('west', 'West')], string='Garden Orientation', default='north')
    offer_ids= fields.One2many('estate.property.offer', 'property_id', string="Offers")
class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property Type'

    name= fields.Char(string='Name', required= True)

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate property Tag'

    name= fields.Char(string='Name', required= True)