from odoo import fields, models, api

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate property'

    name = fields.Char(string='Name', required= True)
    state= fields.Selection([
         ('new', 'New'), 
         ('received', 'Offer Received'), 
         ('accepted', 'Offer Accepted'), 
         ('sold', 'Sold'), 
         ('cancel', 'Cancelled')
         ], default='new', string='Status')
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
    sales_id= fields.Many2one('res.users', string="Salesman")
    buyer_id= fields.Many2one('res.partner', string="Buyer", domain= [('is_company','=',True)])
    phone= fields.Char(string='Phone', related='buyer_id.phone')

    @api.onchange("living_area", "garden_area")

    def _onchange_total_area(self):
            self.total_area = self.living_area + self.garden_area
    total_area= fields.Integer(string="Total Area")

    def action_sold(self):
         self.state = 'sold'

    def action_cancel(self):
         self.state = 'cancel'


    
class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property Type'

    name= fields.Char(string='Name', required= True)

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate property Tag'

    name= fields.Char(string='Name', required= True)