#-*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014-2015 Michael Telahun Makonnen <mmakonnen@gmail.com> and
#    One Click Software <http://oneclick.solutions>.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

{
    'name': 'Accrual',
    'version': '1.1',
    'category': 'Human Resources',
    'description': """
Accruals
========

An Accrual is any benefit (usually time) that accrues on behalf of an employee over an extended
period of time. This can be vacation days, sick days, or a simple time bank. The actual policy
and mechanics of accrual should be handled by other modules. This module only provides
the basic framework for recording the data.
    """,
    'author':'Michael Telahun Makonnen <mmakonnen@gmail.com> and One Click Software',
    'website':'http://oneclick.solutions',
    'depends': [
        'hr',
        'hr_holidays',
        'hr_holidays_extension',
    ],
    'init_xml': [
    ],
    'update_xml': [
        'security/ir.model.access.csv',
        'hr_accrual_view.xml',
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
