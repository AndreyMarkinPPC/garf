# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for defining exceptions."""

from __future__ import annotations


class GaarfError(Exception):
  """Base exception."""


class GaarfQueryException(GaarfError):
  """Base exception for Gaarf queries."""


class GaarfParserException(GaarfError):
  """Base exception for Gaarf parsers."""


class GaarfCustomizerException(GaarfParserException):
  """Specifies incorrect customizer."""


class GaarfVirtualColumnException(GaarfParserException):
  """Specifies incorrect virtual column type."""


class GaarfFieldException(GaarfQueryException):
  """Specifies incorrect Google Ads API field."""


class GaarfMacroException(GaarfQueryException):
  """Specifies incorrect macro in Gaarf query."""


class GaarfResourceException(GaarfQueryException):
  """Specifies incorrect resource name in Google Ads API."""
