# -*- coding: utf-8 -*-
# Copyright © tandemdude 2020-present
#
# This file is part of Lightbulb.
#
# Lightbulb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lightbulb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Lightbulb. If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

__all__ = [
    "LightbulbError",
    "CommandNotFound",
    "CommandInvocationError",
    "CommandIsOnCooldown",
    "CheckFailure",
    "NotOwner",
    "OnlyInGuild",
    "OnlyInDM",
    "BotOnly",
    "WebhookOnly",
    "HumanOnly",
    "NSFWChannelOnly",
]

import typing as t


class LightbulbError(Exception):
    pass


class CommandNotFound(LightbulbError):
    def __init__(self, *args: t.Any, invoked_with: str) -> None:
        super().__init__(*args)
        self.invoked_with = invoked_with


class CommandInvocationError(LightbulbError):
    def __init__(self, *args: t.Any, original: Exception) -> None:
        super().__init__(*args)
        self.original = original
        """The exception that caused this to be raised. Also accessible through ``CommandInvocationError.__cause__``"""
        self.__cause__ = original


class CommandIsOnCooldown(LightbulbError):
    def __init__(self, *args: t.Any, retry_after: float) -> None:
        super().__init__(*args)
        self.retry_after = retry_after
        """The amount of time remaining until the cooldown expires."""


class CheckFailure(LightbulbError):
    pass


class NotOwner(CheckFailure):
    pass


class OnlyInGuild(CheckFailure):
    pass


class OnlyInDM(CheckFailure):
    pass


class BotOnly(CheckFailure):
    pass


class WebhookOnly(CheckFailure):
    pass


class HumanOnly(CheckFailure):
    pass


class NSFWChannelOnly(CheckFailure):
    pass
