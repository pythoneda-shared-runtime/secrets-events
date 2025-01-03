# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/secrets/events/credential_provided.py

This file defines the CredentialProvided class.

Copyright (C) 2024-today boot's pythoneda-shared-runtime/secrets-events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared import attribute, Event, primary_key_attribute
from typing import Dict, List


class CredentialProvided(Event):
    """
    Represents the event in which a credential is provided.

    Class name: CredentialProvided

    Responsibilities:
        - Represent the information associated to the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        name: str,
        value: str,
        metadata: Dict[str, str] = {},
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new CredentialProvided instance.
        :param name: The name of the credential.
        :type name: str
        :param value: The name of the credential.
        :type value: str
        :param metadata: The additional metadata.
        :type metadata: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._name = name
        self._value = value
        self._metadata = metadata
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the credential.
        """
        return self._name

    @property
    @attribute
    def value(self) -> str:
        """
        Retrieves the value of the credential.
        """
        return self._value

    @property
    @attribute
    def metadata(self) -> Dict[str, str]:
        """
        Retrieves the metadata of the event.
        """
        return self._metadata


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
