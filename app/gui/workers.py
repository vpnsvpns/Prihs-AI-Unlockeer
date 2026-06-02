from PySide6.QtCore import QObject, Signal, QRunnable
from app.core.logger import logger
from app.core.hosts_manager import HostsManager

class WorkerSignals(QObject):
    finished = Signal(str, bool, str)
    status_ready = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

class HostsWorker(QRunnable):
    def __init__(self, action: str, manager: HostsManager, parent=None):
        super().__init__()
        self.action = action
        self.manager = manager
        self.signals = WorkerSignals(parent)

    def run(self):
        try:
            if self.action in ("install", "update"):
                result = self.manager.update()
            elif self.action == "uninstall":
                result = self.manager.restore()
            elif self.action == "open":
                from app.gui.hosts_helpers import open_hosts_file_sync
                result, error = open_hosts_file_sync()
                self.signals.finished.emit(self.action, result, error or "")
                return
            else:
                result = False
            self.signals.finished.emit(self.action, result, "")
        except Exception as e:
            logger.exception("Hosts operation failed")
            self.signals.finished.emit(self.action, False, str(e))

class VersionWorker(QRunnable):
    def __init__(self, manager: HostsManager, parent=None):
        super().__init__()
        self.manager = manager
        self.signals = WorkerSignals(parent)

    def run(self):
        status = self.manager.check_status()
        self.signals.status_ready.emit(status)
