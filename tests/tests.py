from textual.app import App, ComposeResult
from textual.widgets import Static, DataTable
import psutil


class CMD_pulse:
    name = "pulse"
    aliases = ["top"]
    description = "Shows a real-time view of system usage."
    schema = None
    need_paths = False

    def execute(self, context, flags, args):

        class PulseApp(App):

            def compose(self) -> ComposeResult:
                self.resource_widget = Static()
                yield self.resource_widget

                self.table_widget = DataTable()
                yield self.table_widget

            def on_mount(self):
                # Store column keys for later use
                self.col_pid, self.col_name, self.col_cpu, self.col_mem = self.table_widget.add_columns(
                    "PID", "Name", "CPU%", "Memory%"
                )
                self.row_map = {}  # Map PID to row key
                self.set_interval(0.5, self.update_stats)

            def update_stats(self):
                psutil.cpu_percent(interval=0.1)  # Pre-calculate once
                cpu = psutil.cpu_percent()  # Use cached value

                mem = psutil.virtual_memory().percent
                self.resource_widget.update(f"CPU Usage: {cpu}%\nMemory Usage: {mem}%")

                current_pids = set()
                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        pid = proc.pid
                        current_pids.add(pid)
                        cpu_pct = proc.cpu_percent(interval=None)  # Use cached, don't recalculate
                        mem_pct = proc.memory_percent()

                        if pid in self.row_map:
                            # Update existing row
                            row_key = self.row_map[pid]
                            self.table_widget.update_cell(row_key, self.col_cpu, f"{cpu_pct:.1f}")
                            self.table_widget.update_cell(row_key, self.col_mem, f"{mem_pct:.1f}")
                        else:
                            # Add new row
                            row_key = self.table_widget.add_row(
                                str(pid),
                                proc.name(),
                                f"{cpu_pct:.1f}",
                                f"{mem_pct:.1f}"
                            )
                            self.row_map[pid] = row_key
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                # Remove rows for processes that are no longer running
                for pid in list(self.row_map.keys()):
                    if pid not in current_pids:
                        del self.row_map[pid]

        app = PulseApp()
        app.run()


if __name__ == "__main__":
    cmd = CMD_pulse()
    cmd.execute(None, None, None)