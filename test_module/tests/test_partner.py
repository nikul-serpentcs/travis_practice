from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        customer = self.env.ref('base.res_partner_3')

    def test_write(self):
        customer.write({'committee_position': 'ABC'})
