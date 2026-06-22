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
                self.table_widget.add_columns("PID", "Name", "CPU%", "Memory%")

                # Prime CPU counters once
                psutil.cpu_percent(None)
                for proc in psutil.process_iter():
                    try:
                        proc.cpu_percent(None)
                    except Exception:
                        pass

                self.set_interval(1, self.update_stats)

            def update_stats(self):
                cpu = psutil.cpu_percent(None)
                mem = psutil.virtual_memory().percent
                self.resource_widget.update(f"CPU Usage: {cpu}%\nMemory Usage: {mem}%")

                processes = []

                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        info = proc.info
                        cpu_pct = info['cpu_percent'] / psutil.cpu_count()
                        mem_pct = info['memory_percent']

                        processes.append((
                            cpu_pct,
                            str(info['pid']),
                            (info['name'] or '')[:25],
                            f"{cpu_pct:.1f}",
                            f"{mem_pct:.1f}"
                        ))
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                processes.sort(reverse=True, key=lambda x: x[0])

                self.table_widget.clear()

                for _, pid, name, cpu_pct, mem_pct in processes[:50]:
                    self.table_widget.add_row(pid, name, cpu_pct, mem_pct)

        app = PulseApp()
        app.run()
