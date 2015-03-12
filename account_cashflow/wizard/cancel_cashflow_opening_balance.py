# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    
#    Copyright (c) 2011 Noviat nv/sa (www.noviat.be). All rights reserved.
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from osv import osv, fields
import netsvc
from tools.translate import _

class cancel_cashflow_opening_balance(osv.osv_memory):
    _name = 'cancel.cashflow.opening.balance'
    _description = 'Cancel selected Cash Flow Opening Balances'
       
    def cancel_balances(self, cr, uid, ids, context):       
        line_ids = context['active_ids']
        line_obj = self.pool.get('account.cashflow.opening.balance')
        line_obj.write(cr, uid, line_ids, {'state': 'draft'}, context=context)
        return {}

cancel_cashflow_opening_balance()
