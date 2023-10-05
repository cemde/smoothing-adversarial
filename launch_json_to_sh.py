import json
import os
from typing import Any

class JSONWithCommentsDecoder(json.JSONDecoder):
    def __init__(self, **kw):
        super().__init__(**kw)

    def decode(self, s: str) -> Any:
        s = '\n'.join(l for l in s.split('\n') if not l.lstrip(' ').startswith('//'))
        return super().decode(s)


def generate_shell_script(configuration):
    if configuration["type"] != "python" or configuration["request"] != "launch":
        return None

    program = configuration.get("program", "")
    args = configuration.get("args", [])
    cwd = configuration.get("cwd", "${workspaceFolder}")

    shell_script = f"python {os.path.join(cwd, program)}"
    for arg in args:
        shell_script += f" {arg}"

    return shell_script

def main():
    launch_json_path = ".vscode/launch.json"  # Change this to the path of your launch.json file
    with open(launch_json_path, "r") as file:
        launch_config = json.load(file, cls=JSONWithCommentsDecoder)

    if "configurations" in launch_config:
        for config in launch_config["configurations"]:
            shell_script = generate_shell_script(config)
            if shell_script:
                print(shell_script)

if __name__ == "__main__":
    main()
