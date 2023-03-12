from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class TuyaDeviceInfo:
    uuid: str
    local_key: str
    device_id: str
    device_name: str
    product_id: str
    product_name: str | None
    category: str | None


class AbstaractTuyaDeviceManager(ABC):
    @abstractmethod
    async def get_device_info(
        self,
        mac_address: str,
        force_update: bool = False,
    ) -> TuyaDeviceInfo | None:
        """Get the rssi of the device."""
        pass
