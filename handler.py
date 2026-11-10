import time
from typing import Callable, Optional, Dict


class ClickHandler:
    """Manages click trigger events and hotkey action bindings."""

    def __init__(self, click_callback: Optional[Callable[[], None]] = None) -> None:
        self.click_callback = click_callback
        self.hotkeys: Dict[str, Callable[[], None]] = {}
        self._is_active: bool = False

    def register_hotkey(self, key_combo: str, callback: Callable[[], None]) -> None:
        """Binds a shortcut combination to a specific callback action."""
        normalized_combo = key_combo.strip().lower()
        self.hotkeys[normalized_combo] = callback

    def unregister_hotkey(self, key_combo: str) -> bool:
        """Removes a registered hotkey binding."""
        normalized_combo = key_combo.strip().lower()
        if normalized_combo in self.hotkeys:
            del self.hotkeys[normalized_combo]
            return True
        return False

    def handle_key_event(self, key_combo: str) -> bool:
        """Dispatches an incoming key press event to registered callbacks."""
        normalized_combo = key_combo.strip().lower()
        if normalized_combo in self.hotkeys:
            self.hotkeys[normalized_combo]()
            return True
        return False

    def trigger_click(self) -> None:
        """Executes the configured click callback if active."""
        if self._is_active and self.click_callback:
            self.click_callback()

    def set_active(self, active: bool) -> None:
        """Updates the handler active status for event processing."""
        self._is_active = active
