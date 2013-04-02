# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
URL patterns for testing Horizon views.
"""

from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import horizon


urlpatterns = patterns('',
    url(r'^$', 'horizon.views.splash', name='splash'),
    url(r'^auth/', include('openstack_auth.urls')),
    url(r'', include(horizon.urls)),
    url(r'^qunit/$',
        TemplateView.as_view(template_name="horizon/qunit.html"),
        name='qunit_tests')
)

urlpatterns += staticfiles_urlpatterns()