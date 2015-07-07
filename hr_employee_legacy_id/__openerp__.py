#-*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011-2015 Michael Telahun Makonnen <mmakonnen@gmail.com> and
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
    'name': 'Legacy Employee ID',
    'version': '1.1',
    'category': 'Human Resources',
    'description': """
Employee Identification Numbers from Previous System
====================================================

When switching from a legacy HR system to a new one. It may be necessary
to have a record of the ID No. used in the previous system.
    """,
    'author':'Michael Telahun Makonnen <mmakonnen@gmail.com> and One Click Software',
    'website':'http://oneclick.solutions',
    'depends': [
        'hr',
    ],
    'init_xml': [
    ],
    'update_xml': [
        'hr_view.xml',
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
